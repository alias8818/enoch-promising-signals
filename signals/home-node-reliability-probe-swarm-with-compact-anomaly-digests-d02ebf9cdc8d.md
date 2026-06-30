# Home-Node Reliability Probe Swarm With Compact Anomaly Digests

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-node-reliability-probe-swarm-with-compact-anomaly-digests-d02ebf9cdc8d`
Run ID: `home-node-reliability-probe-swarm-with-compact-anomaly-digests-d02ebf9cdc8d-20260609T051420886016+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3ea99510e448

## What looked useful

The compact consensus digest produced mean recall 0.625, precision 0.761, F1 0.684, median detection latency 3.17 ticks, p90 latency 18.88 ticks, and 0.0135 bytes-vs-raw ratio. Baselines at the same threshold were central raw threshold F1 0.503 and single-probe F1 0.456. Lower thresholds recovered more faults but reduced precision.

## Boundaries and scale limits

Synthetic telemetry only; no real home-lab traces, hardware probe overhead, network transport, probe crash/restart behavior, clock skew, persistent storage, or operator triage study. This does not validate real-world home-node reliability monitoring.

## Claim scope

In a deterministic synthetic home-node telemetry simulator with 80 nodes, 720 ticks, 12 seeds, and 833 injected CPU/memory/disk/network/thermal faults, a 3-probe/3-vote compact anomaly digest reduced transmitted bytes to 1.35% of raw probe telemetry while improving precision and F1 over naive raw-threshold and single-probe baselines at the same threshold.

## Why it stopped

Synthetic/proxy evidence supports a compact triage mechanism but does not provide direct real-world validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up on real or replayed home-node telemetry with labeled incidents and measured probe overhead; stop this synthetic-only run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Compact Probe Digests on Labeled Home-Node Telemetry
- Success threshold: Mean precision >= 0.70, recall >= 0.60, F1 >= 0.65, digest bytes <= 5% of raw telemetry, and probe overhead <= 2% CPU with no missed critical incident class.
- Stop condition: Stop as negative if real/replayed precision falls below 0.55, recall falls below 0.50, digest bytes exceed 10% of raw telemetry, or probe overhead materially disrupts low-power nodes.

## Evidence references

- Artifact root: `<local-path>/projects/home-node-reliability-probe-swarm-with-compact-anomaly-digests-d02ebf9cdc8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
