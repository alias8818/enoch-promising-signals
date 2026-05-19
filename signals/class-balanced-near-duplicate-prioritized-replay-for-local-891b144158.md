# Class-balanced near-duplicate-prioritized replay for local transformer routers

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `class-balanced-near-duplicate-prioritized-replay-for-local-891b144158`
Run ID: `class-balanced-near-duplicate-prioritized-replay-for-local-891b144158-20260519T194352736588+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Natural near-duplicate replay admission across multiple local transformer routing tasks: enoch://control-plane/projects/natural-near-duplicate-replay-admission-across-multiple-lo-c9e3ba8343/runs/natural-near-duplicate-replay-admission-across-multiple-lo-c9e3ba8343-20260519T193616637630+0000
- Parent run decision: Live-memory replay admission for real small local transformer cascades: enoch://control-plane/projects/live-memory-replay-admission-for-real-small-local-transfor-85eecba84d/runs/live-memory-replay-admission-for-real-small-local-transfor-85eecba84d-20260519T191844352029+0000

## What looked useful

CB-NDPR beat no replay, FIFO, and random replay in imbalanced regimes, but the near-duplicate priority component failed the key ablation: versus class-balanced replay, CB-NDPR was worse in the hardest imbalanced-overlap condition (-0.0040 accuracy, -0.0090 minority recall, -0.0315 worst-class recall mean deltas) and only negligible/near-ceiling in easier conditions.

## Boundaries and scale limits

The validation used a lightweight hashed-feature softmax router, synthetic text-query route labels, 3 stream regimes, and 10 fixed seeds. It did not fine-tune a GPT-2/BERT-class transformer router, use production routing logs, or validate serving-system behavior. This is mechanism-level local evidence, not paper-ready transformer-scale evidence.

## Claim scope

In a reproducible NumPy online text-router benchmark with imbalanced near-duplicate query streams, replay improves minority routing quality, and class-balanced replay is the dominant mechanism. Adding near-duplicate priority to class-balanced replay did not robustly improve held-out router accuracy, minority recall, worst-class recall, or duplicate-family consistency over the class-balanced ablation.

## Why it stopped

Tier 4 paper-readiness was not met. The run produced a replicated mechanism-level benchmark with fixed seeds, direct router metrics, controls, and an ablation, but the proposed near-duplicate priority did not robustly beat the class-balanced ablation; the result remains a scoped proxy rather than full transformer-router validation.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence: retain class-balanced replay as the supported baseline/control and do not claim a near-duplicate-priority contribution without transformer-router and real-query evidence.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/class-balanced-near-duplicate-prioritized-replay-for-local-891b144158`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
