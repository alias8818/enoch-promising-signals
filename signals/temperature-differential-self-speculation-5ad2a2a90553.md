# Temperature-Differential Self-Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `temperature-differential-self-speculation-5ad2a2a90553`
Run ID: `temperature-differential-self-speculation-5ad2a2a90553-20260525T010551036553+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ef73a7cda2a2

## What looked useful

Best non-identical draft temperature was 0.85 for target temperature 1.0, with mean overlap 0.9860 and 7.515 accepted tokens out of 8. Idealized speedup was 4.731x if draft cost were 0.1x, but only 0.946x when draft cost matched the target model, so practical value depends on a genuinely cheap draft path rather than temperature differential alone.

## Boundaries and scale limits

This run used a small n-gram LM, not a neural LLM or serving stack. It did not test GPU batching, KV-cache reuse, early-exit or auxiliary-head draft paths, layer skipping, or output quality beyond exact target-distribution correction.

## Claim scope

On a dependency-free character n-gram language model, using the same next-token distribution at a different draft temperature preserves high speculative verifier acceptance only when the draft temperature is close to the target temperature; temperature difference alone does not produce a speedup when the draft has same-model serial cost.

## Why it stopped

Early proxy evidence: the distributional mechanism works near the target temperature, but a literal same-model temperature-only draft is not a speedup under same-cost verification; this is not a full neural validation.

## Recommended next action

Stop this run as a no-paper useful signal; a next bounded deepen test should use a tiny neural LM or early-exit implementation to measure whether any real self-draft path is cheaper while retaining high acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Neural Temperature-Differential Self-Speculation Latency Probe
- Success threshold: At least 1.2x end-to-end tokens/sec improvement over ordinary sampling while preserving exact target-temperature sampling through rejection correction and accepting at least 6 of 8 draft tokens on average.
- Stop condition: Stop if the draft path is not cheaper than 0.5x target cost, if mean accepted tokens fall below 5 of 8 for all non-identical temperatures, or if corrected sampling cannot be verified against the target distribution.

## Evidence references

- Artifact root: `<local-path>/projects/temperature-differential-self-speculation-5ad2a2a90553`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
