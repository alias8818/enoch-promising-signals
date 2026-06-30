# Sliding Context Window with Anchor Checkpoints on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-context-window-with-anchor-checkpoints-on-cpu-9273e79db84f`
Run ID: `sliding-context-window-with-anchor-checkpoints-on-cpu-9273e79db84f-20260523T103355378821+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8e30b7823e28

## What looked useful

Oracle/salient anchors matched full attention at 100% old-fact retrieval accuracy while sliding-window attention scored 0%; naive mean-pooled anchors scored only 3.75%, identifying checkpoint construction as the hard part. At 32768 tokens, window+stride-256 anchors scanned 384 candidates versus 32768 full keys, giving a 167x last-token scan speedup proxy and 85.3x score-memory proxy reduction.

## Boundaries and scale limits

Tested only synthetic retrieval up to 2048 tokens for accuracy and last-token scan timing up to 32768 tokens on one CPU process; no learned checkpoint creation, transformer training, real language modeling, multi-head attention, batched decode, or end-to-end KV-cache benchmark was tested.

## Claim scope

A dependency-free CPU synthetic retrieval and last-token attention-scan benchmark shows that recent-window attention plus sparse salient/oracle anchor checkpoints can recover old synthetic facts outside the sliding window while reducing candidate key scans and score-vector memory versus full attention.

## Why it stopped

The positive result is mechanism/proxy evidence with oracle anchors, and the simple automatic mean-anchor control failed; this is insufficient for a paper or broad viability claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement learned or deterministic non-oracle anchor selection in a tiny transformer and compare against full and sliding-window baselines on synthetic plus small text retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Anchor Checkpoints for Sliding-Window Tiny Transformers
- Success threshold: Learned or deterministic non-oracle anchors recover at least 80% of full-attention old-fact accuracy, exceed sliding-window accuracy by at least 30 percentage points, and keep end-to-end CPU decode latency or key-scan work at least 2x lower than full attention at the tested context length.
- Stop condition: Stop if non-oracle anchors fail to beat mean anchors by at least 10 percentage points or if anchor construction overhead removes the CPU efficiency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-context-window-with-anchor-checkpoints-on-cpu-9273e79db84f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
