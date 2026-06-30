# Parameter-matched neural baseline for reusable operator transfer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `parameter-matched-neural-baseline-for-reusable-operator-tr-6338ce46c9`
Run ID: `parameter-matched-neural-baseline-for-reusable-operator-tr-6338ce46c9-20260611T022902087230+0000`

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

- Parent run decision: Neural Reusable Operator Transfer vs Fact Memory Baseline: enoch://control-plane/projects/neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb/runs/neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb-20260611T012539310740+0000
- Parent run decision: Memory Doctrine: Reusable Operator Learning vs Fact Recall: enoch://control-plane/projects/memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689/runs/memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689-20260610T234620332680+0000

## What looked useful

Reusable operator transfer achieved mean held-out 16-shot MSE 0.003282 versus 0.101237 for the parameter-matched dense baseline, winning 5/5 seeds; zero-shot MSE was 0.001813 versus 0.232654. Shuffled-label and scratch controls were much worse than the pretrained reusable model.

## Boundaries and scale limits

Synthetic task only; true composition labels are supplied; generator matches the reusable model class; no learned routing, natural data, language modeling, or large-scale training was tested.

## Claim scope

On a synthetic held-out composition benchmark with known primitive labels and a generator matching the reusable-operator factorization, a reusable operator library outperformed a parameter-matched dense conditioned MLP and controls across five fixed seeds.

## Why it stopped

Tier 2 synthetic evidence supports the scoped mechanism but is not broad or natural-task evidence and is not paper-positive.

## Recommended next action

Stop this branch as no-paper useful signal; run one bounded deepen follow-up that removes privileged composition labels or adds a stronger meta-learned neural baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reusable operator transfer without privileged routing labels
- Success threshold: Across at least five fixed seeds, routed reusable transfer must beat the best parameter-matched neural/meta baseline by at least 25% lower held-out few-shot MSE and win at least 4/5 seeds.
- Stop condition: Stop as negative if learned routing collapses, if the best neural/meta baseline matches or beats reusable transfer on at least 2/5 seeds, or if the advantage only appears when true labels are restored.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-neural-baseline-for-reusable-operator-tr-6338ce46c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
