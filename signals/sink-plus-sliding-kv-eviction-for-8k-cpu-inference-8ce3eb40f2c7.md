# Sink-plus-Sliding KV Eviction for 8K CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sink-plus-sliding-kv-eviction-for-8k-cpu-inference-8ce3eb40f2c7`
Run ID: `sink-plus-sliding-kv-eviction-for-8k-cpu-inference-8ce3eb40f2c7-20260604T214515011217+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/78b7f7db23db

## What looked useful

At seq_len=8192, dim=64, sink=16, and equal retained budgets of 256/512/1024 tokens, sink-plus-sliding improved sink_recent cosine by +0.280/+0.342/+0.220 and retained mass by +0.0356/+0.0500/+0.0339 versus sliding-only. Recent-only and random scenarios were effectively neutral. Absolute relative L2 error remained high, with best tested sink_recent budget 1024 still at mean error 2.999 and retained mass 0.160.

## Boundaries and scale limits

No real language model, tokenizer, perplexity, generation-quality, multi-layer accumulation, or production CPU serving stack was evaluated. The result is not publication-grade evidence for 8K LLM inference.

## Claim scope

Bounded NumPy proxy for one-token 8K CPU attention shows that adding 16 retained sink tokens to an equal-size sliding KV budget improves retained attention mass and output cosine only when the synthetic query distribution explicitly attends to initial sink tokens plus recent tokens.

## Why it stopped

Proxy evidence supports the sink mechanism in a constructed attention case but early-falsifies any direct quality claim because absolute output fidelity is poor and no real LLM inference was evaluated.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a bounded real-transformer 8K perplexity/generation evaluation comparing full cache, sliding-only, and sink-plus-sliding at equal KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer 8K KV eviction quality check
- Success threshold: Sink-plus-sliding must reduce perplexity or next-token loss versus sliding-only by at least 5% at the same KV budget on 8K contexts, with no more than 10% decode-time regression and clear layer/head evidence that retained sink tokens carry attention mass.
- Stop condition: Stop if sink-plus-sliding is not better than sliding-only on real-model loss/perplexity at equal KV budget, or if attention diagnostics show negligible mass on retained sink tokens.

## Evidence references

- Artifact root: `<local-path>/projects/sink-plus-sliding-kv-eviction-for-8k-cpu-inference-8ce3eb40f2c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
