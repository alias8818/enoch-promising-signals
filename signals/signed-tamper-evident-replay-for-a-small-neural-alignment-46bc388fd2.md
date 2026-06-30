# Signed tamper-evident replay for a small neural alignment learner

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-tamper-evident-replay-for-a-small-neural-alignment-46bc388fd2`
Run ID: `signed-tamper-evident-replay-for-a-small-neural-alignment-46bc388fd2-20260527T034243941153+0000`

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

- Parent run decision: Tamper-Evident Replay Buffer for Small Agent Alignment: enoch://control-plane/projects/tamper-evident-replay-buffer-for-small-agent-alignment-29a496e0a39c/runs/tamper-evident-replay-buffer-for-small-agent-alignment-29a496e0a39c-20260524T182400173324+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f353212c01e

## What looked useful

All four tamper classes were detected at 1.0 detection rate. Unsigned label-flipped replay averaged 0.6042 accuracy and 0.3897 unsafe acceptance, while signed verified replay averaged 0.9147 accuracy and 0.0724 unsafe acceptance, matching the clean same-count control within -0.0016 accuracy and -0.0003 unsafe acceptance on paired means.

## Boundaries and scale limits

Synthetic 16-dimensional preference task, 512 replay records per seed, 2048 held-out examples per seed, tiny MLP learner, CPU-only local run, non-adaptive attacker, single writer, no key compromise, no real RLHF/RLAIF pipeline, no LLM-scale validation.

## Claim scope

In a 10-seed synthetic neural preference-classification replay test, HMAC-signed hash-chained replay records detected post-hoc label flips, feature shifts, deletions, and reorderings by an attacker without the signing key; fail-closed verification preserved small-MLP learner accuracy and unsafe-acceptance metrics relative to a clean same-count control.

## Why it stopped

Tier-1 controlled direct test completed and produced useful mechanism support, but the evidence remains synthetic and too small for publication readiness.

## Recommended next action

Do not write a paper from this toy result; run a bounded deepen follow-up using a small real preference-learning or RLHF-style loop with signed replay, key rotation, and adaptive tamper scenarios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed replay integrity in a small RLHF-style preference loop
- Success threshold: Detection rate of 1.0 for non-key-compromise tampering, signed verified replay within 2 percentage points of clean same-count reward-model/safety metrics, and at least 10 percentage points better harmful-acceptance or preference accuracy than unsigned tampered replay.
- Stop condition: Stop as negative if signed verification misses any non-key-compromise post-hoc tamper class, or if fail-closed filtering consistently degrades safety/preference metrics more than 2 percentage points relative to clean same-count controls.

## Evidence references

- Artifact root: `<local-path>/projects/signed-tamper-evident-replay-for-a-small-neural-alignment-46bc388fd2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
