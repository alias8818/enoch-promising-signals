# Context-Derived N-Gram Suffix Cache for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-derived-n-gram-suffix-cache-for-speculative-decoding-5c6ad57612e4`
Run ID: `context-derived-n-gram-suffix-cache-for-speculative-decoding-5c6ad57612e4-20260528T190601780789+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/233ff68cbe05

## What looked useful

The mechanism is workload-gated: max_n=8,draft_len=8 achieved 6.33 accepted tokens/step and 6.38x modeled speedup on synthetic code edits, 1.99 accepted tokens/step and 2.60x on templated RAG-copy text, but only 0.03-0.07 accepted tokens/step and below-1.0x modeled speedup on Gutenberg prose. Shuffled controls stayed below 0.92x.

## Boundaries and scale limits

No real target model, tokenizer-specific serving implementation, KV-cache rollback accounting, batching, sampling, or end-to-end latency was measured. Positive evidence is mostly synthetic and repetitive; natural-prose evidence is negative under the proxy cost model.

## Claim scope

A model-free online suffix-cache probe shows that context-derived n-gram drafting can provide large accepted-token opportunities on highly repetitive code-edit and templated RAG-copy sequences, but not on ordinary Gutenberg prose or shuffled controls.

## Why it stopped

Proxy-only useful signal with substantial prior-art overlap; not a full validation of speculative-decoding latency or novelty.

## Recommended next action

Stop paper work for this run; run a bounded real-model serving follow-up comparing existing n-gram/suffix decoding against no speculation on code-edit and RAG-copy workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Suffix-Cache Speculative Decoding on Copy-Heavy Workloads
- Success threshold: At least 1.3x median latency improvement on copy-heavy workloads with no statistically meaningful regression on prose/control workloads, plus acceptance metrics that explain the speedup.
- Stop condition: Stop if real serving overhead reduces copy-heavy median speedup below 1.1x or if prose/control workloads regress by more than 5% when the method is enabled.

## Evidence references

- Artifact root: `<local-path>/projects/context-derived-n-gram-suffix-cache-for-speculative-decoding-5c6ad57612e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
