# Quality Filter Aggressiveness for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `quality-filter-aggressiveness-for-tiny-pretraining-f336767d319d`
Run ID: `quality-filter-aggressiveness-for-tiny-pretraining-f336767d319d-20260614T114613737496+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5b380ea115a

## What looked useful

Increasing the proxy quality score by keeping fewer documents did not yield a validation-loss gain. Full corpus mean validation loss was 2.06813; 50% keep was essentially tied at 2.06848; 10% keep worsened to 2.08183 while reducing unique characters from 718 to 356.

## Boundaries and scale limits

Three seeds, 1500 optimizer steps per variant, Wikitext-2 only, character-level tiny Transformer, heuristic line-quality proxy rather than human labels or a production quality classifier.

## Claim scope

In a Wikitext-2, heuristic-quality-filter, fixed-step tiny character-Transformer pretraining probe, aggressive filtering did not improve clean validation loss; full data was best on mean validation loss and 10% keep-rate was clearly worse.

## Why it stopped

Proxy/local evidence does not support aggressive quality filtering for tiny pretraining and is not broad enough for a paper; it is an early falsification, not a full-scale validation.

## Recommended next action

Stop this run as a bounded proxy early falsification of the aggressive-filtering hypothesis; the next useful test is a direct noisy-web-corpus follow-up with classifier or human quality labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct noisy-web quality filtering sweep for tiny GPT pretraining
- Success threshold: Moderate filtering improves clean validation loss by at least 0.02 nats versus both unfiltered and top-decile aggressive filtering, with paired improvements in at least 2 of 3 seeds and without losing more than 30% unique-token coverage versus unfiltered.
- Stop condition: Stop if moderate filtering is within seed variance of unfiltered or if aggressive filtering again worsens validation loss while reducing coverage.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filter-aggressiveness-for-tiny-pretraining-f336767d319d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
