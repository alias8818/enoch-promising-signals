# Predictive Operator-Model Memory Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `predictive-operator-model-memory-updates-512071ff306f`
Run ID: `predictive-operator-model-memory-updates-512071ff306f-20260620T065702032104+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/86bb76839617

## What looked useful

Across 5 CUDA seeds, predictive operator updates reduced total MSE by 20.95% mean and stale-query MSE for age >= 4 by 33.21% mean, with learned operator RMSE 0.000475 against the true latent transition. Fresh-query MSE was essentially unchanged, localizing the gain to stale memory.

## Boundaries and scale limits

Evidence is limited to low-dimensional synthetic linear dynamics, 12 memory slots, 8-dimensional values, 32-step sequences, 5 random seeds, and a fixed-write explicit-memory control. It does not test natural-language memory, transformer integration, nonlinear memory dynamics, parameter-matched RNN/transformer baselines, or long-horizon production memory updates.

## Claim scope

On a synthetic latent slot-memory task with sparse observations and a fixed unknown linear transition, an explicit learned predictive memory operator reduces held-out stale-query MSE versus a fixed-write memory control and recovers the latent transition.

## Why it stopped

No-paper useful signal: the result is direct for a synthetic mechanism probe but not direct or broad enough for publication-grade evidence about real operator-model memory updates.

## Recommended next action

Run a bounded deepen test with parameter-matched GRU and small transformer controls on nonlinear and semi-natural memory traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Predictive memory operators against parameter-matched sequence-model controls
- Success threshold: Predictive-operator memory improves stale-query MSE by at least 15% versus every parameter-matched baseline while keeping fresh-query MSE within 5% of the best baseline across at least 5 seeds.
- Stop condition: Stop if the stale-query advantage falls below 5% versus any parameter-matched baseline or if gains disappear under nonlinear transition or variable observation-rate ablations.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-memory-updates-512071ff306f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
