# End-to-End Prompt-Lookup Speculative Decoding on Held-Out Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-prompt-lookup-speculative-decoding-on-held-out-1c00b481b7`
Run ID: `end-to-end-prompt-lookup-speculative-decoding-on-held-out-1c00b481b7-20260531T103700984871+0000`

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

- Parent run decision: Prompt-Lookup Speculative Decoding for Agent Traces: enoch://control-plane/projects/prompt-lookup-speculative-decoding-for-agent-traces-cfe968b578c8/runs/prompt-lookup-speculative-decoding-for-agent-traces-cfe968b578c8-20260530T075511024160+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6747810389ed

## What looked useful

Agent traces contain enough repeated local structure for prompt-lookup drafts to be frequently accepted by a real target LM verifier. This supports the mechanism and justifies a bounded latency-focused deepen run, but it is not paper-positive evidence.

## Boundaries and scale limits

Small model only; local trace corpus only; greedy decoding only; call-count savings rather than optimized production latency; no larger instruction/code model, server batching, long-run robustness, sampling, or broad public trace validation.

## Claim scope

On 40 held-out local Enoch/Codex agent trace windows, prompt-lookup speculative decoding with distilgpt2 greedy verification reduced target forward calls by 74.58% at max draft 8 and 67.66% at max draft 4, with 5/5 checked windows exactly matching plain greedy decoding in each direct run.

## Why it stopped

Tier 1 direct validation produced useful bounded mechanism evidence but not publication-grade or broad full-scale validation.

## Recommended next action

Run a bounded deepen test with an optimized KV-cache verifier on a GPT-2-small-class or small instruction/code model over at least 200 held-out agent trace windows, reporting exactness, target calls, wall-clock latency, and throughput against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized Latency Benchmark for Prompt-Lookup Speculative Decoding on Agent Traces
- Success threshold: At least 25% median latency reduction and zero greedy-equivalence failures across at least 200 held-out trace windows.
- Stop condition: Stop if exactness fails, median latency improvement is below 10%, or prompt-lookup overhead removes call-count savings in the optimized implementation.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-prompt-lookup-speculative-decoding-on-held-out-1c00b481b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
