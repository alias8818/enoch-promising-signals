# Gradient-Chunked Adafactor with Selective Factorization for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-chunked-adafactor-with-selective-factorization-for-tiny-vram-training-ba09c5df955a`
Run ID: `gradient-chunked-adafactor-with-selective-factorization-for-tiny-vram-training-ba09c5df955a-20260531T163431348982+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f092b61d322c

## What looked useful

The mechanism is worth future constrained-memory testing: optimizer state falls from AdamW's 2.0x parameter bytes to 0.0093x, and chunking directly removes large factored-update temporaries. The cost is material throughput loss, with chunked selective Adafactor running at 55% of AdamW throughput in this implementation.

## Boundaries and scale limits

No real-corpus GPT-2-small-class run, no enforced tiny-VRAM cap, no full validation loss, no mixed precision or checkpointing integration, and no long-run stability evidence. End-to-end peak memory in the small transformer was activation-dominated, so the run does not prove an end-to-end tiny-VRAM training win.

## Claim scope

On a 3.45M-parameter CUDA tiny-transformer synthetic language-model task, selective factored Adafactor reduced optimizer state by 214x versus AdamW while reaching similar but worse short-run loss; on an 8192 x 8192 CUDA matrix probe, row-chunked factored update materialization reduced optimizer temporary peak allocation by 48x versus naive full materialization.

## Why it stopped

No-paper closure: the evidence is a bounded synthetic/probe useful signal, not direct full-scale or constrained-memory validation.

## Recommended next action

Run a bounded deepen follow-up with an enforced CUDA memory cap on a GPT-2-small-class or larger parameter-matched transformer, comparing AdamW, naive selective Adafactor, and chunked selective Adafactor on peak memory, throughput, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained-memory validation of chunked selective Adafactor
- Success threshold: Chunked selective Adafactor enables at least 1.5x larger feasible batch size or at least 25% lower end-to-end peak memory than the strongest feasible baseline while keeping validation loss within 5% and throughput at or above 50% of that baseline.
- Stop condition: Stop if chunking does not reduce end-to-end peak memory under the cap, if validation loss is more than 10% worse after a minimal hyperparameter sweep, or if throughput falls below 33% of the strongest feasible baseline.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-chunked-adafactor-with-selective-factorization-for-tiny-vram-training-ba09c5df955a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
