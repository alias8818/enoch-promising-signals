# N-Gram Block Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-block-speculative-decoding-on-cpu-43817fc64d5b`
Run ID: `n-gram-block-speculative-decoding-on-cpu-43817fc64d5b-20260524T014312859062+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

Across 240 configurations, repeated prompt traces reached 5.79x to 6.54x modeled speedup at gamma=0.10 and retained about 1.8x at gamma=0.50. Public-domain prose only reached 1.35x to 1.39x at gamma=0.10 and was essentially break-even at gamma=0.50. Python stdlib code showed a modest best case of 1.59x at gamma=0.10 and 1.08x at gamma=0.50.

## Boundaries and scale limits

No real Transformer target model was served. Verification cost is modeled as 1 + gamma * drafted_tokens rather than measured with KV-cache CPU inference. Tokenizers were byte and regex word/punctuation tokenizers, not a production LLM tokenizer. Corpora were small to medium local/public traces up to 80k tokens each.

## Claim scope

Trace-level causal n-gram block drafting on CPU worker text/code/prose corpora. Supports target-call reduction for repetition-heavy prompt/history workloads under low marginal block-verification cost; does not support a broad general-prose CPU speedup claim.

## Why it stopped

Trace-level evidence is useful but not direct end-to-end model-serving validation, and normal prose gains are too marginal unless verification is very cheap.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up that measures actual CPU tokens/sec and block-verification marginal cost in a real small decoder serving loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure real CPU block-verification gamma for n-gram prompt lookup decoding
- Success threshold: At least 1.20x end-to-end CPU tokens/sec improvement on repetition-heavy prompt/code workloads with no broad prose claim unless prose also exceeds 1.10x.
- Stop condition: Stop if measured gamma is >=0.50 and end-to-end speedup is <1.10x on both repeated prompt and code workloads, or if implementation overhead erases target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-block-speculative-decoding-on-cpu-43817fc64d5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
