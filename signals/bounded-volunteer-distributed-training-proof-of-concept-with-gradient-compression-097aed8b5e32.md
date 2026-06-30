# Bounded volunteer distributed training proof-of-concept with gradient compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-volunteer-distributed-training-proof-of-concept-with-gradient-compression-097aed8b5e32`
Run ID: `bounded-volunteer-distributed-training-proof-of-concept-with-gradient-compression-097aed8b5e32-20260611T095824246407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

The mechanism is locally viable in simulation: q8, Top-K, and sign compression sharply reduced gradient bytes with negligible final accuracy loss under bounded client acceptance and dropout. This is useful for deciding to build a real transport/checkpoint prototype, but not enough for a paper.

## Boundaries and scale limits

Synthetic small-model evidence only. No real volunteer devices, network transport, asynchronous aggregation, adversarial clients, privacy checks, checkpoint/rejoin behavior, or GPT-2-small-class training were tested.

## Claim scope

In a local CPU simulator of bounded synchronous volunteer training on a small non-IID synthetic 10-class classification task, gradient compression preserved final accuracy within 0.18 percentage points of an uncompressed baseline while reducing transmitted gradient bytes by 75% to 98%; a harsher 65% dropout and 4-client acceptance stress run preserved the same qualitative result.

## Why it stopped

No-paper closure: this run provides simulator-only useful signal, not direct distributed volunteer training evidence or model-scale validation.

## Recommended next action

Build a localhost multi-process prototype with explicit bandwidth/latency limits and checkpoint/rejoin behavior, then compare compressed and uncompressed training on the same task with measured network bytes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Localhost transport prototype for bounded volunteer compressed training
- Success threshold: At least one compression mode must reduce measured payload bytes by 75% or more while final accuracy remains within 1 percentage point of the uncompressed control across three seeds.
- Stop condition: Stop as negative if real transport overhead erases byte savings or all compression modes lose more than 1 percentage point final accuracy versus uncompressed under the bounded volunteer schedule.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-volunteer-distributed-training-proof-of-concept-with-gradient-compression-097aed8b5e32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
