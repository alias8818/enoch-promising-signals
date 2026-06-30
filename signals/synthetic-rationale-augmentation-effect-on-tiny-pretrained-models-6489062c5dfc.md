# Synthetic rationale augmentation effect on tiny pretrained models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `synthetic-rationale-augmentation-effect-on-tiny-pretrained-models-6489062c5dfc`
Run ID: `synthetic-rationale-augmentation-effect-on-tiny-pretrained-models-6489062c5dfc-20260630T135033545379+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a87d697cf665

## What looked useful

Rationale augmentation appears to teach the model to prefer correct rationale-form completions, but it harms direct-answer selection under the same question prompt. Future tests should separate reasoning benefit from answer-format conditioning.

## Boundaries and scale limits

Tiny/small pretrained causal LM only; synthetic templated task only; three seeds; no self-generated rationale evaluation, natural-language benchmark, larger model, or hyperparameter sweep.

## Claim scope

On a synthetic held-out arithmetic comparison task with distilgpt2 fine-tuned for three epochs on 1024 examples across three seeds, synthetic rationale augmentation improved rationale-shaped completion scoring but did not improve direct answer accuracy.

## Why it stopped

Proxy/medium local evidence is mixed: rationale augmentation gives a rationale-format scoring gain but fails the direct answer interface, so it is not a publication-grade positive validation.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should evaluate self-generated rationales with matched direct, rationale, and mixed-format training controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Self-generated rationale control for tiny pretrained arithmetic comparison
- Success threshold: Rationale-only or mixed-format training improves self-generated final-answer accuracy by at least 5 percentage points over direct-only while maintaining rationale arithmetic validity above 80%.
- Stop condition: Stop if rationale or mixed-format models fail to beat direct-only self-generated final-answer accuracy in at least two of three seeds, or if generated rationales are mostly unparsable/arithmetically invalid.

## Evidence references

- Artifact root: `<local-path>/projects/synthetic-rationale-augmentation-effect-on-tiny-pretrained-models-6489062c5dfc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
