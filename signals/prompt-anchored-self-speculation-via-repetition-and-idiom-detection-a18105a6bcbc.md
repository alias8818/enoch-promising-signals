# Prompt-Anchored Self-Speculation via Repetition and Idiom Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc`
Run ID: `prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc-20260621T192101578755+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/800ffea83752

## What looked useful

The combined detector achieved held-out F1 1.000 and AUROC 1.000 on 144 test examples, while anchor-only F1 was 0.408, repetition-only F1 was 0.618, and idiom/spec-only F1 was 0.933 with 3 false positives. This suggests repeated prompt anchoring can reduce false positives beyond idiom/speculation markers alone in the controlled setting.

## Boundaries and scale limits

Synthetic/template-generated corpus only; no live LLM generations, no human-labeled natural transcripts, no multilingual idioms, no semantic/paraphrase repetition, and no production distribution validation.

## Claim scope

On a deterministic synthetic replay suite, combining prompt-anchor overlap, repeated response n-grams, and idiom/speculation markers separates PASS-like responses from controls better than prompt-anchor-only, repetition-only, or idiom/spec-only baselines.

## Why it stopped

Proxy-only synthetic useful signal; the run supports a mechanism but does not provide publication-grade direct evidence.

## Recommended next action

Run a bounded live-transcript follow-up using 2-3 small open models and human/audited labels to test whether repeated prompt-anchor features still improve over idiom/spec-only detection on natural generations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM PASS transcript validation for repeated prompt-anchor features
- Success threshold: Combined detector improves held-out F1 by at least 0.08 over the best single-signal baseline with no more than a 0.05 recall loss, on at least 200 labeled natural responses.
- Stop condition: Stop if the combined detector fails to beat the best single-signal baseline, if label agreement is too low to support evaluation, or if generation runtime would exceed the local CPU/GPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
