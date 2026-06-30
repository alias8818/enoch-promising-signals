# MinHash-dedup longest-rep data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-longest-rep-data-selection-be00e225ca19`
Run ID: `minhash-dedup-longest-rep-data-selection-be00e225ca19-20260604T052013668320+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1c04344dcd6a

## What looked useful

Longest representative selection achieved 0.985 clean coverage and 0.0001 junk rate in benign clean-extension clusters, but in boilerplate-trap clusters it had 0.573 clean coverage, 0.319 junk rate, and selected the best-clean document in 0% of families versus medoid/shortest at 0.608 clean coverage and 0.117 junk rate. In mixed clusters it traded higher clean coverage (0.846) for higher junk (0.197).

## Boundaries and scale limits

Synthetic 3-scenario experiment with 8 seeds, 300 near-duplicate families per scenario, 6 variants per family, 96-permutation MinHash LSH, and no downstream model training or real web-corpus labels.

## Claim scope

In controlled provenance-labeled MinHash near-duplicate clusters, longest-representative selection preserves the most clean content when extra length is clean extension, but it is not a generally safe default because boilerplate/noise append cases make it retain substantially more junk than medoid or shortest selection.

## Why it stopped

The bounded experiment supports a conditional mechanism but falsifies the broad default-policy claim; this is proxy/synthetic evidence, not full real-corpus or downstream-training validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate a quality-aware longest policy after boilerplate removal or junk scoring on the same harness and one small real labeled corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-aware longest representative after boilerplate filtering
- Success threshold: Quality-aware longest has mixed_realistic clean coverage at least 0.80 while keeping junk rate no more than 0.02 absolute above medoid, and reduces boilerplate_trap junk rate by at least 50% relative to ungated longest.
- Stop condition: Stop if quality-aware longest loses more than 0.08 absolute clean coverage versus ungated longest in mixed_realistic or still has boilerplate_trap junk rate above 0.20.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-longest-rep-data-selection-be00e225ca19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
