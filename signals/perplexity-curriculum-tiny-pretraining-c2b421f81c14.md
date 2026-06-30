# Perplexity-curriculum tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-curriculum-tiny-pretraining-c2b421f81c14`
Run ID: `perplexity-curriculum-tiny-pretraining-c2b421f81c14-20260529T231711229128+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4febaac72315

## What looked useful

Random sample mixing achieved 4.424 mean final validation perplexity over ten seeds; easy-to-hard strict curriculum reached 11.380 (+157.2% vs random) and hard-to-easy reached 10.571 (+139.0% vs random). Both sorted curricula were worse than random for every seed.

## Boundaries and scale limits

Synthetic corpus, character-level MLP, 900 train samples, 160 validation samples, two epochs, ten seeds. Does not validate transformer-scale, natural-corpus, dynamic-loss, paced, or interleaved curriculum schedules.

## Claim scope

In a tiny NumPy character-level language-model pretraining proxy on a synthetic mixed-difficulty corpus, strict global sample ordering by estimated per-sample perplexity/difficulty did not improve held-out perplexity and was substantially worse than random ordering.

## Why it stopped

Proxy early falsification: strict perplexity-sorted curricula were consistently worse than random mixing in the direct tiny-pretraining test, so the result is useful but not paper-positive or a full-scale validation.

## Recommended next action

Stop this strict-sorting hypothesis as a no-paper proxy result; if continuing, run a bounded paced or interleaved curriculum follow-up that preserves random coverage while biasing toward low-perplexity samples early.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paced interleaved perplexity curriculum for tiny pretraining
- Success threshold: Interleaved or paced curriculum must beat random ordering by at least 5% mean final validation perplexity with no worse than random in at least 8 of 10 paired seeds.
- Stop condition: Stop if paced/interleaved schedules fail to beat random by 5% mean final perplexity or lose on more than 2 of 10 paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-curriculum-tiny-pretraining-c2b421f81c14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
