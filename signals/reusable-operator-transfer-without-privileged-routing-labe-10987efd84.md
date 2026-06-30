# Reusable operator transfer without privileged routing labels

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `reusable-operator-transfer-without-privileged-routing-labe-10987efd84`
Run ID: `reusable-operator-transfer-without-privileged-routing-labe-10987efd84-20260611T050037228729+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Parameter-matched neural baseline for reusable operator transfer: enoch://control-plane/projects/parameter-matched-neural-baseline-for-reusable-operator-tr-6338ce46c9/runs/parameter-matched-neural-baseline-for-reusable-operator-tr-6338ce46c9-20260611T022902087230+0000
- Parent run decision: Neural Reusable Operator Transfer vs Fact Memory Baseline: enoch://control-plane/projects/neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb/runs/neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb-20260611T012539310740+0000

## What looked useful

No-label reusable operator transfer is mechanically viable when source operators are identifiable: transfer/oracle MSE ratio was approximately 1.000 at target sizes 64, 256, and 1024, and unrelated-source transfer remained much worse. The practical benefit was limited to low target data: transfer reduced MSE vs target-only no-transfer by 83.44% at n=64, but only 0.41% at n=256 and 0.09% at n=1024.

## Boundaries and scale limits

CPU-only NumPy validation; synthetic linear operators only; no neural representation learning, nonlinear operators, real datasets, high-dimensional structured data, or long training. The transfer advantage over no-transfer vanished by 256 target examples and remained absent at 1024 examples.

## Claim scope

In a synthetic mixture-of-linear-operators benchmark with four reusable operators, 10 fixed seeds, hidden routing labels withheld from the main method, and shifted source/target routers, unlabeled source operator recovery plus target pseudo-route training matched privileged-label oracle MSE and strongly improved over target-only no-transfer only in the 64-example target regime.

## Why it stopped

Bounded validation supports the mechanism but fails the stricter paper threshold because the real no-transfer baseline catches up by 256 target examples; this is not a full negative on all operator-transfer settings, but it is insufficient for a publication-grade claim.

## Recommended next action

Stop this follow-up as no-paper useful evidence: future work should only continue if it moves to a direct nonlinear or real benchmark with a target-only baseline that cannot trivially catch up at moderate target sample sizes.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/reusable-operator-transfer-without-privileged-routing-labe-10987efd84`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
