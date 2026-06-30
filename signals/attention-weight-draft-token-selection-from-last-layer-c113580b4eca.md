# Attention-Weight Draft Token Selection from Last Layer

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `attention-weight-draft-token-selection-from-last-layer-c113580b4eca`
Run ID: `attention-weight-draft-token-selection-from-last-layer-c113580b4eca-20260523T170726570947+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

Attention-copy@8 reached 11.58% on distilgpt2 and 13.93% on gpt2 across 12,288 sampled positions, beating random_copy@8 and recent_copy@8 near 8%, but losing clearly to context_unigram@8 at 28.62%. This argues against using the method as a standalone draft selector without stronger controls.

## Boundaries and scale limits

Tested only GPT-2-family small models, 128-token windows, head-averaged final-layer attention, copy-style draft candidates x[p+1], and offline hit rate rather than end-to-end speculative decoding throughput or acceptance.

## Claim scope

On WikiText-2 test text with distilgpt2 and gpt2, final-layer head-averaged attention over prior positions provides a measurable continuation-copy signal over random and recency baselines, but is not competitive with a trivial context-unigram draft-token baseline.

## Why it stopped

Bounded local evidence is a useful proxy/direct hit-rate falsification of the standalone selector claim, not a full speculative-decoding validation; the method fails the trivial context-unigram control by 14.69-17.04 percentage points at k=8.

## Recommended next action

Stop this standalone heuristic path unless a follow-up directly tests end-to-end speculative decoding acceptance and throughput against context-frequency and model-logit controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/attention-weight-draft-token-selection-from-last-layer-c113580b4eca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
