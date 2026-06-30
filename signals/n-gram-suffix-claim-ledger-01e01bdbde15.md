# N-gram Suffix Claim Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-claim-ledger-01e01bdbde15`
Run ID: `n-gram-suffix-claim-ledger-01e01bdbde15-20260603T183345046102+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

Verified suffix-ledger lookup achieved 14.34x to 463.37x speedup versus naive scan with 0 false positives and 0 false negatives in the tested cases; suffix-only acceptance produced about 0.50 false-positive rate on suffix-collision negatives. Longer suffix keys reduced candidate pressure and improved verified lookup speed on the synthetic ablation.

## Boundaries and scale limits

No semantic entailment, paraphrase, model-generated claim, citation-quality, million-document, or web-scale validation was run. The Python prototype is memory-heavy, reaching 1.33 GB max RSS in the main benchmark, and would need compact integer postings before larger evaluation.

## Claim scope

For exact token n-gram support checks with n=5..12 on bounded synthetic corpora up to 284,966 tokens and a local /usr/share/doc corpus of 58,809 tokens, a suffix-keyed ledger followed by full candidate verification preserved exact-match correctness and accelerated lookup versus naive full scans. Suffix-only acceptance was unsafe under adversarial suffix-collision negatives.

## Why it stopped

The local probe supports a practical mechanism but is not paper-ready because it only tests exact n-gram lookup on bounded synthetic/local corpora and directly falsifies suffix-only acceptance as a safe claim rule.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded deepen experiment with compact integer postings and generated-claim exact-support labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compact verified suffix ledger on generated exact-support claims
- Success threshold: Verified lookup has 0 exact-match false positives and false negatives, at least 10x median speedup over naive scan, and less than 50 bytes per indexed n-gram on the million-token corpus.
- Stop condition: Stop if compact postings exceed 100 bytes per indexed n-gram, verified lookup falls below 3x speedup, or any exact-match false positive appears after full verification.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-claim-ledger-01e01bdbde15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
