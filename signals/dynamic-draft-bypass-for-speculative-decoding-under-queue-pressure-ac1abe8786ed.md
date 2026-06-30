# Dynamic Draft Bypass for Speculative Decoding under Queue Pressure

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamic-draft-bypass-for-speculative-decoding-under-queue-pressure-ac1abe8786ed`
Run ID: `dynamic-draft-bypass-for-speculative-decoding-under-queue-pressure-ac1abe8786ed-20260528T174203241471+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aad2e044b1df

## What looked useful

Queue length alone was not a reliable control signal. The dynamic threshold policy produced 0/36 >2% p95 wins versus the best static baseline in the bounded sweep, harmed 10/36 scenarios by >2%, and had a worst p95 regression of 33.08%.

## Boundaries and scale limits

Synthetic proxy only: no real model pair, GPU batching, KV-cache pressure, production scheduler, or measured draft-target acceptance traces. The largest completed sweep used 36 scenarios, 3 seeds, and 160 requests per scenario.

## Claim scope

In a deterministic single-worker discrete-event proxy sweeping arrival pressure, draft cost, and acceptance rate, a simple ready-queue threshold for bypassing speculative decoding did not robustly improve p95 latency over the better static always-spec or never-spec policy.

## Why it stopped

Proxy early falsification: the simple dynamic threshold did not clear a >2% p95 improvement threshold in any bounded-sweep scenario and sometimes reduced throughput, so this is not full validation and not paper-ready.

## Recommended next action

Stop this simple-threshold line as a paper candidate; a next local test should only proceed if it replaces queue length with acceptance-aware and utilization-aware control in a real serving harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance- and utilization-aware speculative bypass in a real serving harness
- Success threshold: At least 5% p95 latency improvement over the best static baseline with no more than 2% throughput loss in two independent load regimes.
- Stop condition: Stop if dynamic policy fails to beat the best static baseline by 5% p95 latency in a smoke and medium run, or if telemetry shows queue length and acceptance/utilization signals are too noisy for stable control.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-draft-bypass-for-speculative-decoding-under-queue-pressure-ac1abe8786ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
