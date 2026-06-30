# Context-Ngram Speculative Decoding Without Draft Model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-ngram-speculative-decoding-without-draft-model-vram-ca02b7185d06`
Run ID: `context-ngram-speculative-decoding-without-draft-model-vram-ca02b7185d06-20260529T234741019185+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aa1256092b70

## What looked useful

Context n-gram speculative decoding without draft-model VRAM is strongly useful for repetitive/template-like streams and shows a bounded signal on code traces, but ordinary prose has low acceptance and weak modeled speedup once verification length is charged. GPT-2 BPE synthetic repetition reached 2.86x modeled speedup at slope 0.1 with 0.534 acceptance; GPT-2 BPE local Python code reached 1.66x with 0.253 acceptance; GPT-2 BPE Gutenberg prose peaked around 0.997x-1.083x with 0.052-0.135 acceptance.

## Boundaries and scale limits

No real target LM inference, GPU kernel timing, KV-cache measurement, draft-model baseline, or sampling distribution was tested. Observed text/code traces proxy target model outputs, so this does not validate production latency or broad model behavior.

## Claim scope

Trace-level exact speculative-decoding simulation with a context n-gram proposer over Gutenberg prose, local Python code, synthetic low-repeat text, and synthetic repetitive records using byte, regex word/punctuation, and cached GPT-2 BPE tokenization.

## Why it stopped

Trace-level evidence is useful but insufficient for paper claims because it proxies target outputs and does not measure real model verification latency or GPU/KV-cache behavior.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test is a real target-LM latency implementation on GPT-style tokens comparing greedy decoding versus context-ngram speculation across prose, code, retrieval-copy, and templated prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-target latency test for context-ngram speculative decoding
- Success threshold: At least 1.20x wall-clock throughput over greedy decoding on two practical prompt classes with no more than 3% slowdown on ordinary prose and no additional draft-model VRAM.
- Stop condition: Stop if exact greedy equivalence fails, or if measured wall-clock speedup is below 1.10x on all non-synthetic prompt classes after adaptive gating.

## Evidence references

- Artifact root: `<local-path>/projects/context-ngram-speculative-decoding-without-draft-model-vram-ca02b7185d06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
