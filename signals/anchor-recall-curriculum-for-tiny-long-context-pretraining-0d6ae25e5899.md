# Anchor-Recall Curriculum for Tiny Long-Context Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-recall-curriculum-for-tiny-long-context-pretraining-0d6ae25e5899`
Run ID: `anchor-recall-curriculum-for-tiny-long-context-pretraining-0d6ae25e5899-20260620T232608259455+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8637e62a1db0

## What looked useful

Across three seeds, curriculum reached 100% final 512-token recall at 900 steps using 6.91M tokens, while the 512-token-only baseline reached 80.58% mean accuracy at 600 steps using 9.83M tokens. At 1200 steps both solved the task, but curriculum used 9.22M tokens and 17.41s mean wall-clock versus 19.66M tokens and 39.38s for the baseline.

## Boundaries and scale limits

Only synthetic random key/value recall was tested. No natural-language pretraining, no distractor anchors, no GPT-2-small-class baseline, no longer-than-512 context, no larger model, and no robustness ablations were run.

## Claim scope

On a one-anchor synthetic autoregressive recall task with a 4-layer d_model=128 causal transformer, a 64->128->256->512 short-to-long curriculum reached perfect 512-token recall with fewer tokens and less wall-clock than training only at 512 tokens.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic and small-scale; it supports the mechanism but does not validate long-context pretraining broadly.

## Recommended next action

Run a bounded deepen experiment with multiple anchors and distractors at the same token budgets; stop if curriculum loses its token-efficiency advantage under distractor retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distractor-Robust Anchor-Recall Curriculum
- Success threshold: Curriculum reaches at least 95% mean held-out 512-token recall and beats the long-only baseline by at least 10 absolute accuracy points at an equal or lower token budget across three seeds.
- Stop condition: Stop if both schedules remain below 50% recall after the calibrated budget, or if the long-only baseline matches curriculum accuracy and loss at the same or lower token budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-recall-curriculum-for-tiny-long-context-pretraining-0d6ae25e5899`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
