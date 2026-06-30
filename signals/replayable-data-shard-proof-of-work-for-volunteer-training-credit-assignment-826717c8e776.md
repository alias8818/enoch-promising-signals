# Replayable data-shard proof of work for volunteer training credit assignment

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `replayable-data-shard-proof-of-work-for-volunteer-training-credit-assignment-826717c8e776`
Run ID: `replayable-data-shard-proof-of-work-for-volunteer-training-credit-assignment-826717c8e776-20260619T100825704388+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d7f05af6eeb

## What looked useful

Sampled replay audits detected omitted transition work at rates matching hypergeometric theory while costing far less than full replay on honest traces; for example k=32 cost 0.0145x worker time and detected 9.77% skipped transitions in 96% of trials, while k=512 cost 0.226x and detected 0.59% skipped transitions in 99% of trials. Full replay cost 0.897x worker time, so exact verification is not cheaper than redoing the work.

## Boundaries and scale limits

No real volunteer network, no secure identity or challenge transport, no GPU or cross-machine deterministic neural training, no large model, no real dataset, no adaptive adversary beyond pre-challenge omitted transitions. Full replay remains worker-equivalent and all-state reveal storage grows linearly with model size and step count.

## Claim scope

Bounded CPU-only synthetic experiment: deterministic logistic-regression shard with 2,048 SGD transitions, SHA-256 transition commitments, randomized post-commit sampled replay audits, and omitted-transition adversaries.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal but not direct/full validation of volunteer training-credit assignment.

## Recommended next action

Run a bounded deterministic small neural-model follow-up that measures cross-run replay stability, checkpoint/state-reveal storage, and adaptive omitted-work detection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic neural shard replay with checkpointed audit state reveals
- Success threshold: At least 95% detection of 10% omitted transitions with verifier compute below 10% of worker compute, replay mismatch rate of zero across repeated deterministic runs, and checkpoint storage at least 10x smaller than all-state storage.
- Stop condition: Stop if deterministic replay cannot be made stable for the chosen small neural model, or if checkpointed audits exceed 25% of worker compute for 95% detection of 10% omitted transitions.

## Evidence references

- Artifact root: `<local-path>/projects/replayable-data-shard-proof-of-work-for-volunteer-training-credit-assignment-826717c8e776`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
