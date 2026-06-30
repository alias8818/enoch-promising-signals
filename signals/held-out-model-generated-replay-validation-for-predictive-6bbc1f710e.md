# Held-out model-generated replay validation for predictive memory updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-model-generated-replay-validation-for-predictive-6bbc1f710e`
Run ID: `held-out-model-generated-replay-validation-for-predictive-6bbc1f710e-20260614T072730239020+0000`

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

- Parent run decision: Realistic replay validation for predictive agent memory updates: enoch://control-plane/projects/realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd/runs/realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd-20260614T065032314542+0000
- Parent run decision: Agent Memory Architecture: Retrieval vs Semantic Compression vs Predictive Updates: enoch://control-plane/projects/agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9/runs/agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9-20260614T055232785707+0000

## What looked useful

Predictive memory reached 0.881 accuracy versus 0.209 for transcript and flat retrieval baselines, 0.194 for the no-update ablation, and 0.440 for the shuffled predictive control. Gains exceeded the preregistered thresholds on fixed seeds, while incomplete-premise cases showed a realistic failure mode.

## Boundaries and scale limits

Synthetic rule-governed histories only; no real LLM extraction, human-authored traces, production agent data, long-horizon drift, or non-template natural language scoring. The accepted run is Tier 2 mechanism evidence, not publication-grade deployment evidence.

## Claim scope

On a deterministic, synthetic, model-generated replay distribution with 800 held-out future tasks across five fixed seeds, predictive memory updates improved exact next-action accuracy over transcript search, flat retrieval, no-update, and shuffled predictive controls.

## Why it stopped

The Tier 2 synthetic replay threshold was met, but evidence remains generated and rule-governed, so it supports the mechanism without satisfying the paper gate.

## Recommended next action

Stop this worker run as no-paper useful signal; the next bounded test should replace the rule generator with LLM-generated or human-authored replay histories and evaluate noisy memory extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-generated noisy replay validation for predictive memory updates
- Success threshold: Predictive memory accuracy at least 0.70, at least 0.15 above the best real baseline, and at least 0.15 above no-update and shuffled controls, with false-prediction rate not exceeding the best baseline by more than 0.05.
- Stop condition: Stop as negative if predictive memory fails to beat the best real baseline by 0.15 on two independent fixed-seed corpora or if false predictions exceed the baseline by more than 0.05 without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-model-generated-replay-validation-for-predictive-6bbc1f710e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
