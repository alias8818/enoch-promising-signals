# 2-bit KV Cache with FP16 Residual Recent-Token Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-fp16-residual-recent-token-channel-04d66b5d83f8`
Run ID: `2-bit-kv-cache-with-fp16-residual-recent-token-channel-04d66b5d83f8-20260602T135544999121+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42f8898fb57d

## What looked useful

Across four medium seeds, R=64 achieved recent-local relative MSE 0.00268 with output cosine 0.99929 and 5.48x theoretical cache compression, but old-local relative MSE stayed 0.227 and iid relative MSE 0.527. Naive 2-bit dequant+attention averaged about 2.33x FP16 attention latency.

## Boundaries and scale limits

No real language-model perplexity, generation-quality, production-serving, long-context batch, or fused packed-kernel validation was run. Tensor shapes were small/medium synthetic probes: up to seq_len=2048, heads=8, head_dim=64, queries=256, four seeds.

## Claim scope

Synthetic seq_len=2048 GPU attention probes show that a 2-bit historical KV cache with an exact FP16 recent-token channel preserves outputs for recent-local queries, but not for old-token or diffuse queries; naive dequantize-then-attend is slower than FP16 attention.

## Why it stopped

Bounded synthetic evidence is mixed: the FP16 residual channel validates the recency-local mechanism but fails to make 2-bit historical KV generally faithful, and the naive decode path is slower than FP16.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is real GPT-2-small-class decode perplexity plus attention-mass tracing before investing in a fused 2-bit kernel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model residual-window KV quantization trace and perplexity probe
- Success threshold: At R<=64, perplexity degradation is <=5% versus FP16 KV, attention mass inside the residual window is >=80% for the tested decode workload, and memory compression remains >=5x before kernel-fusion work is considered.
- Stop condition: Stop if R<=64 exceeds 5% perplexity degradation or measured attention mass inside the residual window is below 80%, because the synthetic mechanism would not transfer to real decoding.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-fp16-residual-recent-token-channel-04d66b5d83f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
