# Principled Residual Channels for KV Cache Aggressive Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `principled-residual-channels-for-kv-cache-aggressive-compression-ec2e331e225f`
Run ID: `principled-residual-channels-for-kv-cache-aggressive-compression-ec2e331e225f-20260613T210130978784+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

Residual-error channel selection improved mean attention-output NRMSE versus random by 2.41%, 3.96%, and 4.55% for rank/residual settings 1/2, 2/4, and 4/8; paired bootstrap CIs for random-minus-residual-error mean NRMSE were positive in all three settings.

## Boundaries and scale limits

Proxy-only local evidence: short prompts, distilgpt2, offline tensor reconstruction, no real KV-cache implementation, no decode latency, no long-context perplexity, no downstream task accuracy, and no 7B+ validation.

## Claim scope

On extracted distilgpt2 attention tensors with offline per-head low-rank K/V reconstruction, preserving residual-error-selected channels reduced causal-attention output NRMSE versus equal-size random residual channels across three small compression settings.

## Why it stopped

No-paper closure: this run produced a reproducible proxy mechanism signal, but not direct serving or language-model quality evidence.

## Recommended next action

Run a bounded deepen follow-up that implements residual-error channel selection inside an actual incremental KV-cache decoding path and measures perplexity plus latency/memory at fixed KV budget on GPT-2-small-class workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-error channels in real cached decoding
- Success threshold: At equal KV memory budget, residual-error channels reduce perplexity or next-token loss degradation by at least 5% relative to the best non-principled residual-channel control while preserving most of the compression memory benefit.
- Stop condition: Stop if residual-error selection fails to beat random or magnitude controls on perplexity/loss at two memory budgets, or if implementation overhead removes the practical latency/memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-for-kv-cache-aggressive-compression-ec2e331e225f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
