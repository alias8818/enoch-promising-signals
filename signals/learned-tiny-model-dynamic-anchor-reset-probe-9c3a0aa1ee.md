# Learned Tiny-Model Dynamic Anchor Reset Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee`
Run ID: `learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee-20260601T014326214944+0000`

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

- Parent run decision: Dynamic Anchor State Reset for CPU Long-Context: enoch://control-plane/projects/dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256/runs/dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256-20260531T192750821344+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1c64bc485425

## What looked useful

Across three held-out seeds, the learned reset policy met the predeclared Tier 1 threshold: mean relative error reduction versus the best non-oracle control was 44.2% with minimum 42.9%, and mean oracle-gap closure was 53.3% with minimum 52.0%. Learned resets had higher mean change precision than the best hand threshold control while resetting less often.

## Boundaries and scale limits

Three seeds on synthetic vector-prototype streams only; no transformer KV-cache, language modeling, real data, unsupervised reset learning, or GPT-2-small-class baseline was tested.

## Claim scope

In a controlled NumPy synthetic streaming anchor-tracking task with irregular latent anchor changes, a tiny learned reset controller improved closed-loop current-anchor recovery over no-reset, fixed-period reset, and validation-tuned distance-threshold controls.

## Why it stopped

Tier 1 controlled small direct test succeeded as a useful mechanism signal, but evidence remains synthetic and below paper-readiness.

## Recommended next action

Run a bounded deepen follow-up that embeds the learned reset controller in a parameter-matched tiny transformer or recurrent associative-recall model and compares against fixed-period, hand-threshold, no-reset, and oracle-reset controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Dynamic Anchor Reset Confirmation
- Success threshold: Learned reset must reduce held-out retrieval error or loss-derived error by at least 15% versus the best non-oracle reset control across at least 3 seeds and close at least 40% of the control-to-oracle gap.
- Stop condition: Stop if learned reset fails to beat the best non-oracle control on at least 2 of 3 seeds or if gains disappear after parameter matching and validation-only tuning.

## Evidence references

- Artifact root: `<local-path>/projects/learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
