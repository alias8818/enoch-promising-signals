# Sparse Dict Long Context Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-dict-long-context-memory-1a4aa0fd3780`
Run ID: `sparse-dict-long-context-memory-1a4aa0fd3780-20260604T202818915112+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e92de2eb0aa4

## What looked useful

With 4096-dimensional 32-active keys, inverted sparse dictionary retrieval kept 100% accuracy through 20/32 replaced features and was 8.6-13.2x faster than dense scan at 1k-50k records; exact dict lookup was fast but dropped to 0% accuracy under corruption. With 512-dimensional keys, postings touched rose to about 2x records, speedup fell to 1.2-3.0x, and accuracy collapsed at 24-28 replacements.

## Boundaries and scale limits

No language model, learned key formation, natural-language long-context task, parameter-matched transformer baseline, or large-scale serving benchmark was tested. The stress sweep shows the method loses selectivity and robustness when the sparse code dimension is too small.

## Claim scope

Synthetic sparse-code associative retrieval: an inverted sparse dictionary can recover noisy high-dimensional sparse keys with sublinear candidate scoring versus dense overlap scan for up to 50,000 records in this benchmark.

## Why it stopped

Proxy mechanism result only: useful evidence for sparse dictionary retrieval, but not direct evidence for long-context language-model memory.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded sequence-model follow-up that learns sparse keys and compares against dense attention and exact-retrieval controls on synthetic long-context recall.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Sparse-Key External Memory for Synthetic Long-Context Recall
- Success threshold: At 32k-token-equivalent synthetic contexts, learned sparse memory improves recall accuracy by at least 10 percentage points over the dense baseline or matches it with at least 3x lower retrieval latency, while maintaining at least 95% recall under moderate key corruption.
- Stop condition: Stop if learned keys fail to exceed exact/noisy retrieval controls, if collision/tie rates erase the latency advantage, or if gains disappear under parameter/compute matching.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-dict-long-context-memory-1a4aa0fd3780`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
