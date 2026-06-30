# Home-Distributed Agent Inference with Shared Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-distributed-agent-inference-with-shared-ledger-2c92746951f1`
Run ID: `home-distributed-agent-inference-with-shared-ledger-2c92746951f1-20260613T150459453802+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d76f7b50682f

## What looked useful

Per-token synchronous ledger commits added about 5.9 s blocking time per 80-token step, inflated p95 latency by 6-44x across tested loads, and cut throughput to 33-52% of baseline at moderate/high arrivals. Per-step sync added about 74 ms per step and was tolerable until near capacity. Async/batched ledger accounting stayed effectively off the critical path in this proxy.

## Boundaries and scale limits

No real multi-host home deployment, no real LLM inference kernels, no real consensus protocol, no adversarial validation, no payment settlement, and no privacy/security measurement. Results are not publication-grade full-system validation.

## Claim scope

CPU-only local proxy: SQLite WAL durable append benchmark plus event-loop simulation of six home devices under modeled home/WAN ledger RTTs. Supports rejecting synchronous per-token ledger commits in the inference hot path and retaining asynchronous/batched ledger accounting as the only plausible variant tested.

## Why it stopped

Proxy early falsification of the synchronous per-token shared-ledger design; not a full validation of home-distributed inference.

## Recommended next action

Stop this run as a no-paper useful signal; next build a two-or-more-host prototype that compares no ledger, per-step sync ledger, and asynchronous batched ledger using actual agent tasks and measured network RTT.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-host prototype for asynchronous ledger accounting in agent inference
- Success threshold: Async/batched ledger keeps p95 task latency within 1.2x no-ledger baseline and throughput at or above 90% of baseline while preserving durable replay after restart.
- Stop condition: Stop if async/batched ledger falls below 80% baseline throughput or exceeds 2x p95 latency in two independent runs after eliminating implementation bugs.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-agent-inference-with-shared-ledger-2c92746951f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
