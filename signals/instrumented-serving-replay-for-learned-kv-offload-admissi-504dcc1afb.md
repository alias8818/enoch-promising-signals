# Instrumented Serving Replay for Learned KV Offload Admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `instrumented-serving-replay-for-learned-kv-offload-admissi-504dcc1afb`
Run ID: `instrumented-serving-replay-for-learned-kv-offload-admissi-504dcc1afb-20260519T040704765162+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Instrumented Serving Replay for Learned KV Offload Admission: internal_generated:instrumented-serving-replay-for-learned-kv-offload-admissi-504dcc1afb

## What looked useful

Learned admission cut aggregate offload traffic by 1.23% versus LRU and 5.52% versus a heuristic, with a 0.20% offload gap to oracle; paired 64-condition learned-vs-LRU offload delta averaged -1.58%. Mean latency improved only 0.005% versus LRU and deadline miss rate stayed 0 for all policies.

## Boundaries and scale limits

Synthetic/instrumented replay only; no production inference server, real traces, real kernel timing, paged-attention scheduler, or measured GPU/CPU/UMA transfer calibration. The full validation was bounded locally and completed quickly because replay is event-based.

## Claim scope

In a deterministic synthetic event replay with 2.88M requests across 16 seeds and four memory-pressure workloads, a learned KV offload admission score reduced offload MB-token traffic versus LRU and heuristic baselines and remained close to an oracle, but latency gains were negligible.

## Why it stopped

No-paper useful signal: mechanism support is present for offload traffic and oracle proximity, but direct user-facing latency improvement is negligible and evidence remains synthetic/instrumented.

## Recommended next action

Run a bounded real-serving replay or vLLM/TGI integration with measured transfer penalties and real prompt/generation traces; stop treating this synthetic replay as paper-ready because the latency effect is too small.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Serving Calibration for Learned KV Offload Admission
- Success threshold: At least 5% p95 latency reduction or at least 5% offload traffic reduction versus LRU on real-serving-calibrated traces, with no increase in deadline/SLA miss rate and oracle gap below 10%.
- Stop condition: Stop as negative if learned admission fails to beat LRU by 5% on either p95 latency or offload traffic, or if gains disappear under real measured transfer costs.

## Evidence references

- Artifact root: `<local-path>/projects/instrumented-serving-replay-for-learned-kv-offload-admissi-504dcc1afb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
