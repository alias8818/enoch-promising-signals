# Residual-Channel-Gated KV Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-gated-kv-eviction-for-long-context-63f2d38b8e90`
Run ID: `residual-channel-gated-kv-eviction-for-long-context-63f2d38b8e90-20260602T142430688716+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ff39959f5956

## What looked useful

Residual-channel-gated eviction is conditionally useful: in aligned synthetic scenarios it reached 1.000 target hit rate at 2% cache budget versus 0.962 for a noisy past-attention proxy, but retained attention mass was only comparable rather than clearly better. Without residual signal, standalone gating fell to 0.022 target hit rate at 2% budget; with misleading signal it reached only 0.047 and degraded a hybrid score to 0.787 versus 0.962 for past attention.

## Boundaries and scale limits

No trained language model was evaluated. No real residual channels were discovered from model activations. No downstream perplexity, retrieval accuracy, latency, multi-layer/head, or production serving metrics were measured. Evidence is proxy-only and should not be treated as long-context model validation.

## Claim scope

Synthetic controlled KV-cache retention probe with 8,192-token caches, known future query targets, and residual-channel alignment/misalignment controls. Residual-channel gating preserved all synthetic retrieval targets when gate channels were aligned with future relevance, but failed near-randomly or harmfully when the residual signal was absent or misleading.

## Why it stopped

Synthetic proxy evidence supports the mechanism only under known channel alignment and directly exposes brittleness when channels are absent or misleading; this is not full validation of residual-channel-gated KV eviction.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded trained-small-transformer associative retrieval test that selects residual channels without future-target leakage and compares residual-gated eviction against attention and recency baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Small-Transformer Residual Channel KV Eviction Probe
- Success threshold: Residual-gated or attention-plus-residual eviction improves held-out retrieval accuracy by at least 5 percentage points over attention-history eviction at one or more severe cache budgets without a shuffled-channel control showing the same gain.
- Stop condition: Stop if selected real residual channels do not outperform shuffled channels or if attention-history eviction matches/exceeds the residual hybrid across all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-gated-kv-eviction-for-long-context-63f2d38b8e90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
