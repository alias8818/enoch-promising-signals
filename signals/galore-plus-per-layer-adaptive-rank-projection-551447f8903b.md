# GaLore-Plus per-layer adaptive rank projection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-plus-per-layer-adaptive-rank-projection-551447f8903b`
Run ID: `galore-plus-per-layer-adaptive-rank-projection-551447f8903b-20260613T092743462855+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/90ea5e0df42f

## What looked useful

Adaptive per-layer ranks selected non-uniform allocations and modestly outperformed uniform rank-8 projection under the same nominal rank budget, suggesting the mechanism is worth one bounded direct GaLore follow-up. The evidence is no-paper because it is a toy proxy and not direct memory-efficient LLM training evidence.

## Boundaries and scale limits

This was not a true GaLore optimizer-state implementation and did not test transformers, token-level language modeling, quantized optimizers, measured optimizer-state memory, or long-horizon LLM pretraining. Projected-gradient methods remained 132% to 139% higher MSE than full Adam in the tested setting.

## Claim scope

On a small heterogeneous teacher-student MLP proxy, per-layer adaptive low-rank gradient projection improved mean final validation MSE over uniform rank projection by 5.84% with a 90% energy ceiling and by 8.68% with a 99% full-budget ablation across three seeds.

## Why it stopped

Closed as a no-paper useful signal: proxy evidence supports a small adaptive-rank mechanism but is insufficient for publication-grade validation of GaLore-Plus.

## Recommended next action

Implement true projected-coordinate GaLore optimizer-state storage and repeat adaptive-versus-uniform ranks on a GPT-2-small-class language-modeling task with validation perplexity, throughput, and memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True GaLore adaptive ranks on GPT-2-small-class language modeling
- Success threshold: Adaptive GaLore must improve mean validation perplexity by at least 3% versus uniform GaLore at matched optimizer-state budget without reducing throughput by more than 10% or increasing peak memory.
- Stop condition: Stop if adaptive ranks fail to beat uniform ranks on mean validation perplexity, require higher memory, or introduce more than 10% throughput regression under matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/galore-plus-per-layer-adaptive-rank-projection-551447f8903b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
