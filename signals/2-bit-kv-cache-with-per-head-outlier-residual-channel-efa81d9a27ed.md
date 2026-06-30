# 2-bit KV Cache with Per-Head Outlier Residual Channel

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-per-head-outlier-residual-channel-efa81d9a27ed`
Run ID: `2-bit-kv-cache-with-per-head-outlier-residual-channel-efa81d9a27ed-20260611T034756178186+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/513f70c2ab91

## What looked useful

The mechanism is useful for future testing: residual channels helped strongly only when per-head outliers were present. Four residual channels per head cut outlier-case attention NMSE by 87.79% and raised cosine similarity from 0.321760 to 0.911497 with 1.219x bit overhead versus plain 2-bit. Gaussian-control gains were much smaller, indicating the residual path specifically addresses outlier-channel distortion rather than generally fixing 2-bit quantization.

## Boundaries and scale limits

No real language-model perplexity, generation, online cache update, packed-kernel throughput, or 7B+ activation evidence was produced. Channel selection used optimistic full-sequence max-absolute scoring on synthetic tensors.

## Claim scope

Synthetic single-step attention proxy: for B=1, H=16, T=2048, D=128 with four injected high-magnitude channels per head, preserving four exact per-head K/V residual channels reduced attention-output NMSE from 1.613752 to 0.197089 versus plain 2-bit per-head/channel min-max KV quantization, while retaining an estimated 6.564x compression versus fp16 KV cache.

## Why it stopped

Proxy-only evidence is insufficient for a paper or full validation, even though the synthetic mechanism signal supports the hypothesis.

## Recommended next action

Stop this run as a proxy-only useful signal; next run should test a GPT-2-small-class decoder with fp16, plain 2-bit KV, and 2-bit plus per-head residual KV using online channel selection and report perplexity plus attention-output error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real decoder KV-cache test for 2-bit plus per-head residual channels
- Success threshold: At R<=4 residual channels per head, recover at least 50% of the loss/perplexity degradation introduced by plain 2-bit KV while preserving at least 6x estimated KV-cache compression versus fp16 and avoiding worse than 15% decode throughput regression in a local benchmark.
- Stop condition: Stop if R<=4 recovers less than 25% of plain 2-bit degradation on real activations or if online channel selection erases the synthetic benefit.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-outlier-residual-channel-efa81d9a27ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
