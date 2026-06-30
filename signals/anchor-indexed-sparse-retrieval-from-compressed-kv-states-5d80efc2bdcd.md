# Anchor-Indexed Sparse Retrieval from Compressed KV States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-sparse-retrieval-from-compressed-kv-states-5d80efc2bdcd`
Run ID: `anchor-indexed-sparse-retrieval-from-compressed-kv-states-5d80efc2bdcd-20260524T223630990957+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/500874881783

## What looked useful

Across 27 robustness runs over seeds, compressed dimensions, and anchor budgets, salience anchors averaged 0.641 dense top-1 match versus 0.157 for compressed-only and 0.221 for random anchors; mean output-cosine gains were +0.455 over compressed-only and +0.363 over random anchors. A 500-trial uniform-target control reduced salience-anchor top-1 to 0.208 versus 0.218 for random anchors, identifying anchor selection as the key condition.

## Boundaries and scale limits

Evidence is synthetic and mechanism-level only. It does not include real transformer K/V traces, learned salience, end-to-end language-model perplexity or QA accuracy, production latency, or GPU kernel measurements. The uniform-target control shows no advantage over random anchors when target demand is independent of salience.

## Claim scope

In synthetic dense-attention retrieval with 64-dimensional K/V states compressed to 4/8/16 dimensions plus 4-bit value quantization, a small exact anchor table selected by a salience signal recovers dense-attention top-1 matches substantially better than compressed-only retrieval and same-budget random anchors when future targets are correlated with salience.

## Why it stopped

Closed as no-paper useful signal because the current result is synthetic/proxy evidence; it supports the mechanism under salience-correlated demand but does not validate real transformer behavior or end-to-end model quality.

## Recommended next action

Run a bounded real-KV-trace follow-up using a GPT-2-small-class model: record attention caches on a long-context retrieval task, choose anchors from model-observable salience signals, and compare dense KV, quantized KV, random anchors, recency/block anchors, and salience anchors on retrieval accuracy plus cache memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer KV Trace Validation for Salience-Indexed Exact Anchors
- Success threshold: At matched cache memory, salience anchors improve attention target recall by at least 10 percentage points over the best non-salience sparse baseline and improve or preserve end-task retrieval accuracy relative to compressed/quantized KV.
- Stop condition: Stop if salience anchors fail to beat random or recency/block anchors by at least 5 percentage points in target recall on real traces, or if any recall gains disappear in end-task accuracy at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-sparse-retrieval-from-compressed-kv-states-5d80efc2bdcd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
