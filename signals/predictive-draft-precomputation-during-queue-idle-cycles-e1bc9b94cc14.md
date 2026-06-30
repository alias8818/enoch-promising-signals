# Predictive draft precomputation during queue idle cycles

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-draft-precomputation-during-queue-idle-cycles-e1bc9b94cc14`
Run ID: `predictive-draft-precomputation-during-queue-idle-cycles-e1bc9b94cc14-20260611T182901903155+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ecacc591180f

## What looked useful

Idle-cycle draft precompute is a plausible latency optimization when spare capacity exists, with best synthetic condition showing -83.05% mean p95 latency and -78.37% target steps. However, 6 of 20 conditions increased target steps, especially at 40 rps where target steps rose +11.39% to +29.97% while p95 latency still improved.

## Boundaries and scale limits

Synthetic 30-second traces, 15 seeds per condition, 5 arrival rates, 4 fixed draft acceptance probabilities, no real target/draft model, no measured GPU overlap, no KV-cache or memory-bandwidth contention, no production traces.

## Claim scope

In a dependency-free synthetic discrete-event LLM decode-queue simulator, spending underfilled-batch idle budget on speculative draft tokens reduces p95 latency across tested load and acceptance settings, but does not reliably reduce target decode steps under saturated load.

## Why it stopped

Synthetic proxy evidence supports a mechanism but reveals mixed efficiency tradeoffs; it is not direct or production-grade evidence for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement a bounded real serving microbenchmark that measures whether the latency-throughput tradeoff survives with actual target and draft models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real serving microbenchmark for idle-cycle draft precompute
- Success threshold: At least 20% p95 latency reduction with no more than 5% increase in target GPU time or decode steps across two moderate-load trace settings.
- Stop condition: Stop if real-serving overhead or contention removes p95 latency gains, or if target GPU time/decode steps increase by more than 5% in moderate-load settings.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-draft-precomputation-during-queue-idle-cycles-e1bc9b94cc14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
