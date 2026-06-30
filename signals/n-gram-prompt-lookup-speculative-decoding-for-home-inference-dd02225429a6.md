# N-Gram/Prompt-Lookup Speculative Decoding for Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6`
Run ID: `n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6-20260523T052814500746+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e926d567412a

## What looked useful

Oracle copy traces averaged 4.08x verifier-call reduction while noncopy controls stayed at 1.0x. distilgpt2 averaged 2.53x across four prompts/settings with large gains for quote/code prompts and no gains for policy-summary/log prompts.

## Boundaries and scale limits

Tested oracle traces plus sshleifer/tiny-gpt2 and distilgpt2 greedy continuations only; no integrated llama.cpp/vLLM serving implementation, no 3B-8B model benchmark, no robust workload mixture, and no valid GPU chunk-latency result.

## Claim scope

Bounded trace replay and small-LM greedy evidence show prompt-lookup speculative decoding can reduce verifier calls when generated text copies or quotes prompt spans, especially code and quote-style prompts; it gives no benefit on noncopy traces and can give no benefit on some ordinary prompts.

## Why it stopped

No-paper useful signal: the mechanism is supported for copy-heavy traces but the result is bounded/proxy evidence rather than full home-inference serving validation.

## Recommended next action

Stop this trace-level run; next run should integrate prompt lookup into a real local serving path and measure latency/tokens-per-second on a 3B-8B model with copy, quote, code, summary, and noncopy workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated prompt-lookup latency benchmark on a local 3B-8B serving model
- Success threshold: At least 20% median end-to-end decode throughput improvement on copy/quote/code subsets, less than 5% slowdown on noncopy subsets, and byte/token-identical greedy outputs versus baseline.
- Stop condition: Stop if integrated lookup overhead causes more than 5% median slowdown on mixed workload or if accepted-token rate is below 0.5 accepted tokens per verifier call on all copy/quote/code subsets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
