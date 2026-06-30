# Compressed Landmark Memory for Exact Anchor Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-landmark-memory-for-exact-anchor-retrieval-93663abddb1c`
Run ID: `compressed-landmark-memory-for-exact-anchor-retrieval-93663abddb1c-20260604T143721223586+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7c5b6c075e7f

## What looked useful

Compressed landmark memory can exactly retrieve unique-ish synthetic anchors at 1.8% to 3.5% of compact all-kgram memory when anchor_len >= k + W - 1 and fingerprints are at least 24 bits at this scale, but repeated content causes high ambiguity that fingerprint width does not resolve.

## Boundaries and scale limits

No real document corpus, no production tokenizer, no disk/cache/update evaluation, no corpus-verification retrieval, and no million/billion-anchor scale. Repetitive synthetic data shows content-derived landmarks alone cannot guarantee a unique exact anchor occurrence.

## Claim scope

Synthetic exact-offset retrieval with winnowed k-gram landmark fingerprints on 150k-token IID, Zipf-like, and repetitive corpora; anchors of 64 and 128 tokens; compact memory estimated from fingerprint/hash bits plus 32-bit positions.

## Why it stopped

Proxy/local synthetic evidence supports the mechanism only under unique-anchor assumptions and falsifies a broad exact-anchor claim for repeated content; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use a real text corpus with duplicate-anchor controls and compare occurrence-aware or context-augmented landmarks against the same compact memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus duplicate-aware landmark retrieval
- Success threshold: At <=5% of compact all-kgram memory, achieve >=99.5% exact retrieval and <=0.1% wrong-unique retrieval on real-corpus anchors, including a separately reported duplicate-anchor slice.
- Stop condition: Stop if duplicate anchors remain >1% ambiguous at <=10% compact memory or if context/occurrence metadata erases the compression advantage over a compact all-kgram baseline.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-landmark-memory-for-exact-anchor-retrieval-93663abddb1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
