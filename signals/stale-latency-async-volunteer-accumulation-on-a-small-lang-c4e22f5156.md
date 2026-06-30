# Stale-latency async volunteer accumulation on a small language model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `stale-latency-async-volunteer-accumulation-on-a-small-lang-c4e22f5156`
Run ID: `stale-latency-async-volunteer-accumulation-on-a-small-lang-c4e22f5156-20260608T142050669536+0000`

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

- Parent run decision: Compute-normalized async volunteer accumulation on a small language model or distributed emulator: enoch://control-plane/projects/compute-normalized-async-volunteer-accumulation-on-a-small-3345bff964/runs/compute-normalized-async-volunteer-accumulation-on-a-small-3345bff964-20260608T102756206348+0000
- Parent run decision: Async Volunteer Gradient Accumulation: enoch://control-plane/projects/async-volunteer-gradient-accumulation-7cda75dda157/runs/async-volunteer-gradient-accumulation-7cda75dda157-20260608T045400753476+0000

## What looked useful

Stale gradients were consistently harmful at equal token budget: async_stale final validation loss averaged 3.0006 versus 2.2120 for sync and 2.2016 for async_delay0; paired stale-minus-sync loss delta averaged +0.7886 nats and perplexity was 2.21x worse. Mean stale/fresh gradient cosine was only 0.243, supporting staleness misalignment as the mechanism.

## Boundaries and scale limits

Single GB10 local simulation; small byte-level model; no real volunteer network, heterogeneous device scheduling, bandwidth faults, adversarial clients, GPT-2-scale BPE model, or long distributed run.

## Claim scope

On a 3-layer byte-level Transformer trained on WikiText-2 for 600 optimizer steps across seeds 0, 1, and 2, naive stale-latency volunteer-style gradient accumulation with mean delay about 9.9 optimizer versions substantially worsens validation loss versus synchronous training, while a zero-delay worker-copy control matches the synchronous baseline.

## Why it stopped

Tier 2 fixed-seed medium confirmation produced a consistent negative result for naive stale-latency accumulation rather than a paper-positive positive.

## Recommended next action

Stop this naive stale-latency accumulation line as no-paper evidence; only pursue a bounded mitigation follow-up if testing delay-aware weighting or rejection against the same fixed-seed baseline.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Delay-aware filtering for stale volunteer gradients on a small language model
- Success threshold: A mitigation is worth deeper validation only if mean validation perplexity is within 5% of synchronous baseline and at least 50% of simulated volunteer gradients are still used at mean delay near 10 optimizer versions.
- Stop condition: Stop if all mitigation variants remain more than 15% worse than synchronous perplexity or require rejecting more than 80% of stale gradients.

## Evidence references

- Artifact root: `<local-path>/projects/stale-latency-async-volunteer-accumulation-on-a-small-lang-c4e22f5156`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
