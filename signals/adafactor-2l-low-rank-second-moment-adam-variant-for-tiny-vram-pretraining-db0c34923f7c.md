# Adafactor-2L: Low-rank second-moment Adam variant for tiny-VRAM pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adafactor-2l-low-rank-second-moment-adam-variant-for-tiny-vram-pretraining-db0c34923f7c`
Run ID: `adafactor-2l-low-rank-second-moment-adam-variant-for-tiny-vram-pretraining-db0c34923f7c-20260622T002922270184+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1dd78a52684f

## What looked useful

The memory-saving mechanism works for optimizer state, dropping state/parameter bytes from about 2.0x to about 1.0x, but the implemented factored update showed a persistent loss gap (+0.179 final loss at 400 steps) and ran at about 62.8% of AdamW throughput.

## Boundaries and scale limits

Tested only a tiny Transformer on synthetic modular-stride token sequences, not real-corpus GPT-2-small-class or larger pretraining; peak-memory savings are small at this scale because activations and parameters dominate.

## Claim scope

On a tiny synthetic causal-LM proxy, a factored-second-moment AdamW prototype reduced optimizer state by about 49.5% versus AdamW but had consistently worse final loss and lower throughput over 3 seeds at 120 and 400 steps.

## Why it stopped

Bounded proxy evidence supports optimizer-state memory reduction but does not support the proposed variant as a paper-ready tiny-VRAM pretraining optimizer because quality and throughput regress versus AdamW.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test a tuned or fused factored update on real text with a GPT-2-small-class or parameter-matched baseline before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tune and validate factored-second-moment AdamW on real-text small LM pretraining
- Success threshold: At least 40% optimizer-state reduction versus AdamW, validation loss or perplexity within 3% of AdamW at matched token budget, and throughput at least 85% of AdamW on the same hardware.
- Stop condition: Stop if the tuned factored optimizer remains more than 5% worse in validation loss/perplexity or below 75% of AdamW throughput while preserving comparable memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-2l-low-rank-second-moment-adam-variant-for-tiny-vram-pretraining-db0c34923f7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
