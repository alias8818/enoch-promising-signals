# Measured CPU LLM cascade trace validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `measured-cpu-llm-cascade-trace-validation-efea0ec556`
Run ID: `measured-cpu-llm-cascade-trace-validation-efea0ec556-20260610T155557452245+0000`

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

- Parent run decision: CPU Cascade Router: Complexity-Aware Model Selection for Local LLM Serving: enoch://control-plane/projects/cpu-cascade-router-complexity-aware-model-selection-for-local-llm-serving-93bf04da9dcf/runs/cpu-cascade-router-complexity-aware-model-selection-for-local-llm-serving-93bf04da9dcf-20260610T154201826850+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3cf9fae43f79

## What looked useful

The tested margin-gated cascade can satisfy a relative large-call reduction threshold only when the always-large baseline is weak. Primary large accuracy was 28%, small was 24%, and predictions were dominated by an answer-letter prior; the gate preserved shared bias rather than reliable correctness.

## Boundaries and scale limits

No full production serving, no large benchmark suite, no generated-answer extraction, no calibrated option-text scoring, and no large instruction-model full run. Qwen smoke was not scaled because CPU scoring was slow and early accuracy was near chance.

## Claim scope

Tier-1 local CPU direct test of confidence-gated LLM cascades using answer-letter conditional log-likelihood traces on 50 balanced multiple-choice prompts with distilgpt2/gpt2, plus an 8-example cached stronger-model smoke with SmolLM2-135M/Qwen2.5-0.5B-Instruct.

## Why it stopped

Controlled direct test failed to produce meaningful cascade validation: relative threshold success was an artifact of near-chance large-model accuracy and uncalibrated small-model margins, not evidence for a reliable CPU LLM cascade.

## Recommended next action

Stop this run as no-paper negative evidence; run one bounded follow-up that replaces answer-letter scoring with calibrated option-text or generated-answer scoring and requires a competent large baseline before evaluating cascade savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated option-text CPU LLM cascade validation
- Success threshold: Large baseline accuracy >=60%; cascade accuracy >=95% of large accuracy; large-call reduction >=30%; estimated end-to-end latency reduction >0%; no single answer-position prediction rate above 45%.
- Stop condition: Stop negative if the large baseline is below 60%, if confidence remains anti-calibrated, or if every quality-preserving threshold has nonpositive latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/measured-cpu-llm-cascade-trace-validation-efea0ec556`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
