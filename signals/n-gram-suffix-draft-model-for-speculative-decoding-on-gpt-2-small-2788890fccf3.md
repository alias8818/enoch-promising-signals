# N-Gram Suffix Draft Model for Speculative Decoding on GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-draft-model-for-speculative-decoding-on-gpt-2-small-2788890fccf3`
Run ID: `n-gram-suffix-draft-model-for-speculative-decoding-on-gpt-2-small-2788890fccf3-20260611T164900547176+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6f9a06c67866

## What looked useful

Suffix proposals had higher GPT-2 probability, better top-1 agreement, and lower rank than unigram proposals, but sparse count-table draft probabilities were too concentrated, so min(1, p_target/q_draft) acceptance was lower or roughly tied.

## Boundaries and scale limits

CPU-only run; 96-position primary evaluation plus 64-position smoothing sweep; no full-corpus benchmark, no multi-token serving loop, no wall-clock decode speedup measurement, and no calibrated full-vocabulary draft distribution.

## Claim scope

On a small embedded text probe with GPT-2-small target probabilities, a simple corpus-count n-gram suffix draft table improves proposal plausibility versus a unigram draft but does not improve one-token speculative acceptance.

## Why it stopped

Bounded direct acceptance evidence rejects the simple uncalibrated n-gram suffix draft as an acceleration method; this is not a full validation, but it is a reproducible early falsification of the core acceptance claim.

## Recommended next action

Stop this no-paper run; next bounded test should replace the sparse observed-continuation q_draft with a calibrated full-vocabulary/backoff distribution and re-measure GPT-2-small acceptance before any serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated suffix draft distribution for GPT-2-small speculative acceptance
- Success threshold: Calibrated suffix draft improves mean speculative acceptance by at least 25% relative over unigram and reduces target calls per generated token in a small multi-token decode benchmark without worse output likelihood.
- Stop condition: Stop if calibrated variants fail to beat unigram mean acceptance by at least 10% relative on the first standard-corpus GPT-2-small acceptance probe.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-model-for-speculative-decoding-on-gpt-2-small-2788890fccf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
