# Context-local n-gram table as zero-VRAM draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-local-n-gram-table-as-zero-vram-draft-model-b3b607fb5926`
Run ID: `context-local-n-gram-table-as-zero-vram-draft-model-b3b607fb5926-20260529T082151046947+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/38987278d1af

## What looked useful

The mechanism is supported for repetitive local contexts: with a 256-token window on a repetitive protocol file, mean accepted prefix was 6.45 of 8 tokens and full-span hit rate was 70%. On natural regex-token text, context n-gram mean accepted prefix was 0.60 on Alice and 0.425 on Shakespeare at context 1024, with full 8-token hit rates below 0.6% and 11-13 ms mean CPU draft latency. Recent-match copying achieved similar acceptance at much lower latency.

## Boundaries and scale limits

No target LLM, production tokenizer, or end-to-end speculative decoder was run. Corpora were small, sampled locally, and CPU-only. Byte-token results are sensitivity checks, not LLM-token evidence. The implementation rebuilds the table per position rather than using an optimized incremental index.

## Claim scope

Bounded exact-match proxy over two small natural-text corpora and one repetitive protocol-like synthetic corpus: a context-local n-gram table can draft useful spans when repeated structure is present in the active context, but natural-prose regex-token acceptance is modest and naive table rebuild cost is high.

## Why it stopped

Proxy evidence supports a narrow mechanism but not a broad serving claim; natural-token acceptance is modest and naive CPU overhead is too high for a paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate an optimized recent-match/context n-gram drafter with a real small target model and tokenizer and measure end-to-end speculative decoding speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model speculative decoding with optimized context-copy drafter
- Success threshold: At least 1.2x end-to-end tokens/sec improvement over no speculation on repetitive workloads, less than 5% slowdown on natural prose, zero draft-model VRAM, and CPU draft overhead below the saved target-verification time.
- Stop condition: Stop if optimized context-copy acceptance remains below 0.5 mean accepted target tokens or end-to-end throughput is not improved after accounting for CPU overhead.

## Evidence references

- Artifact root: `<local-path>/projects/context-local-n-gram-table-as-zero-vram-draft-model-b3b607fb5926`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
