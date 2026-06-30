# MinHash Dedup Threshold Has a Non-Trivial Optimum for Tiny LMs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-dedup-threshold-has-a-non-trivial-optimum-for-tiny-lms-010467313810`
Run ID: `minhash-dedup-threshold-has-a-non-trivial-optimum-for-tiny-lms-010467313810-20260609T143413924106+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e1da85b33ea

## What looked useful

Threshold 0.72 retained about 86.1% of documents and achieved mean validation NLL 1.600096, beating no dedup at 1.603364 and aggressive threshold 0.30 at 1.713158. The 0.72 threshold was best for every seed.

## Boundaries and scale limits

Synthetic corpus, count-based trigram LM, five seeds, 120 document families, no neural transformer training, no real web/text benchmark, and no full-scale token-budget control.

## Claim scope

In a controlled synthetic corpus with near-duplicate families and repeated boilerplate, MinHash thresholding before training a tiny smoothed trigram language model produced a consistent interior validation-loss optimum across five seeds.

## Why it stopped

Completed bounded proxy experiment; result is useful mechanism evidence but not direct publication-grade evidence for tiny neural LMs or real corpora.

## Recommended next action

Run a bounded deepen follow-up on a real small text corpus with a tiny neural LM and the same threshold sweep before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny neural LM MinHash threshold sweep
- Success threshold: An interior threshold beats both no dedup and the most aggressive threshold on mean validation NLL by at least 0.5% across at least three seeds, with matching or better test NLL and documented retained-token tradeoffs.
- Stop condition: Stop if no interior threshold beats no dedup on validation NLL in at least two of three seeds, or if gains vanish on the clean test split.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-has-a-non-trivial-optimum-for-tiny-lms-010467313810`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
