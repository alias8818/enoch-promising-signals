# Tiny-transformer validation of code/math mixture ratios

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09`
Run ID: `tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09-20260522T103404450149+0000`

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

- Parent run decision: Code/Math Mixing Ratios for Tiny Pretraining: enoch://control-plane/projects/code-math-mixing-ratios-for-tiny-pretraining-843b88b27926/runs/code-math-mixing-ratios-for-tiny-pretraining-843b88b27926-20260522T083925051187+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5479b6846b10

## What looked useful

The controlled sweep found a stable mixture-ratio tradeoff: code loss improved monotonically with more code, math loss worsened with more code, and the 50% mixture gave the best macro validation loss in both seeds. This supports mixture-ratio sweeping as a useful small-test mechanism but is not paper-ready.

## Boundaries and scale limits

Synthetic generated Python-like and arithmetic/math text only; character-level tokenizer; about 63k-parameter tiny transformers; two seeds; 1000 optimizer steps; validation by loss only with no execution, answer accuracy, real corpus, BPE-tokenizer, or downstream transfer measurement.

## Claim scope

In a controlled Tier 1 synthetic setup, 48-wide 2-layer character-level causal transformers trained on code/math mixtures showed a consistent interior optimum: the 50% code / 50% math mixture had lower macro held-out code+math loss than pure-code or pure-math endpoints across two seeds.

## Why it stopped

Tier 1 direct test succeeded as mechanism evidence but remains no-paper because the data, tokenizer, model size, seed count, and metrics are too limited for publication-grade validation.

## Recommended next action

Run a bounded deepen test with a real tokenizer and small real code/math corpora, 3 seeds, and ratios concentrated around 25/50/75% code; stop if no interior mixture beats endpoints on macro validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer bounded confirmation of code/math mixture-ratio optimum
- Success threshold: An interior mixture must beat both pure-domain endpoints on mean macro validation loss and in at least 2 of 3 seeds, without worsening either domain loss by more than 10% relative to the nearest specialist endpoint.
- Stop condition: Stop if no interior ratio beats both endpoints on macro validation loss after 3 seeds, or if the effect reverses under real-tokenizer/real-corpus conditions.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
