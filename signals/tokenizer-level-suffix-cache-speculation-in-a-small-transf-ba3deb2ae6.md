# Tokenizer-level suffix-cache speculation in a small transformer loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tokenizer-level-suffix-cache-speculation-in-a-small-transf-ba3deb2ae6`
Run ID: `tokenizer-level-suffix-cache-speculation-in-a-small-transf-ba3deb2ae6-20260519T200650252657+0000`

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

- Parent run decision: KV-Cache Suffix-Array Speculation: enoch://control-plane/projects/kv-cache-suffix-array-speculation-2fdda793fba3/runs/kv-cache-suffix-array-speculation-2fdda793fba3-20260519T200127097182+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b619b6e6d9ae

## What looked useful

Correct cached suffixes achieved exact greedy parity on 512/512 main prompts and 256/256 replicate prompts, 100% suffix-token acceptance, 85.7% model-call reduction, and 6.11x/6.02x wall-clock speedups. Wrong-cache controls had 0% acceptance, 0% call reduction, and slight slowdowns.

## Boundaries and scale limits

Synthetic deterministic token distribution; tiny 2-layer CPU transformer; full-context forwards rather than production KV-cache serving; no natural text/tokenizer trace validation; no pretrained GPT-2-small-class or larger model; no sampling-policy validation.

## Claim scope

In a controlled synthetic small causal-transformer greedy decode loop with deterministic trigger-to-suffix token patterns, tokenizer-level suffix-cache speculation can preserve exact greedy output while reducing model calls by 85.7% and improving CPU wall-clock decode time by about 6x.

## Why it stopped

No-paper closure: the Tier 1 direct mechanism test is positive, but evidence is synthetic and too narrow for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on real tokenizer traces using a GPT-2-small-class model with KV-cache-aware suffix verification; stop if accepted suffix tokens cover less than 10% of generated tokens or wall-clock speedup is below 1.15x at exact-output parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token GPT-2-small suffix-cache speculation with KV-aware verification
- Success threshold: At exact greedy-output parity, accepted suffix tokens cover at least 10% of generated tokens and end-to-end wall-clock decode speedup is at least 1.15x versus a KV-cache greedy baseline, with a wrong-cache/disabled-cache control showing no comparable gain.
- Stop condition: Stop as negative if exact parity fails, accepted suffix coverage is below 10%, or end-to-end speedup is below 1.15x after controlling for verification overhead.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-level-suffix-cache-speculation-in-a-small-transf-ba3deb2ae6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
