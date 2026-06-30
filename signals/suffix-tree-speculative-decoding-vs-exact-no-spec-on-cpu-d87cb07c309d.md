# Suffix-Tree Speculative Decoding vs Exact No-Spec on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-vs-exact-no-spec-on-cpu-d87cb07c309d`
Run ID: `suffix-tree-speculative-decoding-vs-exact-no-spec-on-cpu-d87cb07c309d-20260619T233404409503+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Suffix-index speculation is promising when exact verifier calls are expensive enough to amortize lookup and batch verification overhead, but it is slower than no-spec when the verifier is cheap.

## Boundaries and scale limits

No real transformer, KV cache, production suffix tree, real prompt trace, or datacenter-scale serving workload was tested. Medium run was 24 tasks per domain and 3072 generated tokens per domain.

## Claim scope

Synthetic CPU n-gram verifier with exact greedy decoding: suffix-index speculative proposals preserved identical outputs and reduced verifier calls to about 15% of baseline; wall-clock speedup appeared only when verifier calls had nontrivial CPU work.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy and mixed: exactness and verifier-call reduction are supported, but practical CPU speedup depends on verifier cost.

## Recommended next action

Run a bounded real-transformer CPU follow-up using a small cached transformer verifier and the same exactness, acceptance, verifier-call, and wall-clock metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer CPU verifier test for suffix-index speculative decoding
- Success threshold: At least 1.2x median tokens/s speedup with exact output equality and at least 50% draft-token acceptance on an overlap-heavy trace; no worse than 0.9x on the negative control.
- Stop condition: Stop if exactness fails, if acceptance stays below 30% on overlap-heavy prompts, or if median throughput remains below 1.0x after tuning draft length and suffix context.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-vs-exact-no-spec-on-cpu-d87cb07c309d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
