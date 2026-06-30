# Int4-to-Int8 Difficulty Router on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-to-int8-difficulty-router-on-cpu-bc7267ca2416`
Run ID: `int4-to-int8-difficulty-router-on-cpu-bc7267ca2416-20260524T193243464748+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/776b47d08011

## What looked useful

Across five seeds, all-int4 accuracy averaged 0.664766, all-int8 averaged 0.690200, and the best router averaged 0.690400 accuracy while routing 0.698900 of examples on average. The mechanism signal is present, but the required route fraction implies a mean break-even int4 speedup around 4.17x under the simple cost model.

## Boundaries and scale limits

No real LLM, real activations, packed int4 CPU kernel, batched serving scheduler, or end-to-end latency validation was tested. Results are limited to small synthetic linear workloads with dependency-free C++ loops.

## Claim scope

On a deterministic synthetic multiclass linear CPU workload, int4 confidence-margin routing can recover essentially all int8 accuracy, but only by routing a high fraction of examples.

## Why it stopped

Bounded synthetic evidence supports the difficulty-routing mechanism but does not support a paper-ready CPU speed/quality claim; the result is a proxy, not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; only deepen if a follow-up directly measures packed int4 and int8 CPU kernels against the observed route-fraction break-even.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed CPU Kernel Break-Even Test for Int4-to-Int8 Routing
- Success threshold: At matched all-int8 accuracy within 0.1 percentage points, routed serving latency is at least 10% lower than all-int8 on a representative CPU workload, with route fraction below the measured break-even threshold in at least 3 seeds or traces.
- Stop condition: Stop if the measured int4 kernel is not at least 3x faster than int8 end-to-end, or if real activation route fractions exceed the measured break-even threshold at matched accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/int4-to-int8-difficulty-router-on-cpu-bc7267ca2416`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
