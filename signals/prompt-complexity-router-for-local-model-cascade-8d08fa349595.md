# Prompt-complexity router for local model cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-complexity-router-for-local-model-cascade-8d08fa349595`
Run ID: `prompt-complexity-router-for-local-model-cascade-8d08fa349595-20260609T141331662540+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7d58c3a87292

## What looked useful

Best combined router reached 0.8127 accuracy at 30% escalation versus 0.7923 cheap-only, 0.7945 strong-only, and 0.8038 confidence-threshold at the same escalation fraction. Complexity-only routing did not reliably beat cheap-only.

## Boundaries and scale limits

Classification proxy only; no generative LLM pair, no real prompt-quality labels, no latency or memory measurement for local LLM serving, one dataset and one deterministic split.

## Claim scope

On a reproducible six-category 20 Newsgroups local classifier cascade, prompt/document complexity alone is a weak router, but complexity features combined with cheap-model uncertainty improve selective escalation accuracy over cheap-only and confidence-threshold baselines at fixed escalation budgets.

## Why it stopped

No-paper useful-signal closure: this was a bounded proxy validation, not full evidence for generative local model cascades.

## Recommended next action

Run the same routing protocol on a real local LLM pair with direct task-quality labels and measured latency/cost before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local LLM cascade routing with uncertainty plus complexity features
- Success threshold: At 30% or lower escalation, combined router beats confidence-only routing by at least 1 absolute quality point and recovers at least half of the always-small to always-large quality gap with lower measured cost than always-large.
- Stop condition: Stop if complexity plus uncertainty fails to beat confidence-only routing on two held-out task families or if the stronger local model does not materially outperform the cheap model.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-complexity-router-for-local-model-cascade-8d08fa349595`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
