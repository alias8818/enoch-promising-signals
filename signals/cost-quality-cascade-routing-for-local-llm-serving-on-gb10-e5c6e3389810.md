# Cost-quality cascade routing for local LLM serving on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cost-quality-cascade-routing-for-local-llm-serving-on-gb10-e5c6e3389810`
Run ID: `cost-quality-cascade-routing-for-local-llm-serving-on-gb10-e5c6e3389810-20260613T111159778900+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d25e02f83924

## What looked useful

The cheap 0.5B tier had 0.0% accuracy and required 97.5% escalation to approach 1.5B quality, making the cascade slower than direct 1.5B serving. The 1.5B-to-3B cascade also had zero thresholds that matched or beat direct 3B on both accuracy and latency; matching 3B accuracy on the test split required about 67.5% escalation and 0.355s mean latency versus 0.217s for direct 3B.

## Boundaries and scale limits

Single-request local generation only; no HTTP serving stack, batching, concurrency, KV-cache reuse, diverse workload mix, trained router, quantized runtime, or 7B+ model tier was tested.

## Claim scope

On 60 GSM8K examples per tier pair using local CUDA-backed Transformers generation on GB10, sequential cascades from Qwen2.5 0.5B to 1.5B and from 1.5B to 3B using cheap-model mean generated-token log probability did not achieve a better accuracy-latency tradeoff than direct larger-model serving.

## Why it stopped

Moderate early falsification: in the direct local GB10 proxy benchmark, no tested confidence threshold improved both quality and latency over direct larger-model serving, and the production-serving aspects not tested would be required for broader validation.

## Recommended next action

Stop this simple sequential logprob-router line as no-paper evidence; a bounded follow-up should test a non-generative or trained router whose overhead is small enough to make escalation economically plausible.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-generative router for GB10 local LLM cascade serving
- Success threshold: Achieve at least 95% of direct larger-model accuracy with at least 25% lower mean latency or generated-token cost, including router overhead.
- Stop condition: Stop if router overhead exceeds 20% of direct larger-model latency or if calibration cannot produce any threshold that beats direct larger-model serving on both quality and cost.

## Evidence references

- Artifact root: `<local-path>/projects/cost-quality-cascade-routing-for-local-llm-serving-on-gb10-e5c6e3389810`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
