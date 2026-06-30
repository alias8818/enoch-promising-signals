# Real-tokenizer bounded confirmation of code/math mixture-ratio optimum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae`
Run ID: `real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae-20260522T111505361609+0000`

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

- Parent run decision: Tiny-transformer validation of code/math mixture ratios: enoch://control-plane/projects/tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09/runs/tiny-transformer-validation-of-code-math-mixture-ratios-1c2bea5a09-20260522T103404450149+0000
- Parent run decision: Code/Math Mixing Ratios for Tiny Pretraining: enoch://control-plane/projects/code-math-mixing-ratios-for-tiny-pretraining-843b88b27926/runs/code-math-mixing-ratios-for-tiny-pretraining-843b88b27926-20260522T083925051187+0000

## What looked useful

GPT-2 BPE best r_code values were [0.45, 0.50, 0.45, 0.40, 0.45] on the primary grid and [0.45, 0.475, 0.425, 0.40, 0.45] on a finer smoothing sensitivity run. All seeds were interior; median best r_code was 0.45. Pure-domain baselines were much worse, while gain over r=0.5 was small at about 0.00264 nats/token. A whitespace-tokenizer ablation shifted the optimum lower to median 0.35, showing tokenizer dependence.

## Boundaries and scale limits

No Transformer was trained; math corpus retained 10 Wikipedia pages after throttling; some splits did not fill the 200k train and 50k validation token caps; result is a tokenizer/count mechanism signal, not a full model-training law.

## Claim scope

On a bounded real-tokenizer count-distribution test using local CPython standard-library code and Wikipedia math text, GPT-2 BPE held-out balanced NLL has a stable interior code/math mixture optimum near r_code=0.44-0.45 across five fixed document-split seeds.

## Why it stopped

Evidence supports the bounded real-tokenizer count-mixture mechanism but is not paper-positive because it lacks actual model-training validation.

## Recommended next action

Stop as no-paper useful signal; next bounded direct-evidence step is small GPT-style model training at r_code values around 0.35, 0.45, and 0.55 using the same real tokenizer and held-out code/math NLL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model confirmation of the GPT-2 BPE code/math mixture optimum
- Success threshold: Median best trained-model r_code is between 0.40 and 0.50 across seeds, beats r=0.5 by at least 0.005 nats/token balanced NLL or a predeclared practical threshold, and beats pure-domain baselines by a clear margin.
- Stop condition: Stop if trained-model balanced NLL is flat within noise across 0.35-0.55 or if the optimum moves to a pure-domain endpoint on two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-tokenizer-bounded-confirmation-of-code-math-mixture-r-7ac585faae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
