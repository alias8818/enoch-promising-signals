# Live LLM PASS transcript validation for repeated prompt-anchor features

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442`
Run ID: `live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442-20260621T200901721971+0000`

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

- Parent run decision: Prompt-Anchored Self-Speculation via Repetition and Idiom Detection: enoch://control-plane/projects/prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc/runs/prompt-anchored-self-speculation-via-repetition-and-idiom-detection-a18105a6bcbc-20260621T192101578755+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/800ffea83752

## What looked useful

Layered repeated-anchor validation reached 10/10 exact match versus 6/10 for the best baseline, exceeding the predeclared +0.30 margin threshold with a +0.40 margin.

## Boundaries and scale limits

Small synthetic Tier 1 test only; deterministic extractive validator; no live LLM generation, natural operator transcripts, broad paraphrase robustness, or large-scale validation.

## Claim scope

In a 10-task synthetic controlled replay benchmark with repeated stable prompt anchors and later contradictory one-off anchors, a repeated-anchor validation strategy recovered the stable anchor value more accurately than no memory, transcript search, and flat retrieval.

## Why it stopped

Tier 1 direct transcript/retrieval mechanism test produced a useful signal, but the run used a deterministic validator rather than live LLM generation and is not paper-positive.

## Recommended next action

Run one bounded live-LLM deepen test on the same replay design plus paraphrased variants before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM repeated prompt-anchor context consumption test
- Success threshold: Layered validated-anchor context achieves exact_match >= 0.80 and at least +0.20 over the best baseline on live LLM outputs, with hallucinated anchor rate no higher than baseline.
- Stop condition: Stop if layered context fails to beat the best baseline by +0.20, if hallucinated anchor rate increases, or if no live LLM backend can be run without credentials or long compute.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
