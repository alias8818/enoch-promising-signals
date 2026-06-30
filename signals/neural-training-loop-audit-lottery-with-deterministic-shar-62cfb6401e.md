# Neural training-loop audit lottery with deterministic shard recompute

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `neural-training-loop-audit-lottery-with-deterministic-shar-62cfb6401e`
Run ID: `neural-training-loop-audit-lottery-with-deterministic-shar-62cfb6401e-20260520T085536567531+0000`

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

- Parent run decision: Audited Gradient Lottery With Shard Recompute Challenges: enoch://control-plane/projects/audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7/runs/audited-gradient-lottery-with-shard-recompute-challenges-78cd4366a7-20260520T085008349351+0000
- Parent run decision: Verifiable Gradient Lottery on Local Shards: enoch://control-plane/projects/verifiable-gradient-lottery-on-local-shards-b18331d71203/runs/verifiable-gradient-lottery-on-local-shards-b18331d71203-20260520T084201470811+0000

## What looked useful

Across 100 fixed seeds and 500 injected-fault runs, detection rates tracked audit probability: 4/100 at 5%, 12/100 at 10%, 23/100 at 20%, 51/100 at 50%, and 100/100 at full audit. Clean audited controls had 0 false positives, and 10% auditing cost about 15% wall-clock overhead versus the unaudited baseline.

## Boundaries and scale limits

Tested on a small real image dataset and CPU NumPy MLP only; not validated on GPT-2-class models, GPU/mixed-precision kernels, distributed training, production checkpoint storage, adversarial lottery prediction, or dataloader replay under framework nondeterminism.

## Claim scope

In a single-process deterministic NumPy MLP training loop on sklearn digits, hidden lottery auditing by exact shard recompute detects injected post-update state faults when the corrupted shard is selected, produces zero clean false positives across the tested seeds, and has overhead that scales with audit fraction.

## Why it stopped

Tier 2 bounded mechanism evidence is positive, but the validation is too small and framework-simplified for paper-positive claims about modern neural training-loop auditing.

## Recommended next action

Stop this run as no-paper useful evidence; deepen with a framework-level PyTorch/GPT-2-small-class replay audit that validates dataloader, optimizer, mixed-precision, and hidden post-commit lottery mechanics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-level hidden lottery shard recompute for GPT-2-small-class training
- Success threshold: At 10% audit rate, observed detection rate confidence interval contains 10%, clean false-positive rate is 0 in the tested trace, baseline quality is not degraded beyond normal seed variance, and wall-clock overhead is below 25% versus unaudited training.
- Stop condition: Stop as unsupported if deterministic replay has any unexplained clean mismatch, if 10% audit overhead exceeds 50% after reasonable engineering, or if fault detection no longer tracks selected-shard probability under hidden lottery selection.

## Evidence references

- Artifact root: `<local-path>/projects/neural-training-loop-audit-lottery-with-deterministic-shar-62cfb6401e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
