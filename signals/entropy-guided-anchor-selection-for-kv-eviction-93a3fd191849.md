# Entropy-Guided Anchor Selection for KV Eviction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `entropy-guided-anchor-selection-for-kv-eviction-93a3fd191849`
Run ID: `entropy-guided-anchor-selection-for-kv-eviction-93a3fd191849-20260525T031752159909+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94d9ebb9dd35

## What looked useful

In controlled traces, direct low-entropy attention weighting did not outperform cumulative attention and was consistently below recency on retained attention mass. A contrastive entropy variant produced only a narrow budget-32 neutral-case win that did not persist at budget 64.

## Boundaries and scale limits

No real transformer serving, perplexity, latency, memory-pressure, layer/head, or eviction-feedback validation was run. Results are proxy evidence only and should not be interpreted as full long-context model validation.

## Claim scope

Synthetic counterfactual attention-trace KV eviction with fixed budgets 32 and 64, sequence length 4096, 64 trials per scenario, hybrid recent-window plus old-anchor cache policies.

## Why it stopped

Proxy synthetic evidence does not support entropy-guided anchor selection as a robust KV eviction improvement over recency or cumulative-attention baselines.

## Recommended next action

Stop this run as a proxy early falsification; if deepening is desired, test the same policies on GPT-2-small-class real attention traces with quality and retained-mass metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small Attention-Trace Test for Entropy-Guided KV Anchors
- Success threshold: Entropy-guided policy beats both recency and cumulative-attention baselines by at least 3% on long-range retained attention or retrieval accuracy while losing no more than 1% total retained attention mass.
- Stop condition: Stop if entropy-guided policies fail to beat both baselines on two independent real-trace datasets or if the measured gain appears only under synthetic/proxy scoring without a direct quality improvement.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-guided-anchor-selection-for-kv-eviction-93a3fd191849`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
