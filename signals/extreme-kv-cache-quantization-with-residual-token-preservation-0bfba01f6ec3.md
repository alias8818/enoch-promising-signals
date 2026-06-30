# Extreme KV Cache Quantization with Residual Token Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-kv-cache-quantization-with-residual-token-preservation-0bfba01f6ec3`
Run ID: `extreme-kv-cache-quantization-with-residual-token-preservation-0bfba01f6ec3-20260621T235852525999+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

2-bit quantization without residual preservation had high mean relative output L2 in recent_local and mixed scenarios (0.6997 and 0.7647). A <=64-token residual window reduced those errors to 0.0234 and 0.0261 while retaining 4.27x estimated fp16-cache compression. The old_needle control stayed at about 0.7260 relative output L2 for residual windows through 128 tokens, showing recency-only preservation does not protect old salient dependencies.

## Boundaries and scale limits

Evidence is synthetic and CPU-only. It does not measure real model perplexity, generation quality, packed-kernel latency, production memory overhead, or robustness across model families and real long-context corpora.

## Claim scope

In a deterministic synthetic multi-head attention proxy, preserving a recent full-precision residual KV window can make 2-bit per-token KV quantization low-error when the salient tokens are recent or mixed-recent, while retaining about 4.27x estimated cache compression at a 64-token residual window.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic proxy and falsified for old salient tokens, but the evidence is not direct model or serving-kernel validation.

## Recommended next action

Run a bounded real-decoder follow-up using the same 2-bit/3-bit/4-bit residual-window matrix on perplexity plus a long-context needle task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder residual KV quantization validation
- Success threshold: At the same memory budget, residual-window KV quantization reduces loss/perplexity degradation by at least 50% versus all-quantized KV and preserves recent-needle accuracy within 5 percentage points of fp16, while old-needle failures are explicitly measured.
- Stop condition: Stop if residual-window KV does not improve perplexity or recent-needle accuracy over all-quantized KV in two seeded runs, or if dependency/runtime limits prevent a real-decoder test within the local budget.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-kv-cache-quantization-with-residual-token-preservation-0bfba01f6ec3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
