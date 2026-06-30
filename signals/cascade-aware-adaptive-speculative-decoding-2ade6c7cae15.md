# Cascade-Aware Adaptive Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-aware-adaptive-speculative-decoding-2ade6c7cae15`
Run ID: `cascade-aware-adaptive-speculative-decoding-2ade6c7cae15-20260525T060021294575+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/db3d7bb517ac

## What looked useful

Across 40 replicates at 50k emitted tokens per replicate with draft_cost=0.08, HMM cascade control was neutral on iid/choppy traces (+0.11%/+0.09% vs best static), slight on mild cascades (+0.46%), and positive on strong persistent cascades (+9.88%); the simple streak cascade heuristic was negative in all regimes.

## Boundaries and scale limits

No real target/draft model logits, no real serving latency, no verifier batching or KV-cache measurement, no stochastic quality-preserving acceptance, and no large-model or production workload validation were run.

## Claim scope

Synthetic speculative-decoding cost-model evidence shows that HMM-style cascade belief tracking improves modeled throughput over the best fixed draft length only when acceptance probabilities have persistent easy/hard states; naive full-accept streak adaptation is not sufficient.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic/proxy only, not direct model-serving validation.

## Recommended next action

Run a bounded real-logit replay using a small target/draft model pair and fixed prompt suite; stop if real acceptance traces do not show enough persistence for HMM cascade control to beat tuned static gamma by at least 5% in measured latency or cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Logit Replay for Cascade-Aware Speculative Gamma Control
- Success threshold: HMM cascade control improves measured latency or modeled verifier cost by at least 5% over best tuned static gamma on real-logit replay without increasing output divergence under the chosen acceptance rule.
- Stop condition: Stop as negative if acceptance persistence is weak or HMM cascade control fails to beat best static gamma by 5% on the real-logit replay.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-aware-adaptive-speculative-decoding-2ade6c7cae15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
