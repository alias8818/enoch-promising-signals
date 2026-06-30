# Calibrated cascade router for local dual-model serving on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-cascade-router-for-local-dual-model-serving-on-gb10-5e03cabc66f0`
Run ID: `calibrated-cascade-router-for-local-dual-model-serving-on-gb10-5e03cabc66f0-20260609T234357744649+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfccda14a281

## What looked useful

Final proxy: cheap accuracy 0.8110, strong accuracy 0.8599. Best calibrated route reached 0.8523 accuracy with 72.68% cheap acceptance, 27.32% deferral, and 1.1847x estimated speedup vs strong-only. Cheap-model ECE improved from 0.1266 to 0.0176 after temperature scaling, but an uncalibrated threshold reached a similar 1.1916x speedup at 0.8506 accuracy.

## Boundaries and scale limits

No actual local LLMs were served; the result excludes token generation, KV-cache behavior, model residency, concurrent request queueing, real prompt distributions, and UMA pressure from larger models.

## Claim scope

On a self-contained CUDA synthetic classification serving proxy on GB10, a cheap/strong cascade router achieved near-strong accuracy with lower estimated per-request inference cost; temperature calibration improved cheap-model probability quality but did not clearly outperform an uncalibrated threshold control.

## Why it stopped

Closed as a bounded proxy useful signal: the mechanism worked in synthetic CUDA inference, but evidence is not direct local LLM serving and calibration was not clearly better than uncalibrated threshold routing.

## Recommended next action

Run the same calibrated-vs-uncalibrated routing protocol with two actual resident local language models or instruction classifiers on GB10, measuring end-to-end latency, throughput, memory pressure, and queueing under concurrent requests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local dual-model serving calibration test on GB10
- Success threshold: Calibrated router is within 1 percentage point of strong-only quality, improves p50 latency or throughput by at least 15% versus strong-only, and improves the speed/quality frontier versus uncalibrated confidence routing on the same workload.
- Stop condition: Stop if strong-only cannot be made a valid stronger baseline, if calibrated routing does not beat uncalibrated routing at matched quality, or if cascade overhead eliminates the latency/throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-cascade-router-for-local-dual-model-serving-on-gb10-5e03cabc66f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
