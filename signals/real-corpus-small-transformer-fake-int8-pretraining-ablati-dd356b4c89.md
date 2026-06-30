# Real-Corpus Small-Transformer Fake INT8 Pretraining Ablation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-small-transformer-fake-int8-pretraining-ablati-dd356b4c89`
Run ID: `real-corpus-small-transformer-fake-int8-pretraining-ablati-dd356b4c89-20260608T091105189729+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: INT8 Fake-Quantized Tiny Pretraining: enoch://control-plane/projects/int8-fake-quantized-tiny-pretraining-9c9002f1b922/runs/int8-fake-quantized-tiny-pretraining-9c9002f1b922-20260608T041710545549+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/51f62cf8b7b9

## What looked useful

Fake INT8 pretraining did not materially degrade final validation loss in the tested small real-corpus setting. Weight-only fake INT8 was effectively tied with dense, and weights+activations had a worst observed validation-loss penalty of +0.258%, below the predefined 5% threshold. Fake quantization added runtime overhead because it was implemented as unfused PyTorch operations.

## Boundaries and scale limits

Small char-level corpus and model only; no subword tokenizer, GPT-2-small-class scale, broad corpus mix, long schedule, true INT8 kernels, inference throughput, or multi-seed robustness beyond two seeds.

## Claim scope

In a Tier 1 controlled direct test on Tiny Shakespeare, a 1.83M parameter character-level causal transformer trained for 1,200 steps with fake INT8 quantization-aware linear weights, or linear weights plus linear inputs/activations, matched the dense baseline within 0.258% final validation loss across two seeds.

## Why it stopped

Tier 1 direct small-scale validation passed the predefined loss threshold, but the evidence is not publication-grade because it is limited to a 1.83M parameter char-level model and short real-corpus training.

## Recommended next action

Run a bounded deepen follow-up on a subword-tokenized 10M+ token corpus or GPT-2-small-class setup with the same dense, weight-only, and weight+activation fake INT8 variants and at least three seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword Small-Transformer Fake INT8 Pretraining Robustness Check
- Success threshold: Both fake INT8 variants finish within 2% final validation loss of the dense baseline on every seed, with no divergence or persistent training instability.
- Stop condition: Stop as negative or mixed if either fake INT8 variant exceeds 2% validation-loss degradation on two or more seeds, diverges, or shows persistent instability not present in the dense baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-small-transformer-fake-int8-pretraining-ablati-dd356b4c89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
