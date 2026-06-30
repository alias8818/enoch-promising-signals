# KV-Cache Prefix Matching for Zero-Compute Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-prefix-matching-for-zero-compute-speculation-a4a6ac2eee91`
Run ID: `kv-cache-prefix-matching-for-zero-compute-speculation-a4a6ac2eee91-20260524T165040936032+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04976dd3018e

## What looked useful

Exact prefix matching is workload-specific: with word/punctuation tokens and K=8, L=16 accepted tokens per position were 0.00060 for tiny_shakespeare and 0.00833 for Alice, but 0.53047 for CPython json decoder, 0.54304 for RFC 9110, and 2.64516 for synthetic logs. Blind skip is unsafe because eligible first-token mismatch rates were typically 8% to 40%; verification remains necessary.

## Boundaries and scale limits

No BPE tokenizer, no verifier model, no production serving benchmark, no KV tensor reuse validation, no approximate matching, and corpora capped at 200000 tokens per tokenizer stream. Speedup numbers are optimistic upper bounds from offline accepted-token counts and exclude lookup overhead, batching, memory pressure, and verifier latency.

## Claim scope

Offline exact-prefix trace benchmark over small public/plain-text corpora and controls: previous occurrence continuations can serve as zero-compute speculative drafts in repetitive structured, technical, and code-like streams, but exact long-prefix repeats are too rare to be broadly useful in narrative/open-ended text at this scale.

## Why it stopped

Proxy trace evidence supports a narrow mechanism but not a publication-grade or general KV-cache zero-compute speculation claim; production and model-side evidence are still missing.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded step is a real verifier-model prompt-lookup speculative decoding benchmark on repetitive technical/code/log workloads with BPE tokenization and wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-model benchmark for exact prefix lookup speculation on repetitive technical workloads
- Success threshold: At least 15% end-to-end verified decoding speedup on two repetitive technical/code/log workloads, less than 5% slowdown on narrative controls, exact output equality with verified decoding, and measured lookup memory overhead below 10% of verifier KV-cache memory for the tested context.
- Stop condition: Stop if accepted tokens per verifier pass remain below 0.2 or end-to-end speedup is below 5% on repetitive workloads after reasonable L/K tuning, because the offline trace signal does not translate to serving benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-prefix-matching-for-zero-compute-speculation-a4a6ac2eee91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
