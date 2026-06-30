# Anchor-Indexed KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-compression-for-long-context-a616343ff454`
Run ID: `anchor-indexed-kv-compression-for-long-context-a616343ff454-20260601T085950794982+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51f0628e9d71

## What looked useful

Anchor indexing produced a bounded positive mechanism signal in synthetic retrieval: in the main sweep it beat the strongest non-anchor baseline in 300/400 cells with mean absolute accuracy delta +0.0735, but sensitivity sweeps showed the advantage disappears or reverses when records cost about two KV-token equivalents or false anchors are too frequent.

## Boundaries and scale limits

No real transformer KV cache was modified; no language-model perplexity, downstream QA, needle-in-haystack, throughput, or GPU serving measurements were collected. Evidence is limited to vectorized CPU simulations up to 32768 context tokens, 1024 synthetic facts, and 10000 retrieval trials per condition.

## Claim scope

Synthetic associative-retrieval benchmark only: compact anchor-indexed records preserved long-range keyed facts better than sliding-window, random-token, random-pair, and noisy salience-token cache retention when anchor records cost 1.25-1.5 KV-token equivalents and false-anchor rates were moderate.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal and explicit failure boundaries, but not direct model-level evidence for a long-context KV compression claim.

## Recommended next action

Run a bounded direct follow-up that implements anchor-indexed KV records in a tiny decoder-only transformer and compares equal-memory retrieval accuracy, perplexity, and decode throughput against sliding-window and salience eviction baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Decoder Anchor-Indexed KV Cache Validation
- Success threshold: At least +5 absolute retrieval-accuracy points over the strongest compressed baseline at equal KV memory in two or more context lengths, no perplexity regression larger than 5% on the synthetic validation set, and decode throughput at least 80% of the fastest compressed baseline.
- Stop condition: Stop as negative if anchor indexing fails to beat the strongest equal-memory compressed baseline by 5 absolute accuracy points, if throughput falls below 80% of baseline, or if the required record size approaches raw key/value pair cost.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-for-long-context-a616343ff454`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
