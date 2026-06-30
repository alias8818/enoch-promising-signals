# Anchor-Precision KV Cache with Windowed Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-precision-kv-cache-with-windowed-compression-fabf83308987`
Run ID: `anchor-precision-kv-cache-with-windowed-compression-fabf83308987-20260629T185731478648+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d384553fe35e

## What looked useful

At context lengths 1024, 4096, and 8192, anchor precision reduced mean relative attention-output error in the anchor-retrieval regime from about 0.106 for same-memory recent-only preservation to 0.000038, 0.000103, and 0.000217 respectively. In local retrieval it matched recent-only near zero error, and in diffuse attention it was effectively neutral versus recent-only.

## Boundaries and scale limits

No real pretrained language model, no perplexity or downstream task benchmark, no packed int4 kernel timing, no quantization metadata overhead accounting beyond simple storage estimates, no multi-layer accumulation study, and no learned semantic anchor selection.

## Claim scope

Synthetic CUDA attention probe over random K/V caches: preserving the first 32 anchor tokens plus a 256-token recent window at higher precision sharply reduces attention-output error versus a same-memory recent-only policy when queries attend to anchors, and is neutral in local or diffuse query regimes.

## Why it stopped

Synthetic direct-attention evidence supports the mechanism only under controlled anchor-attention conditions, but it is proxy evidence rather than full model validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the same policies inside a small pretrained transformer KV-cache decode loop on long-context retrieval and perplexity tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Transformer KV-Cache Anchor Precision Probe
- Success threshold: Anchor precision improves early-fact retrieval accuracy or perplexity by at least 20% of the gap between uniform int4 and fp16 while matching same-budget recent-only on local-retrieval prompts and not increasing estimated KV memory.
- Stop condition: Stop if anchor precision fails to beat same-budget recent-only on early-anchor retrieval at two or more context lengths, or if packed-cache overhead removes the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-precision-kv-cache-with-windowed-compression-fabf83308987`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
