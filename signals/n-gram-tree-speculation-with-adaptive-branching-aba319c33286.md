# N-gram Tree Speculation with Adaptive Branching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-tree-speculation-with-adaptive-branching-aba319c33286`
Run ID: `n-gram-tree-speculation-with-adaptive-branching-aba319c33286-20260530T034111092206+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8ab10a9b95e

## What looked useful

Adaptive n-gram tree speculation is not inert, but in this bounded proxy it buys only about 2.0-2.3% fewer target calls versus greedy and is dominated or matched by fixed-width controls depending on whether node cost or call reduction is prioritized.

## Boundaries and scale limits

No transformer target model, GPU tree-attention kernel, tokenizer-matched LM distribution, KV-cache behavior, or wall-clock decoder benchmark was tested. Runs were CPU-only proxy simulations over up to 50,000 held-out emitted tokens per configuration.

## Claim scope

On a 262,927-token Tiny Shakespeare word-token proxy with n-gram proposal trees, adaptive branching modestly improves held-out target-token coverage over greedy speculation but does not beat simple fixed-width controls on target-call reduction, and its draft-node cost is high.

## Why it stopped

Proxy/early falsification of the strong adaptive-branching efficiency claim: adaptive improved over greedy but did not outperform simple fixed-width controls and required many extra draft-tree nodes per extra accepted token.

## Recommended next action

Stop this run as no-paper proxy evidence; only continue via a bounded direct small-LM wall-clock benchmark against greedy and fixed-width tree controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM wall-clock validation of adaptive n-gram tree speculation
- Success threshold: Adaptive branching must improve end-to-end wall-clock tokens/sec by at least 10% over the best fixed-width control while preserving the same target outputs or an equivalent quality metric.
- Stop condition: Stop if adaptive branching fails to beat the best fixed-width control on wall-clock throughput in two tokenizer/model settings or if tree construction overhead exceeds the saved target verification time.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-tree-speculation-with-adaptive-branching-aba319c33286`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
