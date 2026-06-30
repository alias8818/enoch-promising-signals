# Token-level learned router for GPT-2-small quantization cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-level-learned-router-for-gpt-2-small-quantization-ca-14c9031b65`
Run ID: `token-level-learned-router-for-gpt-2-small-quantization-ca-14c9031b65-20260628T191825455255+0000`

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

- Parent run decision: Quantization Cascade with Learned Router: enoch://control-plane/projects/quantization-cascade-with-learned-router-91a8632779b8/runs/quantization-cascade-with-learned-router-91a8632779b8-20260628T185815387004+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/325fe8d4803e

## What looked useful

8-bit fake quantization alone increased mean NLL by 0.1832 versus full precision. A learned router at 25%, 50%, and 75% full-precision token budgets reduced the deltas to 0.1237, 0.0652, and 0.0296 and improved top-1 match from 0.7505 to 0.8612, 0.9371, and 0.9886. However, high-entropy routing was slightly better on NLL at the same budgets, so the learned-router claim is not supported as tested.

## Boundaries and scale limits

Evaluated 20,320 train token positions and 8,128 eval token positions with fake dequantized weights, not a real int8/int4 serving backend; no fused mixed-precision kernels, no autoregressive latency benchmark, and only one dataset/model seed. 4-bit evidence is smoke-only early falsification for this simple quantizer.

## Claim scope

On a bounded GPT-2-small/WikiText-2 offline proxy, token-level fallback from 8-bit fake weight quantization to full precision reduces NLL degradation and improves top-1 agreement versus random routing, but the tested learned logistic router does not beat a simple high-entropy routing heuristic.

## Why it stopped

Bounded proxy evidence found useful token-level fallback behavior, but the learned router failed to beat the simple entropy baseline and the setup did not measure real serving speedup.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should test a stronger learned router against entropy and margin controls with real quantization/timing before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Beat entropy with a stronger token router under real GPT-2 quantized serving constraints
- Success threshold: At 25% and 50% full-precision token budgets, the learned router reduces mean NLL delta by at least 10% relative to high-entropy routing while retaining a measurable serving-speed or memory benefit versus full precision.
- Stop condition: Stop if entropy remains equal or better on NLL recovery at matched budgets, or if real serving overhead removes the expected efficiency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-learned-router-for-gpt-2-small-quantization-ca-14c9031b65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
