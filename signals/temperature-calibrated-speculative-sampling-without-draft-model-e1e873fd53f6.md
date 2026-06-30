# temperature-calibrated speculative sampling without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `temperature-calibrated-speculative-sampling-without-draft-model-e1e873fd53f6`
Run ID: `temperature-calibrated-speculative-sampling-without-draft-model-e1e873fd53f6-20260611T221943884081+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/441f70712620

## What looked useful

Draft-free proposals from the current target distribution achieved 2.35x to 3.16x idealized target-call reduction while preserving exact-verification correctness in synthetic Markov targets, but scalar temperature calibration was not robust: it improved topic_shift from 2.402x to 2.574x, selected tau 1.0 for sticky and dirichlet, and did not consistently beat the uncalibrated proposal.

## Boundaries and scale limits

No real transformer, no GPU latency measurement, no KV-cache behavior, no real prompt distribution, and no validation beyond 50k-token synthetic traces per condition. Target-call speedup is idealized and assumes block verification costs one target call.

## Claim scope

Synthetic finite-state Markov proxy with exact speculative accept/reject verification, 64-token vocabulary, 8-token draft blocks, and proposals derived only from the block-start target distribution transformed by a single scalar temperature.

## Why it stopped

No-paper useful signal from a synthetic proxy: exact verification made the no-draft sampler distributionally plausible, but global temperature calibration was only mixed and the result is not full validation.

## Recommended next action

Do not write a paper from this run; run a bounded direct LM follow-up that measures actual block-verification latency and acceptance on a small transformer before investing in larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer latency test for draft-free temperature-calibrated speculative sampling
- Success threshold: At least 1.25x measured end-to-end decoding speedup over direct sampling on a fixed small-model prompt set, with no detectable distribution regression beyond Monte Carlo error and at least 10% relative improvement over the uncalibrated draft-free proposal.
- Stop condition: Stop if measured end-to-end speedup is below 1.05x or calibrated acceptance fails to beat the uncalibrated proposal on two prompt/model seeds.

## Evidence references

- Artifact root: `<local-path>/projects/temperature-calibrated-speculative-sampling-without-draft-model-e1e873fd53f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
