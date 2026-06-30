# Code/Math Mixing Ratios for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `code-math-mixing-ratios-for-tiny-pretraining-843b88b27926`
Run ID: `code-math-mixing-ratios-for-tiny-pretraining-843b88b27926-20260522T083925051187+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5479b6846b10

## What looked useful

Across n-gram orders 3, 5, and 7, mixed code/math ratios reduced specialist mean bits-per-character by 1.34 to 2.07 bpc relative to the average of code-only and math-only specialist endpoints. The result supports testing mixed-domain ratios in a direct tiny-transformer setup, but does not justify a paper claim.

## Boundaries and scale limits

CPU-only pure-Python proxy; no neural transformer, no real code/math corpus, no tokenizer study, no downstream task evaluation, 5 seeds per ratio, 120k training characters per run.

## Claim scope

In a controlled synthetic character n-gram proxy for tiny pretraining, mixed code/math specialist slices outperformed specialist-only endpoints on held-out code-plus-math loss; the best ratio was shallow between 25% and 50% code within a fixed 60% specialist slice.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic n-gram proxy rather than direct transformer pretraining validation.

## Recommended next action

Run a bounded tiny-transformer follow-up on real code/math/prose corpora with the same ratio grid, matched token budget, at least 3 seeds, and held-out code/math/prose perplexity plus small downstream probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer validation of code/math mixture ratios
- Success threshold: A mixed code/math ratio improves balanced specialist validation loss by at least 5% over both specialist-only endpoints, with overlapping conclusion across seeds and no prose loss degradation larger than 3%.
- Stop condition: Stop if mixed ratios do not beat both endpoints on specialist mean validation loss after matched-budget training, or if gains vanish across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/code-math-mixing-ratios-for-tiny-pretraining-843b88b27926`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
