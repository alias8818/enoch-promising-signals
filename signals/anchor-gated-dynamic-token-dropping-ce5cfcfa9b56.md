# Anchor-Gated Dynamic Token Dropping

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-dynamic-token-dropping-ce5cfcfa9b56`
Run ID: `anchor-gated-dynamic-token-dropping-ce5cfcfa9b56-20260525T152911606458+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccacb4f92101

## What looked useful

Anchor-gated dropping is promising only when anchors reliably identify local evidence; it is unsafe as a general token dropping strategy because accuracy collapsed on a control task whose label depended on distributed non-anchor evidence.

## Boundaries and scale limits

Tested only tiny 2-layer Transformer classifiers on synthetic data, with deterministic anchor-window pruning and proxy attention-cost metrics. No GPT-2-scale model, real corpus, learned gate, generation-quality metric, KV-cache-aware latency, or production memory measurement was run.

## Claim scope

In a synthetic Transformer classification benchmark where explicit anchor tokens localize all relevant evidence, deterministic anchor-window token dropping preserved or improved accuracy while keeping 6.2% of tokens and reducing the quadratic attention-cost proxy to 0.38% of dense. The same policy failed on a global-evidence control task.

## Why it stopped

Synthetic proxy evidence produced a useful scoped signal but is not publication-grade direct evidence; the global-evidence control also shows the method is not generally reliable.

## Recommended next action

Run a bounded GPT-2-small-class follow-up on real anchored formats such as JSON/XML/tool traces with dense, random, and non-anchor salience baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small anchor-gated dropping on real structured traces
- Success threshold: Retain at least 95% of dense accuracy or task score on anchor-local real inputs while dropping at least 50% of tokens, and avoid more than 5 percentage points of extra failure versus dense on the global-context control through detection or fallback.
- Stop condition: Stop if anchor-gated dropping underperforms random matched-drop at the same retained-token budget, loses more than 10 percentage points versus dense on anchor-local inputs, or cannot detect/fallback on global-context examples.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-dynamic-token-dropping-ce5cfcfa9b56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
