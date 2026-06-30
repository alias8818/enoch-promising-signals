# Held-out Canary Probe Trust Scoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-canary-probe-trust-scoring-8eb74a912e19`
Run ID: `held-out-canary-probe-trust-scoring-8eb74a912e19-20260609T174310610179+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59032affdc1

## What looked useful

With 35% public-probe gaming, 8 held-out canaries per domain achieved Pearson r 0.946 and RMSE 0.063 at moderate shift 0.35, versus public probes at r 0.799 and RMSE 0.160. Without public-probe gaming, public probes were as good or slightly better than shifted held-out canaries, narrowing the claim to contaminated or gameable visible-probe settings.

## Boundaries and scale limits

Synthetic/proxy-only evidence; no real LLMs, production agents, adaptive attackers, benchmark contamination logs, canary leakage tests, or human-facing trust decisions were evaluated.

## Claim scope

In a controlled synthetic black-box-agent simulation, randomized held-out canary probes predicted hidden-task accuracy better than self-reported confidence and public probes when public probes were gameable; the advantage weakened but persisted under tested canary-domain shift.

## Why it stopped

Proxy-only simulation supports the mechanism but is not direct validation of real model trust scoring.

## Recommended next action

Stop this run as a no-paper synthetic useful signal; the next concrete step is a medium direct benchmark using small open models and contaminated visible probe sets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model canary trust scoring under visible-probe contamination
- Success threshold: Held-out canary scores improve Pearson correlation with hidden-task accuracy by at least 0.10 over visible probes and reduce RMSE by at least 20% in contaminated conditions, without losing more than 0.05 correlation in uncontaminated controls.
- Stop condition: Stop if held-out canaries do not beat visible probes in contaminated conditions across at least two task families, or if canary/task distribution mismatch explains most predictive power loss.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-canary-probe-trust-scoring-8eb74a912e19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
