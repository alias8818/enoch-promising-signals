# Linear Attention for Long Context on Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `linear-attention-for-long-context-on-small-models-2a4cebb065a7`
Run ID: `linear-attention-for-long-context-on-small-models-2a4cebb065a7-20260608T064705315311+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

The fixed-size ELU+1 linear attention state collapses random associative recall as context grows: long-context cosine stayed near zero and sign accuracy near chance even with feature-scale sweeps, indicating a concrete collision failure mode worth checking before expensive small-model training.

## Boundaries and scale limits

Mechanistic NumPy benchmark only; no trained language model, learned projections, natural-language corpus, gated linear-attention variants, state-space hybrids, or multi-seed training study.

## Claim scope

Plain ELU+1 positive-feature linear attention failed exact-match synthetic key-value retrieval for small heads (16, 32, 64) at long contexts up to 32768 tokens, while scaled softmax attention retained high retrieval quality at 32 and 64 dimensions.

## Why it stopped

Scoped mechanism benchmark produced a useful negative signal for plain ELU+1 linear attention, but it is not full validation or paper-ready evidence for the broad long-context small-model idea.

## Recommended next action

Stop this no-paper run; if continuing, run a bounded trained associative-recall comparison between parameter-matched softmax, ELU+1 linear attention, and a gated/delta linear-memory variant to see whether learned updates overcome the fixed-state collision observed here.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trainable gated linear memory versus ELU+1 on long associative recall
- Success threshold: The gated/delta variant reaches at least 0.85 target cosine and 0.95 sign accuracy at 8192 tokens, stays at least 0.30 cosine above ELU+1 at 32768 tokens, and does not exceed the parameter-matched softmax model by more than 10 percent in parameter count.
- Stop condition: Stop if the gated/delta variant remains below 0.60 target cosine at 8192 tokens after matched training budget across three seeds or if it does not materially outperform plain ELU+1.

## Evidence references

- Artifact root: `<local-path>/projects/linear-attention-for-long-context-on-small-models-2a4cebb065a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
