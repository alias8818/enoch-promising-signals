# Cascade Routing for Multi-Step Local Agent Tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cascade-routing-for-multi-step-local-agent-tasks-02e08e97b4cb`
Run ID: `cascade-routing-for-multi-step-local-agent-tasks-02e08e97b4cb-20260613T090250174546+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/22a04b86cca6

## What looked useful

Confidence-based cascade routing did not meet the target of at least 95% static-large task success with at least 30% cost savings. Preserving task success routed almost every step to the large worker, while retry cascades were substantially more expensive than static-large routing.

## Boundaries and scale limits

No real LLMs, local model latencies, tool-call traces, or production workloads were tested; confidence and worker outcomes were simulated.

## Claim scope

Synthetic multi-step local-agent proxy with 3-10 dependent steps, three cost/quality worker tiers, noisy confidence, fixed cascade policies, and a 90-point threshold sweep at moderate confidence noise.

## Why it stopped

Proxy early falsification: fixed cascades and tuned threshold routing failed the 95% success-retention plus 30% cost-saving target under the synthetic multi-step dependency model.

## Recommended next action

Stop this proxy run; a direct follow-up should replay real local-agent task traces and measure whether calibrated routing can beat static-large latency or compute cost at fixed task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Cascade Routing for Real Local Agent Tasks
- Success threshold: At least 95% task-success retention versus static strongest local worker and at least 30% measured mean latency or compute-cost savings on held-out traces.
- Stop condition: Stop as negative if no calibrated router on held-out traces reaches 95% task-success retention with at least 20% savings, or if trace collection lacks task-level success labels.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-routing-for-multi-step-local-agent-tasks-02e08e97b4cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
