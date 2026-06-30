# Suffix-LMC Speculative Decoding with Zero Draft VRAM on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1`
Run ID: `suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1-20260611T053739748453+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46bcacdb967d

## What looked useful

gpt2 replay accepted 401 of 555 proposed suffix-draft tokens across 480 generated tokens, reducing replay verifier steps from 480 to 136 (0.7167 theoretical call reduction). distilgpt2 accepted 602 of 789 proposals across 640 generated tokens, reducing replay steps from 640 to 162 (0.7469 theoretical call reduction).

## Boundaries and scale limits

No production KV-cache verifier or latency benchmark was implemented; prompts were small and partly repetition-heavy; sampling and broad open-domain corpora were not tested; results are not publication-grade.

## Claim scope

On a small GB10 greedy-trace replay suite with GPT-2-class target models, a zero-parameter suffix/LMC draft over existing token history produced accepted multi-token bursts and reduced estimated target verifier iterations on repeated/template prompts without allocating a separate draft model.

## Why it stopped

Proxy greedy-trace replay supports the mechanism but does not provide direct end-to-end speculative decoding latency evidence or broad-corpus validation.

## Recommended next action

Stop this worker run as a no-paper useful signal; next, implement a real cache-aware verifier and benchmark latency/throughput on repeated-template and non-repetitive prompt controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache verifier benchmark for zero-VRAM suffix-LMC drafting
- Success threshold: At least 20% wall-clock throughput improvement over greedy on repeated/template prompts with exact output match and no regression larger than 5% on non-repetitive controls.
- Stop condition: Stop if accepted replay bursts fail to translate into at least 10% measured throughput gain after a correct cache-aware verifier, or if cache rollback overhead makes non-repetitive controls more than 10% slower.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
