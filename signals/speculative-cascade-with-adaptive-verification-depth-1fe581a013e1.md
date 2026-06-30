# Speculative Cascade with Adaptive Verification Depth

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-cascade-with-adaptive-verification-depth-1fe581a013e1`
Run ID: `speculative-cascade-with-adaptive-verification-depth-1fe581a013e1-20260628T082135346207+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1e1b24b469b9

## What looked useful

Adaptive verification depth won in 12/12 simulated noise/schedule conditions, with relative speedup over best fixed K from 12.35% to 21.87% and mean 17.16%; the benefit decreased as predictor noise increased.

## Boundaries and scale limits

Proxy-only CPU simulation: no real LLM logits, no measured GPU latency, no batching/KV-cache effects, no implementation overhead, and no full model-serving validation. Existing public work already covers broad adaptive speculative decoding and cascade scheduling.

## Claim scope

In a synthetic speculative-decoding cascade simulator with heterogeneous context difficulty, noisy acceptance predictors, and correction-style acceptance-prefix accounting, adaptive verification depth improved cost-normalized throughput over the ex-post best fixed verification depth across all tested settings.

## Why it stopped

The result is a proxy/synthetic useful signal rather than full validation, and broad novelty is weakened by existing adaptive speculative decoding and cascade literature.

## Recommended next action

Stop this run as no-paper useful simulator evidence; the concrete next action is a bounded direct validation on real small draft/target model pairs with measured latency and the same best-fixed-K control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model adaptive verification depth validation
- Success threshold: Adaptive policy improves measured tokens/second by at least 8% over ex-post best fixed K on both model pairs while preserving exact speculative decoding correction semantics.
- Stop condition: Stop as unsupported if adaptive improves less than 3% over best fixed K or if policy overhead erases simulated gains on either model pair.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-cascade-with-adaptive-verification-depth-1fe581a013e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
