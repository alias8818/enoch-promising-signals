# Real-model KV cache test for exact position anchored lossy compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-kv-cache-test-for-exact-position-anchored-lossy-d748c0ccd0`
Run ID: `real-model-kv-cache-test-for-exact-position-anchored-lossy-d748c0ccd0-20260526T194521231090+0000`

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

- Parent run decision: Lossy State Compression with Exact Position Anchors: enoch://control-plane/projects/lossy-state-compression-with-exact-position-anchors-19db28626e33/runs/lossy-state-compression-with-exact-position-anchors-19db28626e33-20260525T095402178368+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3646626a8185

## What looked useful

Anchored 4-bit KV compression had low degradation versus exact (delta NLL 0.0152, mean KL 0.0115) and better KL/top-1 preservation than no-anchor 4-bit, while 2-bit and zeroed lossy caches degraded strongly. The practical NLL advantage over no-anchor 4-bit was only 0.0104, below the 0.02 threshold.

## Boundaries and scale limits

Single 124M-parameter GPT-2 model, six built-in natural-text windows, 96-token context, 24-token continuation, no standard benchmark corpus, no long-context retrieval task, no production cache memory/latency implementation, no larger modern model.

## Claim scope

Small direct GPT-2 inference test: preserving exact stride-16 KV anchor positions plus a 32-token recent exact window while 4-bit quantizing other cached positions kept continuation behavior close to exact on six 96-token-context rolling text windows, but did not meet the pre-registered NLL advantage threshold over a recent-window-only 4-bit control.

## Why it stopped

Tier 1 direct test produced a mixed useful signal but failed the pre-registered anchored-vs-no-anchor NLL advantage threshold; this is mechanism support, not paper-positive validation.

## Recommended next action

Run a bounded deepen test on a standard corpus with longer contexts and retrieval-sensitive slices, using the same exact-anchor intervention and a recent-window-only quantized control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer-context standard-corpus test of exact KV anchors versus recent-window quantized KV
- Success threshold: Anchored 4-bit cache beats no-anchor 4-bit by at least 0.02 NLL or equivalent task metric, keeps mean KL versus exact below 0.02, and documents actual KV memory savings.
- Stop condition: Stop if anchored 4-bit fails to beat no-anchor 4-bit by 0.02 on aggregate NLL/task metric or if KL exceeds 0.02 after reasonable stride/recent-window calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-kv-cache-test-for-exact-position-anchored-lossy-d748c0ccd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
