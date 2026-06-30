# Does deduplication help when training on <100M tokens? Test on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `does-deduplication-help-when-training-on-100m-tokens-test-on-gb10-a7ee36fb6b7c`
Run ID: `does-deduplication-help-when-training-on-100m-tokens-test-on-gb10-a7ee36fb6b7c-20260614T123634066519+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b8e093e8ed29

## What looked useful

Exact deduplication had too little duplicate mass in this corpus slice to show a robust material benefit: dedup was better in 2/3 seeds, raw was better in 1/3, mean dedup-minus-raw loss was -0.001969, and the seed standard deviation was 0.005421.

## Boundaries and scale limits

This run used exact deduplication only, one public corpus, a compact 4-layer Transformer, 3M-token streams, 700 optimizer steps per condition, and validation cross-entropy only. It does not test fuzzy/near-deduplication, downstream tasks, duplicate-rich web corpora, or 50M-100M token training.

## Claim scope

On a 90,000-document Wikitext-103 sample with a 3,000,000-token matched training stream per condition, exact normalized document/line deduplication removed 0.1911% of training documents and produced a tiny, non-robust validation-loss difference in a three-seed small GPT-style training run.

## Why it stopped

Bounded direct local evidence found only a tiny mixed exact-dedup effect smaller than seed variation, so it is not paper-positive or a robust practical win.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is fuzzy/near-deduplication on a duplicate-richer <100M-token web-text sample with at least five seeds and the same matched-token protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fuzzy deduplication on duplicate-richer sub-100M-token web text
- Success threshold: Deduplicated training must improve mean validation loss by at least 0.01 and by more than one standard error across at least five seeds, with no seed showing a large reversal.
- Stop condition: Stop if measured duplicate or near-duplicate mass is below 1%, or if the five-seed mean improvement is smaller than seed noise.

## Evidence references

- Artifact root: `<local-path>/projects/does-deduplication-help-when-training-on-100m-tokens-test-on-gb10-a7ee36fb6b7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
