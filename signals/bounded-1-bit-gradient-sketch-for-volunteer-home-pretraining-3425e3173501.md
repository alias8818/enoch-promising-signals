# Bounded 1-Bit Gradient Sketch for Volunteer Home Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-1-bit-gradient-sketch-for-volunteer-home-pretraining-3425e3173501`
Run ID: `bounded-1-bit-gradient-sketch-for-volunteer-home-pretraining-3425e3173501-20260621T153102244098+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6efb0dc3fabc

## What looked useful

Error feedback reduced the bounded 1-bit mean final eval-loss gap versus fp32 from 1.3860 to 0.2583 across three seeds; bounded 1-bit without error feedback was consistently worse.

## Boundaries and scale limits

Three seeds, synthetic Markov-token data, 80 steps, 8 simulated clients, 327,680 train tokens per mode per seed, no real text corpus, no client churn, no unreliable network, no GPT-2-small-class model, and no long convergence test.

## Claim scope

On a synthetic non-IID volunteer-client next-token proxy with a 108k-parameter tiny transformer, bounded 1-bit gradient sketches need client-side error feedback to approach full-precision averaging; bounded 1-bit without error feedback consistently lags.

## Why it stopped

Proxy experiment produced useful mechanism evidence but not direct/full validation for volunteer home pretraining.

## Recommended next action

Run a bounded direct-text follow-up on a small real corpus with the same fp32, sign, bounded_1bit, and bounded_1bit_ef controls plus explicit communication accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded 1-bit error-feedback gradient sketch on a real small text corpus
- Success threshold: bounded_1bit_ef final validation loss within 5% of fp32 and better than sign and bounded_1bit without error feedback under the same token budget and communication accounting.
- Stop condition: Stop if bounded_1bit_ef is more than 10% worse than fp32 on validation loss in two of three seeds or fails to beat bounded_1bit without error feedback.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-1-bit-gradient-sketch-for-volunteer-home-pretraining-3425e3173501`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
