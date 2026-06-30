# Canary Shortcut Gradient Audits in a Small Sequence Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `canary-shortcut-gradient-audits-in-a-small-sequence-model-4da8da3b18`
Run ID: `canary-shortcut-gradient-audits-in-a-small-sequence-model-4da8da3b18-20260523T082952736902+0000`

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

- Parent run decision: Hidden Gradient Puzzle Audits in a Real Training Loop: enoch://control-plane/projects/hidden-gradient-puzzle-audits-in-a-real-training-loop-e0239f0774/runs/hidden-gradient-puzzle-audits-in-a-real-training-loop-e0239f0774-20260523T082006197588+0000
- Parent run decision: Gradient Puzzle Proofs for Volunteer Training Nodes: enoch://control-plane/projects/gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1/runs/gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1-20260523T073915707656+0000

## What looked useful

Early-phase XOR shortcut models reached 0.9720 mean in-distribution accuracy but 0.5269 clean accuracy, 0.0000 counterfactual accuracy, and 0.9729 counterfactual flip rate. The same-epoch clean baseline reached 1.0000 clean accuracy and 0.0098 flip rate. Gradient audit metrics separated the shortcut from the clean baseline: canary rank-1 saliency 0.5824 vs 0.0312, canary gradient share 0.0784 vs 0.0522, and canary-to-semantic saliency ratio 1.2646 vs 0.4962. Longer/easier sweeps showed the signal disappears once models learn the semantic rule.

## Boundaries and scale limits

Validated only on synthetic count/XOR sequence tasks with 5 fixed seeds, 4096 training examples, 2048 test examples, and a small Transformer classifier; not validated on language-model-scale training, naturalistic canaries, or multiple attribution methods.

## Claim scope

In a synthetic 70k-parameter Transformer sequence classifier with a fixed-position planted canary, input-gradient saliency distinguishes active shortcut reliance from a clean semantic baseline during the shortcut-dominated early training phase.

## Why it stopped

Tier 2 local evidence supports active-shortcut detection but also shows the audit is not a persistent signature of canary exposure after semantic learning, so the result is useful but not paper-ready.

## Recommended next action

Stop as no-paper useful signal; a bounded next study should test checkpoint time courses and attribution-method agreement on larger but still local sequence models before any paper attempt.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpoint Time-Course Canary Shortcut Attribution Agreement
- Success threshold: For shortcut models, attribution canary score should correlate with counterfactual flip rate at r >= 0.8 across checkpoints and exceed clean-baseline attribution by at least 2x during epochs where flip rate >= 0.8; all three attribution methods must agree on the sign of the effect.
- Stop condition: Stop if attribution scores fail to track flip rate in at least 4 of 5 seeds or if clean baselines show comparable canary attribution despite low flip rates.

## Evidence references

- Artifact root: `<local-path>/projects/canary-shortcut-gradient-audits-in-a-small-sequence-model-4da8da3b18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
