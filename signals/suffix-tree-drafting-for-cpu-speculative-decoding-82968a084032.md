# Suffix-Tree Drafting for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-drafting-for-cpu-speculative-decoding-82968a084032`
Run ID: `suffix-tree-drafting-for-cpu-speculative-decoding-82968a084032-20260629T022852023837+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed5246c3b5cb

## What looked useful

Suffix-index drafting is workload-dependent: it gives high modeled verifier-call reduction on repetitive spans and near-zero gain on low-repetition streams, but its measured advantage over n-gram-mode drafting was within about +/-0.002 modeled call reduction while lookup cost increased with longer contexts.

## Boundaries and scale limits

CPU-only proxy replay over synthetic boilerplate, templated chat, low-repetition random tokens, and repeated local project documents; no live neural verifier, KV-cache measurement, batching, sampling correction, or production decoder integration.

## Claim scope

In deterministic online token-trace replay, suffix-index copy drafting reduces modeled verifier calls on repetitive traces but does not materially outperform a simpler online n-gram-mode drafting baseline.

## Why it stopped

Bounded proxy evidence supports the copy-drafting mechanism on repetitive traces, but early falsifies the stronger suffix-tree advantage claim because the suffix-index variant did not beat the simpler n-gram baseline in modeled call reduction.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should integrate suffix-index and n-gram-mode drafters into a real CPU decoder and require a wall-clock tokens/s win over the n-gram baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU decoder comparison for suffix-index versus n-gram speculative drafting
- Success threshold: Suffix-index drafting improves end-to-end CPU tokens/s by at least 5% over n-gram-mode drafting on repetitive workloads without regressing the low-repetition control by more than 2%.
- Stop condition: Stop if suffix-index tokens/s is at or below n-gram-mode tokens/s on the repetitive workload, or if drafter lookup overhead consumes the verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafting-for-cpu-speculative-decoding-82968a084032`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
