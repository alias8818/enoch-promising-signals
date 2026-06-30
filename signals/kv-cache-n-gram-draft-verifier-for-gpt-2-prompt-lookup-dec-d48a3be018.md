# KV-cache n-gram draft verifier for GPT-2 prompt-lookup decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-n-gram-draft-verifier-for-gpt-2-prompt-lookup-dec-d48a3be018`
Run ID: `kv-cache-n-gram-draft-verifier-for-gpt-2-prompt-lookup-dec-d48a3be018-20260524T155211433301+0000`

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

- Parent run decision: N-gram draft speculative decoding for GPT-2 inference: enoch://control-plane/projects/n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382/runs/n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382-20260524T083503296929+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Exact greedy equivalence held on 6/6 prompts. Repeated prompts reduced forwards from 260 to 102 and improved mean throughput by 2.37x; controls proposed no drafts and matched baseline throughput. Overall forwards fell from 390 to 232 with 76.2% draft-token acceptance.

## Boundaries and scale limits

Six prompts, 64 generated tokens each, GPT-2-small only, greedy decoding only, partly synthetic repeated prompts, Hugging Face eager inference, no production serving stack, no batched multi-request load, no larger-model or natural-corpus robustness test.

## Claim scope

In a controlled GPT-2-small greedy-decoding test with repeated and non-repeated prompts, a prompt-lookup n-gram drafter verified through the model KV cache preserved exact greedy outputs and reduced model forward calls on repeated prompts.

## Why it stopped

Tier 1 direct test produced bounded mechanism support but not publication-grade evidence; close as no-paper useful signal rather than claiming broad validation.

## Recommended next action

Run a medium natural-corpus confirmation using long documents with repeated spans, optimized cache truncation on rejection, and a predefined success threshold of exact equivalence plus at least 20% median latency improvement on repeated-span cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus confirmation for GPT-2 prompt-lookup KV verification
- Success threshold: Exact match on 100% of prompts, at least 20% median latency improvement and 30% forward-call reduction on repeated-span prompts, and no more than 5% median latency regression on non-repeated controls.
- Stop condition: Stop if exactness fails, repeated-span acceptance falls below 30%, or non-repeated controls regress by more than 5% median latency after implementation overhead is optimized.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-draft-verifier-for-gpt-2-prompt-lookup-dec-d48a3be018`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
