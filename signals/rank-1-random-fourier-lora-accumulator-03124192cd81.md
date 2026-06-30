# Rank-1 Random Fourier LoRA Accumulator

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rank-1-random-fourier-lora-accumulator-03124192cd81`
Run ID: `rank-1-random-fourier-lora-accumulator-03124192cd81-20260608T184003726986+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d5119da739e8

## What looked useful

The mechanism has a narrow aligned-basis success mode: K=1536 Fourier atoms fit smooth Fourier targets nearly exactly, but the same budget leaves generic low-rank targets at mean relative error 0.581865 and checkerboard targets at 0.993159, while SVD-LoRA oracles solve those cases with fewer or equal trainable parameters.

## Boundaries and scale limits

CPU-only NumPy proxy; no transformer fine-tuning, no optimizer dynamics, no language-model validation, and no GPT-2-small-class comparison. Matrix targets were synthetic normalized 48x48 updates with five-seed full runs and three-seed high-budget checks.

## Claim scope

At 48x48 matrix-adaptation scale, a scalar-coefficient accumulator over fixed random Fourier rank-1 atoms is not a competitive general replacement for learned-factor LoRA; it succeeds only on an in-family smooth Fourier target when given a large atom budget.

## Why it stopped

Bounded proxy early falsification: the fixed random Fourier scalar-atom accumulator does not efficiently represent generic low-rank or high-frequency rank-1 updates, so the broad parameter-efficient LoRA replacement claim is unsupported without a new alignment mechanism.

## Recommended next action

Stop this general LoRA-replacement line unless reformulated around learned or data-aligned atom bases; a transformer follow-up should only proceed if it tests that distinct alignment hypothesis directly.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Data-Aligned Fourier Atom LoRA Accumulator
- Success threshold: At equal trainable parameter count, data-aligned atoms achieve validation loss within 5% of LoRA improvement over the frozen baseline and at least 30% lower update reconstruction error than fixed random Fourier atoms.
- Stop condition: Stop if data-aligned atoms do not beat fixed Gaussian atoms by at least 10% reconstruction error or if validation loss remains closer to the frozen baseline than to parameter-matched LoRA.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-random-fourier-lora-accumulator-03124192cd81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
