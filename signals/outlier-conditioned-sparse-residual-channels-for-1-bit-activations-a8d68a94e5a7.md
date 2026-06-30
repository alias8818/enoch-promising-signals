# Outlier-Conditioned Sparse Residual Channels for 1-bit Activations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `outlier-conditioned-sparse-residual-channels-for-1-bit-activations-a8d68a94e5a7`
Run ID: `outlier-conditioned-sparse-residual-channels-for-1-bit-activations-a8d68a94e5a7-20260521T204102095214+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a296f7a6b8d

## What looked useful

Across 5 seeds on the tail-dependent teacher task, outlier residual channels reached 0.6183 mean test accuracy versus 0.4172 for binary activations and 0.4322 for matched random sparse residuals, with positive paired deltas in all seeds. On the sign-teacher control, outlier residuals matched binary accuracy and did not provide a gain.

## Boundaries and scale limits

No end-to-end trained 1-bit activation model, no transformer/GPT-2-small-class baseline, no natural dataset, no hardware throughput measurement; evidence is synthetic and representation-level only.

## Claim scope

Controlled fixed-random-feature proxy: outlier-conditioned sparse residual channels on top of 1-bit sign activations improve classification when labels depend on high-magnitude activation tails, and do not help on a sign-only control task.

## Why it stopped

No-paper closure: the local proxy supports the proposed mechanism but does not directly validate trained 1-bit activation networks or full-scale model behavior.

## Recommended next action

Run a bounded end-to-end trainable 1-bit MLP or tiny transformer ablation on a real dataset with parameter/FLOP-matched binary, random residual, dense residual, and outlier-conditioned residual variants.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model test of outlier-conditioned residual channels for 1-bit activations
- Success threshold: Outlier-conditioned residual variant improves the primary validation metric by at least 2 percentage points accuracy or 5 percent relative loss/perplexity versus binary and matched random residual controls at comparable residual density in at least 3 seeds.
- Stop condition: Stop if the outlier-conditioned variant fails to beat matched random residual controls on the real-dataset validation metric, or if the gain requires dense residual density or materially higher parameter/FLOP budget.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-conditioned-sparse-residual-channels-for-1-bit-activations-a8d68a94e5a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
