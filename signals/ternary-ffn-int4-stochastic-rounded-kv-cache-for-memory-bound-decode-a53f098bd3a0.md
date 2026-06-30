# Ternary FFN + INT4 stochastic-rounded KV cache for memory-bound decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-ffn-int4-stochastic-rounded-kv-cache-for-memory-bound-decode-a53f098bd3a0`
Run ID: `ternary-ffn-int4-stochastic-rounded-kv-cache-for-memory-bound-decode-a53f098bd3a0-20260629T031941947223+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3da86e28ed9

## What looked useful

At d_model=1024, d_ff=4096, seq_len=4096, storage fell to 37.5% of fp16 baseline but combined latency regressed 4.67x; INT4 attention alone regressed 4.91x and ternary FFN regressed 2.88x. At seq_len=16384, storage fell to 30.0% but combined latency regressed 7.13x and INT4 attention regressed 7.91x. Attention relative L2 error was about 0.31-0.33 and FFN relative L2 error about 0.59.

## Boundaries and scale limits

Not a trained model, not end-to-end perplexity/generation, not a fused CUDA/Triton kernel, not a GPT-2-small-class baseline, and not a production serving benchmark.

## Claim scope

Bounded synthetic GB10 CUDA decode proxy for one-layer batch-1 decode using unfused PyTorch dequantization: packed INT4 stochastic-rounded K/V cache plus ternary FFN reduces explicit storage but is slower and has large output error versus dense fp16.

## Why it stopped

Proxy early falsification rather than full validation: the storage mechanism works, but the tested unfused implementation is slower than fp16 and too inaccurate on synthetic layer outputs.

## Recommended next action

Stop this naive unfused path; only revisit with a fused packed-INT4 attention kernel and fused ternary FFN kernel plus real-model calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed-INT4 KV attention decode microkernel on GB10
- Success threshold: At least 1.25x faster attention latency than fp16 baseline at seq_len >= 16384 with attention relative L2 <= 0.10 and no fp16 K/V materialization in the timed path.
- Stop condition: Stop if fused INT4 attention is not faster than fp16 by seq_len 16384 or if relative L2 remains above 0.10 after groupwise scaling/calibration.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-ffn-int4-stochastic-rounded-kv-cache-for-memory-bound-decode-a53f098bd3a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
