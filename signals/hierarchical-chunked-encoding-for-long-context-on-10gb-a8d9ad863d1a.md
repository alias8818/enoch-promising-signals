# Hierarchical Chunked Encoding for Long Context on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-chunked-encoding-for-long-context-on-10gb-a8d9ad863d1a`
Run ID: `hierarchical-chunked-encoding-for-long-context-on-10gb-a8d9ad863d1a-20260608T072904664727+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ea49e4cdc158

## What looked useful

Hierarchical chunking reduced attention-score elements by 7.98x at length 512 and analytically by 124.06x at length 8192 with chunk size 64, but the tested query-independent single mean summary per chunk stayed near chance on random key-value retrieval while an exact full-context scan reached 100%.

## Boundaries and scale limits

No natural-language corpus, GPT-2-small-class baseline, long training run, 7B+ model, or full long-context benchmark was run. Learned Transformer controls also failed the hard random retrieval task, so this is not a trained-architecture win/loss claim beyond the fixed-summary bottleneck probe.

## Claim scope

Bounded synthetic evidence for a naive single-summary-per-chunk hierarchical encoder on random key-value retrieval at sequence length 512, plus analytic attention-score scaling through length 16384.

## Why it stopped

Proxy/early falsification of the naive fixed-summary mechanism, not a full validation of hierarchical long-context modeling.

## Recommended next action

Stop this run as no-paper useful signal; next test should replace fixed mean summaries with a query-conditioned chunk reader or multiple summary slots and require clear retrieval accuracy above chance against an exact/control baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Query-conditioned chunk reader for long-context retrieval on local GPU
- Success threshold: At least 80% retrieval accuracy at seq_len 512 and at least 50% at seq_len 2048 while using at least 4x fewer attention-score elements than full attention.
- Stop condition: Stop if the improved hierarchical reader remains within 2x chance accuracy after a calibrated under-15-minute GPU run or if memory/runtime exceeds the full-attention control at the tested lengths.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-chunked-encoding-for-long-context-on-10gb-a8d9ad863d1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
