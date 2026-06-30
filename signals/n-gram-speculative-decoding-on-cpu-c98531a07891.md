# N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-c98531a07891`
Run ID: `n-gram-speculative-decoding-on-cpu-c98531a07891-20260609T002142757891+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f715af5ee7e

## What looked useful

Best conservative modeled speedups were 2.35x on code-like templates, 1.57x on phrase-like text, and 1.27x on structured logs, while uniform random controls regressed below 1.0x. Draft length should be capped or adapted by domain.

## Boundaries and scale limits

No real transformer, tokenizer, production prompt mix, or end-to-end CPU serving runtime was measured; target verification speedups are modeled rather than directly timed.

## Claim scope

Synthetic replay evidence shows that n-gram speculative drafting can reduce target invocations on repetitive/template-like and phrase-repetitive CPU decoding workloads, but not on high-entropy streams.

## Why it stopped

Proxy/synthetic evidence supports the mechanism in repetitive regimes but is insufficient for a paper or broad CPU-serving claim.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; next run should perform direct CPU transformer integration on a small real model with the same acceptance and speed metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Transformer Test for N-Gram Speculative Decoding
- Success threshold: At least 1.2x end-to-end tokens/second on repetitive real prompts with identical greedy outputs and no more than 5% regression on low-repetition prompts.
- Stop condition: Stop if verifier/integration overhead keeps repetitive-prompt speedup below 1.1x or if output equivalence cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-c98531a07891`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
