# Hierarchical local-global attention for 4k CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-local-global-attention-for-4k-cpu-ea32b79e4bac`
Run ID: `hierarchical-local-global-attention-for-4k-cpu-ea32b79e4bac-20260523T170853928845+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

Hierarchical local-global attention produced the expected 4k CPU speedup, 7.18x-14.27x faster than the dense benchmark at 4096 tokens, but it had low dense-output cosine, 0.269-0.326 at 4096, and failed the token-specific long-range copy probe where dense attention remained high and the mean-summary global path stayed near zero.

## Boundaries and scale limits

No language-model training, no multi-head transformer integration, no learned routing, no optimized BLAS-backed dense baseline, and no real corpus/task quality measurement. The result supports only a bounded CPU-kernel mechanism signal.

## Claim scope

Synthetic single-head CPU attention benchmark at 512-4096 tokens, dimension 32, comparing exact dense attention with fixed-window local attention plus per-window mean key/value global summaries.

## Why it stopped

Bounded synthetic CPU evidence shows a real speed advantage but an early mechanism falsification for dense-attention substitution: mean global summaries lose token-specific long-range retrieval.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is to replace mean block summaries with token-selective global routing and require both long-range copy fidelity and CPU speedup at 4k.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-selective global routing for 4k CPU local-global attention
- Success threshold: At 4096 tokens, at least 5x CPU speedup versus dense attention, long-range copy cosine >= 0.7, dense-output cosine >= 0.7, and no worse than 10% relative accuracy loss on a small real retrieval/copy task.
- Stop condition: Stop as negative if token-selective routing cannot exceed 0.7 long-range copy cosine while maintaining at least 5x 4096-token speedup in the same bounded CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-local-global-attention-for-4k-cpu-ea32b79e4bac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
