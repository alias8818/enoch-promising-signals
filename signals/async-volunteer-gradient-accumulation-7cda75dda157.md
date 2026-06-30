# Async Volunteer Gradient Accumulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `async-volunteer-gradient-accumulation-7cda75dda157`
Run ID: `async-volunteer-gradient-accumulation-7cda75dda157-20260608T045400753476+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Async accumulation remained effectively performance-equivalent to synchronous accumulation under the tested modest staleness/dropout regimes; simple staleness weighting reduced observed staleness but cost nearly 2x gradient evaluations and did not improve validation metrics.

## Boundaries and scale limits

Toy synthetic tasks only; no real distributed clients, no network serialization or bandwidth constraints, no adversarial workers, no non-IID volunteer data, no privacy/security controls, no language-model or GPT-2-small-class baseline, and observed p95 staleness reached only 4 server updates.

## Claim scope

In a local PyTorch simulation on synthetic linear and two-moons classification tasks, asynchronous volunteer-style microbatch gradient accumulation with modest staleness and 20% dropout matched synchronous accumulation within tiny validation-loss and accuracy deltas over 5 seeds.

## Why it stopped

No-paper closure: this is useful local simulation evidence, but it is not direct enough or broad enough to support a publication-grade volunteer-scale training claim.

## Recommended next action

Run a bounded deepen test using a small language model or real distributed emulator with equal gradient-evaluation budgets, explicit non-IID/dropout/bandwidth controls, and a severe-staleness sweep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compute-normalized async volunteer accumulation on a small language model or distributed emulator
- Success threshold: Async volunteer accumulation is useful if final validation loss or perplexity is within 5% of synchronous accumulation at equal gradient-evaluation budget while p95 staleness exceeds 10 updates and dropout is at least 20%.
- Stop condition: Stop as negative if async validation loss or perplexity is more than 10% worse than synchronous accumulation in two independent seeds under equal gradient-evaluation budget, or if communication/coordination overhead dominates the saved compute.

## Evidence references

- Artifact root: `<local-path>/projects/async-volunteer-gradient-accumulation-7cda75dda157`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
