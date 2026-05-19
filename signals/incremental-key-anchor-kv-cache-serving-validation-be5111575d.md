# Incremental Key-Anchor KV Cache Serving Validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `incremental-key-anchor-kv-cache-serving-validation-be5111575d`
Run ID: `incremental-key-anchor-kv-cache-serving-validation-be5111575d-20260518T043303562296+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Incremental Key-Anchor KV Cache Serving Validation: internal_generated:incremental-key-anchor-kv-cache-serving-validation-be5111575d

## What looked useful

Key-anchor can preserve repeated old anchors better than random or periodic old-token controls, but it gives only small gains over sliding window in anchor/mixed regimes and can be much worse on adversarial long-range traces. At long context and small cache fractions, output error remains high even when target-hit rate is high.

## Boundaries and scale limits

No pretrained LLM serving integration, no production batching, no real prompt/task benchmark, and no kernel-level paged-cache measurement. Synthetic traces directly test attention/cache policy behavior but do not establish downstream generation quality or deployment throughput.

## Claim scope

Online key-anchor KV-cache retention was evaluated in a deterministic synthetic attention serving benchmark up to 4096 tokens, five fixed seeds, three cache budgets, four trace regimes, and five baselines/controls. It shows a bounded mechanism signal on repeated-anchor traces but not robust paper-ready superiority.

## Why it stopped

Tier 4 paper-readiness is unsupported: the direct synthetic benchmark found mixed mechanism support but robustness failures against a simple sliding-window baseline, and the evidence lacks real-model serving validation.

## Recommended next action

Stop this depth-4 follow-up chain and archive the benchmark as no-paper robustness evidence; do not recommend another deepen/retry follow-up under the controller depth cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/incremental-key-anchor-kv-cache-serving-validation-be5111575d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
