# MinHash Deduplication Threshold Sweep on Local Corpus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-deduplication-threshold-sweep-on-local-corpus-d7a871810c08`
Run ID: `minhash-deduplication-threshold-sweep-on-local-corpus-d7a871810c08-20260621T151801326672+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6ee64797e2

## What looked useful

The bounded sweep over 4,560 local controlled pairs selected threshold 0.50 for both tested shingle widths. 3-word shingles reached precision 0.835, recall 0.723, F1 0.775, specificity 0.989; 5-word shingles reached precision 0.829, recall 0.548, F1 0.659, specificity 0.991. MinHash approximation error was low, so failures were mostly label/corpus and shingle-sensitivity issues rather than signature estimation errors.

## Boundaries and scale limits

The seed corpus was only 12 local text files and labels were generated/proxy labels, not human-adjudicated real duplicate labels. Results do not validate production, web-scale, or heterogeneous-corpus thresholds.

## Claim scope

On this scaffold-sized local project corpus with deterministic near-duplicate controls, 3-word shingles with 128 MinHash permutations and a 0.50 threshold gave the best tested F1; 5-word shingles were more brittle to deletion-style variants.

## Why it stopped

Bounded proxy/local-corpus threshold sweep completed, but the available scaffold data is placeholder-only and the generated labels are insufficient for a paper-ready validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, run the same script on a real labeled local duplicate corpus or add adjudicated labels for discovered near-identical local file pairs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adjudicated Local Deduplication Threshold Sweep
- Success threshold: At least 200 adjudicated pairs with F1 >= 0.80 and precision >= 0.90 for a selected threshold, plus documented failure modes.
- Stop condition: Stop if adjudicated precision remains below 0.80 at all thresholds or if recall remains below 0.65 when precision is at least 0.90.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-deduplication-threshold-sweep-on-local-corpus-d7a871810c08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
