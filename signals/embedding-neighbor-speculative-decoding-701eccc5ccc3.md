# Embedding-Neighbor Speculative Decoding

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `embedding-neighbor-speculative-decoding-701eccc5ccc3`
Run ID: `embedding-neighbor-speculative-decoding-701eccc5ccc3-20260521T213723179758+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ea20a1ed6703

## What looked useful

Embedding-neighbor candidate sets beat random controls but lose 9.8-19.3 percentage points of target probability mass and 13.5-28.3 percentage points of teacher-forced token coverage versus same-size top-k controls, making the standalone mechanism unattractive for speculative decoding.

## Boundaries and scale limits

Tested only GPT-2-small and a small built-in text sample; did not test full speculative decoding throughput, larger LMs, broader corpora, draft-model acceptance, KV-cache latency, or sampling quality.

## Claim scope

On a bounded GPT-2-small one-step candidate-set probe over 512 positions, output-embedding nearest-neighbor expansion around top-logit anchors retrieves nontrivial target probability mass but is consistently worse than exact same-size top-k controls.

## Why it stopped

Bounded direct probe found useful structure relative to random but a large consistent deficit versus the natural same-size top-k control; this is no-paper useful-signal evidence, not full-scale validation.

## Recommended next action

Stop this standalone output-embedding-neighbor candidate-set path unless a separate cheap anchor generator and end-to-end latency model can be tested against standard speculative decoding baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/embedding-neighbor-speculative-decoding-701eccc5ccc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
