# Bounded KV-Head Pruning for gb10 VRAM Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-head-pruning-for-gb10-vram-reduction-4e7ced639515`
Run ID: `bounded-kv-head-pruning-for-gb10-vram-reduction-4e7ced639515-20260609T151015172792+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7d6a4a111bc8

## What looked useful

At seq_len 4096, 25% and 50% KV-head pruning reduced exact KV-cache bytes by 25% and 50%. Low-energy-head pruning kept relative L2 at 0.0174 and 0.0283, while random-energy controls had large relative L2 error of 0.4654 and 0.6923.

## Boundaries and scale limits

Synthetic attention tensors only; no pretrained model, perplexity, downstream task, fused production attention kernel, long-session serving, or multi-layer compounding validation.

## Claim scope

On a GB10 CUDA tensor probe of grouped-query decode attention, static whole-KV-head pruning gives exact linear KV-cache byte reduction and low output perturbation only when pruned heads are genuinely low contribution; unqualified pruning of random/comparable heads is not supported.

## Why it stopped

Proxy CUDA mechanism evidence is insufficient for a paper and mixed: memory savings are direct, but quality preservation depends on a synthetic low-contribution-head condition and fails under the random-energy control.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a pretrained GQA causal LM with real-text head-importance calibration, perplexity delta, and GB10 decode memory/throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GQA KV-head pruning calibration and perplexity check on GB10
- Success threshold: At least 25% KV-cache byte reduction with <=1% perplexity or next-token loss regression and no decode throughput regression on held-out real text.
- Stop condition: Stop if head-importance ranking is not stable across held-out prompts or if 25% pruning exceeds 1% loss/perplexity regression.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-head-pruning-for-gb10-vram-reduction-4e7ced639515`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
