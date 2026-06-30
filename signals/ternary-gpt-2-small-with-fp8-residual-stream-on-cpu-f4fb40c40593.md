# Ternary GPT-2-small with FP8 residual stream on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-gpt-2-small-with-fp8-residual-stream-on-cpu-f4fb40c40593`
Run ID: `ternary-gpt-2-small-with-fp8-residual-stream-on-cpu-f4fb40c40593-20260619T164957840951+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/38572eb15e20

## What looked useful

Ternary storage was 4x smaller as int8+scale and about 15.7x smaller with ideal 2-bit packing, and FP8 residual quantization had relative MSE around 7e-4 in this proxy. However, ternary dequantization was 2.68x to 3.75x slower than dense fp32 on GPT-2-small 128-token projection cases, split ternary masks were 2.18x to 2.37x slower, and FP8-input plus ternary-dequant projection was 4.42x to 10.56x slower.

## Boundaries and scale limits

Tested synthetic GPT-2-small projection shapes only, with random activations/weights, 128-token cases, 5 repeats, NumPy 2.4.6/OpenBLAS, four CPU threads, and software FP8 quantization. No trained GPT-2-small, perplexity benchmark, native FP8 arithmetic, or packed ternary CPU kernel was evaluated.

## Claim scope

On this CPU worker, ordinary NumPy/OpenBLAS-style CPU paths for GPT-2-small-shaped ternary projections plus a software FP8 E4M3 residual stream reduce storage but are slower than optimized dense fp32 GEMM; this is a local systems viability result, not a trained language-model quality result.

## Why it stopped

Proxy/local early falsification of the ordinary CPU-kernel path: storage compression is real, but the available dequantization/software-FP8 execution route is materially slower than dense fp32 and is not sufficient for a paper or practical CPU speedup claim.

## Recommended next action

Stop this no-paper run; the bounded next test is an AVX2/AVX512 packed ternary CPU projection kernel that avoids per-call dequantization and is compared against dense fp32 on the same GPT-2-small projection shapes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed ternary CPU kernel for GPT-2-small projections
- Success threshold: At least 1.25x faster median us/token than dense fp32 on two of the three GPT-2-small projection shapes with no more than 2x the FP8/ternary proxy error observed here.
- Stop condition: Stop if the packed ternary kernel is not faster than dense fp32 on at least two GPT-2-small projection shapes after basic vectorization and thread pinning, or if implementation requires non-local/private hardware.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gpt-2-small-with-fp8-residual-stream-on-cpu-f4fb40c40593`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
