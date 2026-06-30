# Adaptive Draft Length in Speculative Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-draft-length-in-speculative-cascade-f4e3fbc6c166`
Run ID: `adaptive-draft-length-in-speculative-cascade-f4e3fbc6c166-20260628T183747577723+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/325fe8d4803e

## What looked useful

Adaptive draft length produced +5.3% to +8.3% paired throughput gains versus the best fixed K in four nonstationary synthetic scenarios, but lost -1.8% to -5.2% in three stationary scenarios and reached only 86.6% of oracle throughput under rapid shifts.

## Boundaries and scale limits

No real LLM, GPU kernel, corpus trace, serving latency, batching, KV-cache, or quality evidence was produced. Results should be treated as a scheduler mechanism signal only.

## Claim scope

Synthetic speculative-decoding scheduler simulation with K=1..16, 7 acceptance scenarios, 80 seeds, and a simple draft/verifier cost model. Adaptive EWMA draft length improves throughput over the best fixed-K baseline on nonstationary synthetic acceptance traces but loses on stationary traces.

## Why it stopped

No-paper useful signal: the result is synthetic/proxy evidence, not direct serving or model evidence; it supports a bounded follow-up rather than a publication claim.

## Recommended next action

Run a bounded real-trace replay with a small draft/verifier model pair, measured latency, tuned fixed-K controls, oracle bound, and a stationarity gate or fixed-K fallback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of adaptive speculative draft length with stationarity fallback
- Success threshold: Adaptive-with-fallback beats tuned fixed K by at least 4% on nonstationary held-out traces with 95% CI above zero and loses less than 1% on stationary held-out traces.
- Stop condition: Stop if adaptive-with-fallback fails to beat tuned fixed K on real nonstationary traces or if stationary regression remains at or above 1%.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-draft-length-in-speculative-cascade-f4e3fbc6c166`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
