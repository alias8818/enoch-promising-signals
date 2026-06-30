# Learned anchor selection for exact-anchor interleaved KV compression in a small decoder

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-anchor-selection-for-exact-anchor-interleaved-kv-c-67455381c0`
Run ID: `learned-anchor-selection-for-exact-anchor-interleaved-kv-c-67455381c0-20260524T065052895262+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Anchor-Gated KV Compression: Exact Anchors with Interleaved Compressed State: enoch://control-plane/projects/anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c/runs/anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c-20260524T062932842792+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/81f1d9eb3e82

## What looked useful

Across three seeds, dense accuracy was 0.9999 mean, learned@2 accuracy was 0.9831 mean with 100% true-anchor retention, while recent@2/uniform@2/random@2 accuracies were 0.0668/0.0636/0.1041. This supports the mechanism that learned exact-anchor selection can preserve decoder behavior when the useful anchor is sparse and non-recent.

## Boundaries and scale limits

Synthetic task only; small decoder only; final-query compressed attention only; no natural language corpus, real long-context serving trace, end-to-end NLL-trained selector, latency kernel, or GPT-2-small-class validation.

## Claim scope

In a controlled synthetic anchor-copy task with a 2-layer small decoder, a supervised learned selector can retain exact KV anchors that preserve most dense final-query accuracy at small cache budgets and substantially outperform same-budget recent, uniform, and random retention policies.

## Why it stopped

Tier 1 direct controlled test produced a useful mechanism signal but not paper-ready evidence; closure is no-paper because claims remain synthetic and small-scale.

## Recommended next action

Run a bounded deepen follow-up that trains a budget-aware selector from downstream compressed NLL on a less explicitly marked synthetic or small real-text retrieval task, and stop if learned anchors fail to beat oracle-informed heuristics or same-budget saliency controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-aware learned anchor selection from compressed decoder loss
- Success threshold: At two or more cache budgets, learned budget-aware selection must improve compressed NLL by at least 25% relative to the best non-oracle heuristic and keep task accuracy within 5 percentage points of dense accuracy on held-out sequences.
- Stop condition: Stop as negative if learned selection does not beat the best non-oracle heuristic on held-out NLL, if gains vanish when explicit marker labels are removed, or if larger budgets consistently degrade more than smaller budgets without a correctable calibration mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/learned-anchor-selection-for-exact-anchor-interleaved-kv-c-67455381c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
