# Exact-Anchor KV Compression with Residual Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-with-residual-quantization-28fa09fd0f85`
Run ID: `exact-anchor-kv-compression-with-residual-quantization-28fa09fd0f85-20260604T035904000754+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

Exact-anchor residual 3-bit at 3.419 nominal bits/scalar reduced synthetic relative L2 output error to 0.0248 versus 0.0859 for uniform 4-bit, but top-1 match fell to 0.8455 versus 0.9016 and top-8 Jaccard fell to 0.6707 versus 0.8380. Exact-anchor residual 4-bit improved top-1 match but used more bits and still slightly trailed top-8 Jaccard.

## Boundaries and scale limits

No GPT-2-small-class or larger model, no perplexity or generation-quality evaluation, no production KV-cache kernels, no throughput measurement, and no real long-context benchmark were run. Synthetic KV structure and interpolation residuals may not match real model caches.

## Claim scope

On synthetic attention/KV tensors with controlled smoothness and anchor salience, exact anchor plus residual quantization reduced attention output-vector reconstruction error versus uniform quantization at comparable nominal bit budgets, but did not consistently preserve attention ranking. The cached tiny-GPT-2 sanity check was non-discriminating.

## Why it stopped

Mechanism evidence is mixed: output reconstruction improved in synthetic direct tests, but attention-ranking stability regressed and real-model evidence was too weak for a paper or production claim.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded GPT-2-small-class perplexity and decode-quality evaluation comparing uniform KV quantization to exact-anchor residual quantization with attention-ranking diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small exact-anchor residual KV quantization evaluation
- Success threshold: At equal or lower measured KV memory than uniform 4-bit, exact-anchor residual quantization must keep perplexity delta within 1 percent relative, preserve next-token top-1 agreement at least as well as uniform 4-bit, and avoid lower mean attention top-8 Jaccard than uniform 4-bit.
- Stop condition: Stop as negative if exact-anchor residual quantization fails to match uniform 4-bit on perplexity/logit agreement or attention top-k stability at equal or lower measured KV memory.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-with-residual-quantization-28fa09fd0f85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
