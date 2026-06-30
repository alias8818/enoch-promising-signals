# Naturalistic LLM Operator-Memory Update Prediction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `naturalistic-llm-operator-memory-update-prediction-9bf2825d69`
Run ID: `naturalistic-llm-operator-memory-update-prediction-9bf2825d69-20260620T121532720974+0000`

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

- Parent run decision: Predictive Operator-Model Updates from Agent Memory: enoch://control-plane/projects/predictive-operator-model-updates-from-agent-memory-3cb5b32d630b/runs/predictive-operator-model-updates-from-agent-memory-3cb5b32d630b-20260620T115522237902+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Contextual rules achieved mean macro-F1 0.973 across five seeds, while trigger regex reached 0.449 and bag-of-words Naive Bayes reached 0.554; failures concentrate on durable-vs-episodic scope and operator-vs-third-party attribution.

## Boundaries and scale limits

Synthetic snippets only; no real operator traces, no human label adjudication, no modern LLM or embedding classifier, and no held-out real operator/project distribution.

## Claim scope

In a controlled synthetic Tier 1 direct test of naturalistic operator/agent snippets, operator-memory update need is recoverable by context-aware rules, but shallow bag-of-words and trigger-word baselines do not meet the learned-predictor threshold.

## Why it stopped

No-paper closure: controlled synthetic evidence is useful mechanism support but not broad or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with 100-200 sanitized or independently authored naturalistic session snippets, human-reviewed update labels, and an LLM or embedding semantic classifier against the same trigger and lexical controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-reviewed naturalistic operator-memory update prediction
- Success threshold: Semantic classifier macro-F1 >= 0.75 and at least 0.15 above both trigger regex and shallow lexical baselines on held-out labels.
- Stop condition: Stop if semantic classifier macro-F1 is below 0.65 or does not beat trigger/lexical controls by 0.10, or if human label agreement is too low to define the target reliably.

## Evidence references

- Artifact root: `<local-path>/projects/naturalistic-llm-operator-memory-update-prediction-9bf2825d69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
