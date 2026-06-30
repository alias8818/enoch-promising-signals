# Audited Gradient Lottery With Shard Recompute Challenges

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7`
Run ID: `audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7-20260520T085008349351+0000`

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

- Parent run decision: Verifiable Gradient Lottery on Local Shards: enoch://control-plane/projects/verifiable-gradient-lottery-on-local-shards-b18331d71203/runs/verifiable-gradient-lottery-on-local-shards-b18331d71203-20260520T084201470811+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/080b78960275

## What looked useful

Empirical detection rates matched 1 - C(S-k,a)/C(S,a) within 2.8 percentage points maximum error over 2000 trials per scenario; selected 64-shard/8-audit cases matched within 0.35, 0.19, and 0.21 percentage points for 1, 4, and 8 corrupt shards respectively; false positives were 0.0.

## Boundaries and scale limits

Single synthetic batch, logistic regression only, deterministic CPU NumPy recomputation, no distributed workers, no neural network training loop, no GPU nondeterminism, no optimizer-state attacks, no adaptive tolerance-aware adversary, and no end-to-end model quality evaluation.

## Claim scope

Small direct NumPy logistic-regression mechanism test: after gradient commitment, random shard recomputation detects shard-sparse gradient corruption at the closed-form lottery probability with zero observed false positives across 40 controlled scenarios.

## Why it stopped

Tier 1 controlled direct test met the mechanism threshold, but evidence remains small-scale and no-paper; closure is a useful signal rather than publication readiness.

## Recommended next action

Run a bounded medium direct test in a small neural training loop with committed batch provenance, deterministic/tolerance-aware recomputation, dense and shard-sparse attack controls, and train-quality impact metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural training-loop audit lottery with deterministic shard recompute
- Success threshold: Across at least 5 seeds, false positives stay below 0.5%, shard-sparse detection remains within 5 percentage points of lottery theory, audited honest training stays within 1% relative validation loss or accuracy of unaudited honest training, and audit overhead is measured rather than assumed.
- Stop condition: Stop if nondeterministic recomputation requires a tolerance that allows practically harmful corruptions to evade detection, or if audit overhead exceeds full-gradient recomputation without a clear systems optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
