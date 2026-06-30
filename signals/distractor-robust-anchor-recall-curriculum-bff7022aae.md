# Distractor-Robust Anchor-Recall Curriculum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distractor-robust-anchor-recall-curriculum-bff7022aae`
Run ID: `distractor-robust-anchor-recall-curriculum-bff7022aae-20260620T234624550232+0000`

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

- Parent run decision: Anchor-Recall Curriculum for Tiny Long-Context Pretraining: enoch://control-plane/projects/anchor-recall-curriculum-for-tiny-long-context-pretraining-0d6ae25e5899/runs/anchor-recall-curriculum-for-tiny-long-context-pretraining-0d6ae25e5899-20260620T232608259455+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8637e62a1db0

## What looked useful

Curriculum and hard-only training both solved the trained hard length around 80 distractors, but curriculum retained high accuracy on longer spans while hard-only collapsed. Main run len112 accuracy was 0.9587 for curriculum vs 0.1624 for hard. Confirmatory sweep showed curriculum-hard deltas of +0.8535 at len96, +0.6530 at len112, and +0.7471 at len128.

## Boundaries and scale limits

Synthetic task only; 3 seeds per run; short local GB10 training; compact Transformer encoder; no GPT-2-small-class baseline, no natural-language corpus, no long-run convergence study, and no isolation of query-position generalization from distractor robustness.

## Claim scope

In a small synthetic anchor-recall sequence-classification task with a compact 2-layer Transformer encoder, a staged distractor curriculum improved longer-span recall generalization versus a matched hard-only baseline at equal optimizer steps.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal, but evidence remains synthetic, small-scale, and mechanistically ambiguous rather than paper-positive.

## Recommended next action

Run a bounded deepen test that separates distractor robustness from query-position generalization using mixed-length hard baselines, randomized query positions/padding, and equal length exposure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Disentangle distractor curriculum effects from query-position generalization
- Success threshold: Curriculum beats mixed-length hard baseline by at least 10 percentage points mean accuracy on out-of-support lengths while matching in-support accuracy, with no seed collapsing below the baseline mean.
- Stop condition: Stop if the curriculum advantage drops below 5 percentage points after mixed-length/query-position controls or if both methods solve/fail all controlled evaluations indistinguishably.

## Evidence references

- Artifact root: `<local-path>/projects/distractor-robust-anchor-recall-curriculum-bff7022aae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
