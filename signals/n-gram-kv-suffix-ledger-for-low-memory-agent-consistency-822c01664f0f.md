# N-Gram KV Suffix Ledger for Low-Memory Agent Consistency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f`
Run ID: `n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f-20260519T202818718270+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a632fe50dec5

## What looked useful

suffix_ledger_2_5 reached 96.1% stale accuracy versus 0% for recent context, with estimated memory at 89.8% of raw transcript and far below full n-gram indexing at 403.9%; however, reordered aliases dropped to 10.2% accuracy.

## Boundaries and scale limits

No LLM agent, real transcript, learned memory writer, allocator-level memory measurement, or full-scale serving test was run. The high-accuracy suffix ledger used an estimated 89.8% of raw transcript bytes and failed on reordered alias queries.

## Claim scope

In a deterministic synthetic commitment-recall benchmark, a compact suffix n-gram KV ledger recovers stale lexical and relation-paraphrased facts after a 24-record context cutover substantially better than a recent-context baseline.

## Why it stopped

Proxy-only synthetic evidence supports lexical stale-recall but exposes an early failure mode on reordered aliases and does not justify paper-positive claims.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up adding alias canonicalization or semantic fallback to test whether reordered-alias accuracy can exceed 80% while keeping memory below raw transcript.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Alias-Robust Suffix Ledger for Low-Memory Agent Consistency
- Success threshold: Reordered-alias accuracy >= 80%, stale-only accuracy >= 95%, and estimated memory <= 100% of raw transcript bytes across at least 20 seeds.
- Stop condition: Stop if reordered-alias accuracy remains below 50% or memory exceeds raw transcript bytes in the best high-accuracy configuration.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
