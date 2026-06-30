# Fixed Sparse Attention for 4K Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fixed-sparse-attention-for-4k-context-on-cpu-63d85b3eaad3`
Run ID: `fixed-sparse-attention-for-4k-context-on-cpu-63d85b3eaad3-20260604T110328493414+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

Fixed local sparse attention can make the raw 4K CPU attention computation much cheaper in a bounded synthetic benchmark, but the local-only mask has long-range reachability limits and needs quality validation before it is a viable architecture claim.

## Boundaries and scale limits

No language-model training, perplexity, retrieval, batching, multi-head layout, quantization, production kernel, or real workload quality evidence was tested. Only a local causal fixed sparse mask was benchmarked.

## Claim scope

On this CPU worker, a NumPy vectorized fixed local causal attention pattern with window 128 over synthetic float32 Q/K/V tensors at length 4096 and dimension 64 was 23.31x faster than a dense causal NumPy baseline and reduced estimated score storage from 64 MiB to 2 MiB.

## Why it stopped

No-paper closure: the run produced a useful CPU mechanism signal, but only on synthetic Q/K/V tensors; this is not direct model-quality evidence or full validation.

## Recommended next action

Run a bounded deepen test comparing local-only, local-plus-global, and dilated fixed sparse masks against dense attention on a small synthetic retrieval or tiny language-model quality task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality Check for Fixed Sparse 4K CPU Attention Patterns
- Success threshold: At length 4096, a fixed sparse pattern reaches at least 95% of dense baseline task accuracy or within 5% relative perplexity while retaining at least 5x CPU attention runtime speedup.
- Stop condition: Stop if all tested fixed sparse masks lose more than 10% relative task quality versus dense attention or fail to retain at least 3x CPU attention runtime speedup.

## Evidence references

- Artifact root: `<local-path>/projects/fixed-sparse-attention-for-4k-context-on-cpu-63d85b3eaad3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
