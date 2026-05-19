# Entropy-Arbitrated Speculative Router with N-Gram Fallback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-arbitrated-speculative-router-with-n-gram-fallback-9016e1b6d614`
Run ID: `entropy-arbitrated-speculative-router-with-n-gram-fallback-9016e1b6d614-20260518T014435774704+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b29b30c8532f

## What looked useful

Entropy gating is predictive enough to be useful as a calibration feature, but entropy alone is too low-coverage and too inconsistently calibrated to support a standalone speculative-router paper claim.

## Boundaries and scale limits

Single small public text corpus, character-level n-grams only, no transformer draft/verifier pair, no tokenizer-level LLM evaluation, no rollback implementation, and latency is represented by a simple cost proxy rather than hardware measurements.

## Claim scope

On a Tiny Shakespeare character-level proxy, low conditional entropy from a trained n-gram model identifies a small subset of next-character predictions that are far more accurate than random same-coverage routing, but the usable strict-error coverage is only about 0.7% to 1.1% for the best 1% error settings and is not consistently better than top-probability confidence routing.

## Why it stopped

Proxy evidence supports the routing signal but not the full speculative-serving claim; strict-error coverage is small and confidence-only routing is usually as strong or stronger.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is a calibrated entropy-plus-confidence router across multiple corpora with matched-error comparison against confidence-only routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Entropy-Plus-Confidence N-Gram Router Across Corpora
- Success threshold: At 1% accepted-token error, entropy-plus-confidence must reach at least 5% cheap-token coverage on at least two of three corpora and improve coverage by at least 25% relative over confidence-only at matched error.
- Stop condition: Stop if entropy-plus-confidence fails to beat confidence-only coverage at matched 1% error on two corpora or if validation-selected thresholds exceed 2x the target error on test.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-arbitrated-speculative-router-with-n-gram-fallback-9016e1b6d614`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
