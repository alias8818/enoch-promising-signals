# Anchor-Compressed Long-Context Memory State for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-compressed-long-context-memory-state-for-cpu-inference-7237c2bb5cf3`
Run ID: `anchor-compressed-long-context-memory-state-for-cpu-inference-7237c2bb5cf3-20260607T080900125457+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/240bf78d3f82

## What looked useful

Mean anchors achieved 21.56x state-byte compression at 16384 tokens and recovered stale-topic ideal cosine 0.222 versus sliding-window -0.022, but exact retrieval target cosine remained near zero (0.011) versus full attention 1.000. Smaller blocks improved stale-topic fidelity at lower compression: 8192-token block 16 reached 0.438 ideal cosine at 8.26x compression.

## Boundaries and scale limits

Tested only model-free synthetic attention states up to 16384 tokens, dim 128, one CPU process, fixed recent window 512, and mean-pooled anchors. No real transformer, learned anchors, tokenizer, perplexity, generation quality, or production CPU serving stack was evaluated.

## Claim scope

In a synthetic NumPy CPU attention probe, simple mean-pooled anchor states reduce KV-like state size and scan time and preserve some stale aggregate/topic information, but they fail exact long-range key retrieval.

## Why it stopped

Synthetic proxy evidence supports aggregate-memory savings but early-falsifies simple mean-pooled anchors as a general long-context KV replacement; no real LLM inference validation was performed.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement learned or multi-anchor retention in a tiny transformer and require both stale aggregate recall improvement over sliding window and nonzero exact-retrieval preservation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Multi-Anchor KV Compression in a Tiny Transformer
- Success threshold: At 8192+ token contexts, learned or multi-anchor compression must retain at least 8x state-byte reduction, improve exact retrieval by at least 0.20 absolute over mean anchors, and preserve stale aggregate recall within 0.10 cosine of full attention.
- Stop condition: Stop if exact retrieval remains within 0.05 absolute of mean-anchor failure or if CPU latency/memory savings fall below 4x versus full KV at the tested context length.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-compressed-long-context-memory-state-for-cpu-inference-7237c2bb5cf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
