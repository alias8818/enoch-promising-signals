# Adaptive Cascade Router on Single GB10 Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-cascade-router-on-single-gb10-local-serving-9121d7c6ccb0`
Run ID: `adaptive-cascade-router-on-single-gb10-local-serving-9121d7c6ccb0-20260621T032853176523+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/60b7c27a2283

## What looked useful

The cascade mechanism is locally plausible on GB10 when confidence is predictive and the fallback is stronger: threshold 0.7 used fallback for about 38% of requests, averaged 0.75275 accuracy versus 0.7500 for always-large, and reduced mean latency from 0.09559 ms to 0.06316 ms. This is no-paper evidence because it is a synthetic proxy.

## Boundaries and scale limits

Synthetic classifier workload only; no real LLM backends, token generation, KV-cache behavior, prompt quality scoring, concurrency, or long-run memory-pressure validation. One invalid fallback-control run showed routing can hurt when the fallback model is not better on the routed tail.

## Claim scope

On a synthetic batch-1 GPU serving proxy on one NVIDIA GB10, a confidence-threshold cascade with a trained fallback control reduced mean request latency by about 34% versus always-large while matching or slightly exceeding always-large synthetic classification accuracy across four seeds.

## Why it stopped

Finalized as no-paper useful signal: the run produced synthetic/proxy support for the mechanism but not direct real-LLM local-serving validation.

## Recommended next action

Run a bounded real-LLM GB10 follow-up with two local models, prompt-level quality scoring, TTFT/tokens/sec, fallback rate, and memory telemetry; stop paper consideration until that direct evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Cascade Serving on Single GB10
- Success threshold: Cascade achieves at least 20% lower mean TTFT or at least 20% higher effective tokens/sec than always-large while quality is no more than 1 percentage point below always-large and memory remains stable without earlyoom pressure.
- Stop condition: Stop if the small-model confidence is not predictive of quality, if fallback rate above 70% is required to match always-large quality, if cascade overhead erases at least 80% of the latency gain, or if GB10 memory pressure prevents stable local serving.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-router-on-single-gb10-local-serving-9121d7c6ccb0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
