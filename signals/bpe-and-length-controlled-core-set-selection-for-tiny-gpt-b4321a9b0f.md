# BPE and Length-Controlled Core-Set Selection for Tiny GPT Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `bpe-and-length-controlled-core-set-selection-for-tiny-gpt-b4321a9b0f`
Run ID: `bpe-and-length-controlled-core-set-selection-for-tiny-gpt-b4321a9b0f-20260605T065813766298+0000`

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

- Parent run decision: Embedding Core-Set Coverage for Tiny Pretraining: enoch://control-plane/projects/embedding-core-set-coverage-for-tiny-pretraining-7d46ae7240eb/runs/embedding-core-set-coverage-for-tiny-pretraining-7d46ae7240eb-20260604T203823963022+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd0adc3b10ec

## What looked useful

Coverage selection increased unique BPE types by about 1.7k over matched random, but final validation loss was worse in all three seeds: coverage-random deltas were +0.0677, +0.0893, and +0.0431 nats. Low-diversity control was best, suggesting BPE type coverage alone is not a reliable early-pretraining core-set objective under these controls.

## Boundaries and scale limits

Small Wikitext-2 candidate pool, 70k selected-token budget, 300 optimizer updates per condition, 2-layer/128-dim tiny GPT, coarse length-bin control rather than exact length distribution matching; no GPT-2-small-class or full-corpus validation.

## Claim scope

Tier 1 direct test on Wikitext-2: a greedy BPE-coverage core-set, controlled to about 70k GPT-2 BPE tokens and coarse document-length-bin budgets, did not improve a 2-layer tiny GPT's held-out validation loss versus matched random selection across three seeds.

## Why it stopped

Replicated Tier 1 direct early falsification: the proposed BPE-coverage core-set mechanism improved token-type coverage but worsened held-out tiny-GPT validation loss versus matched random in every calibrated seed, so it is not paper-positive.

## Recommended next action

Stop this follow-up as a no-paper useful negative; if continuing locally, run an exact length-distribution matched fixed-window follow-up before considering any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-Length Fixed-Window Core-Set Control for Tiny GPT
- Success threshold: Coverage-core-set final validation loss at least 0.03 nats lower than matched random in mean paired delta, with no worse than one losing seed out of three.
- Stop condition: Stop if coverage-core-set is not better than random by at least 0.03 nats mean paired delta or loses in two or more seeds under exact length/window matching.

## Evidence references

- Artifact root: `<local-path>/projects/bpe-and-length-controlled-core-set-selection-for-tiny-gpt-b4321a9b0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
