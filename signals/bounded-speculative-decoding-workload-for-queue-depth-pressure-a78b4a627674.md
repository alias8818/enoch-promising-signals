# Bounded Speculative Decoding Workload for Queue Depth Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-speculative-decoding-workload-for-queue-depth-pressure-a78b4a627674`
Run ID: `bounded-speculative-decoding-workload-for-queue-depth-pressure-a78b4a627674-20260609T170015530699+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e2a380800d3b

## What looked useful

Simple queue-depth bounding is not a robust pressure-control mechanism by itself. It can reduce draft waste and improve p95 latency near the capacity edge, but under sustained overload it can amplify backlog by giving up the throughput advantage of speculative decoding.

## Boundaries and scale limits

Synthetic CPU-only discrete-event simulation; no real LLM server, GPU timing, batching, KV-cache effects, production scheduler, or measured model acceptance trace. Confirmation used 6,000 requests across six arrival rates plus two short acceptance sensitivity sweeps.

## Claim scope

In a deterministic single-queue speculative decoding proxy with identical arrivals across policies, a naive queue-depth-aware speculative window bound only helped in a narrow near-capacity regime and was worse under sustained overload because fallback to k1 reduced service efficiency.

## Why it stopped

Proxy evidence is mixed: the default confirmation sweep missed the useful-signal criterion and showed severe overload regressions, so this is an early falsification of naive queue-depth bounding rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace k1 fallback with a throughput-preserving admission controller and evaluate it against fixed k8 under the same queue-pressure criteria.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Throughput-preserving speculative admission under queue pressure
- Success threshold: Across at least two adjacent near-saturation arrival rates, improve p95 latency by >5% and p95 queue depth by >10% versus fixed k8 while losing <5% token throughput, with no catastrophic regression at the next higher load point.
- Stop condition: Stop if all throughput-preserving bounds either fail the latency/queue criteria or lose >=5% token throughput versus fixed k8 at near-saturation load.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-speculative-decoding-workload-for-queue-depth-pressure-a78b4a627674`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
