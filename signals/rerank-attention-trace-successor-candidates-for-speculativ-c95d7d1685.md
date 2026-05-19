# Rerank Attention-Trace Successor Candidates for Speculative Drafting

Status: `useful_signal`
Project ID: `rerank-attention-trace-successor-candidates-for-speculativ-c95d7d1685`
Run ID: `rerank-attention-trace-successor-candidates-for-speculativ-c95d7d1685-20260514T043116573038+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/590fb4ae00cd

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Early falsification on real GPT-2/distilgpt2 WikiText-2 next-token reranking: attention-trace successors were available, but calibration selected lambda 0.0 and trace-heavy settings generally worsened target log-probability and target-rank metrics. This is not full speculative decoding validation.

## Recommended next action

Stop this line: the Tier 1 controlled direct/proxy test selected the draft baseline and did not meet the target-distribution improvement threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/rerank-attention-trace-successor-candidates-for-speculativ-c95d7d1685`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
