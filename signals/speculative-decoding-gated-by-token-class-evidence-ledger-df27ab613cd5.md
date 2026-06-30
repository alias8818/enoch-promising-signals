# Speculative Decoding Gated by Token-Class Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-gated-by-token-class-evidence-ledger-df27ab613cd5`
Run ID: `speculative-decoding-gated-by-token-class-evidence-ledger-df27ab613cd5-20260613T054432343149+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b47ae733d08

## What looked useful

The fixed ledger_lcb_n4_t0.50 policy improved mean relative cost proxy by +3.19%, +2.70%, +1.96%, and +0.70% for draft weights 0.02, 0.05, 0.10, and 0.20 across two calibrated runs, while increasing accepted/proposed rate but reducing tokens per target call.

## Boundaries and scale limits

Not a production latency benchmark; not exact speculative sampling; only two small prompt samples, one target/draft pair, k=4, greedy decoding, and cost proxies rather than optimized wall-clock serving measurements.

## Claim scope

Small GPT-2/distilGPT-2 greedy speculative-decoding proxy with 20-prompt calibrated and 20-prompt replication runs: an online token-class lower-confidence-bound ledger can improve target-position-plus-draft-cost proxies modestly when draft cost is low to moderate.

## Why it stopped

Bounded proxy evidence supports a small mechanism effect, but the result is not full validation because it uses greedy decoding, small GPT-2-class models, tiny prompt samples, and cost proxies instead of real serving latency.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement exact or production-equivalent speculative decoding with fixed ledger parameters and measure real tokens/sec latency on held-out prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-latency validation of fixed token-class ledger gating for speculative decoding
- Success threshold: At least 2% measured tokens/sec improvement over fixed-k baseline on held-out prompts with identical greedy outputs and no regression greater than 1% on any major prompt-length bucket.
- Stop condition: Stop if fixed ledger gating fails to beat baseline by 2% measured tokens/sec or if output equivalence fails under the intended decoding mode.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-gated-by-token-class-evidence-ledger-df27ab613cd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
