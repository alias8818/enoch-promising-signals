# Calibrated Entropy-Plus-Confidence N-Gram Router Across Corpora

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `calibrated-entropy-plus-confidence-n-gram-router-across-co-e23bca791a`
Run ID: `calibrated-entropy-plus-confidence-n-gram-router-across-co-e23bca791a-20260518T015204597465+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b29b30c8532f

## What looked useful

Normalized predictive entropy is a useful n-gram corpus-routing signal, beating random and confidence-only baselines, but adding max-probability confidence hurt or failed to improve held-out NLL and route accuracy.

## Boundaries and scale limits

Small direct Tier 1 test only: 4 text categories, 252 train documents per expert, 14k validation tokens, 28k test tokens, 7k vocabulary, word trigram experts. No neural LM experts, document/window-level routing, broad corpora, or production serving evaluation.

## Claim scope

On a controlled four-category 20 Newsgroups token-level routing test with corpus-specific interpolated trigram experts, calibrated entropy-plus-confidence routing did not improve over entropy-only routing; entropy alone was the best non-oracle router.

## Why it stopped

Direct Tier 1 test falsified the confidence-plus-entropy improvement over the entropy-only baseline at this scale; this is not full validation of all possible routers, but it is enough to close this follow-up as not paper-ready.

## Recommended next action

Stop this confidence-plus-entropy n-gram route as no-paper evidence; if continuing, run the bounded follow-up on document/window-level routing across independent corpora before considering any larger model-serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Window-Level Entropy Router Across Independent Corpora
- Success threshold: Calibrated confidence-plus-entropy must beat entropy-only by at least 1% relative NLL and at least 1 absolute percentage point route accuracy on held-out windows; otherwise close the confidence addition as unsupported and keep only entropy-only as the useful signal.
- Stop condition: Stop if entropy-only again matches or beats calibrated confidence-plus-entropy on held-out windows, or if the entropy-only signal does not beat random by at least 5 absolute percentage points route accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-entropy-plus-confidence-n-gram-router-across-co-e23bca791a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
