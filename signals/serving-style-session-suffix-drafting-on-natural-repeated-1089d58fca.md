# Serving-style session suffix drafting on natural repeated traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `serving-style-session-suffix-drafting-on-natural-repeated-1089d58fca`
Run ID: `serving-style-session-suffix-drafting-on-natural-repeated-1089d58fca-20260523T090322744227+0000`

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

- Parent run decision: Real-model session suffix draft validation: enoch://control-plane/projects/real-model-session-suffix-draft-validation-b9e50a4a3e/runs/real-model-session-suffix-draft-validation-b9e50a4a3e-20260523T074444492533+0000
- Parent run decision: Session-Ngram Suffix-Tree Speculative Decoding: enoch://control-plane/projects/session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3/runs/session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3-20260523T054434567893+0000

## What looked useful

Session suffix drafting achieved 1.2274x mean verifier-call speedup and saved 53,426 calls over no drafting, versus 1.1068x for the offline order-6 n-gram baseline and 1.1631x for the temporal-shuffle control. However, exact-prefix trie reached 1.3374x and saved 72,751 calls, so the standalone method is not paper-ready.

## Boundaries and scale limits

This is trace-level categorical clickstream simulation, not live LLM serving. The vocabulary is small, sessions are short, and a simple exact-prefix trie baseline outperforms the proposed suffix drafter on this dataset.

## Claim scope

On UCI MSNBC natural clickstream traces with 120k train and 30k test sessions across three fixed seeds, a recency-biased online session suffix drafter reduces serving-style verifier calls versus no drafting, an order-6 n-gram suffix baseline, and a temporal-shuffle control.

## Why it stopped

Tier-2 direct trace simulation supports suffix reuse but fails to beat a simple exact-prefix memorization baseline, so the result is useful mechanism evidence rather than paper-positive evidence.

## Recommended next action

Stop this run as no-paper useful signal; a next bounded test should evaluate a hybrid exact-prefix-plus-suffix drafter on a richer repeated text or tool-call trace where exact full-prefix memorization is less dominant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid exact-prefix and suffix drafting on richer repeated text traces
- Success threshold: Across at least three fixed seeds, the hybrid must improve verifier-call speedup by at least 5% relative over exact_prefix_trie and at least 10% relative over ngram while retaining a positive gap over temporal-shuffle control.
- Stop condition: Stop if the hybrid fails to beat exact_prefix_trie on mean speedup or if the temporal-shuffle control explains most of the measured gain.

## Evidence references

- Artifact root: `<local-path>/projects/serving-style-session-suffix-drafting-on-natural-repeated-1089d58fca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
