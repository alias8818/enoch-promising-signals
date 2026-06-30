# Self-Speculative Decoding via Early Hidden State Prediction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-hidden-state-prediction-42cbec20c485`
Run ID: `self-speculative-decoding-via-early-hidden-state-prediction-42cbec20c485-20260605T081531081490+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29dd12b5c1cf

## What looked useful

Layer-1 ridge prediction reached 24.9% held-out final-argmax agreement versus 3.1% shuffled control, but the best simple speculative cost model was 0.983x before overheads. A near-final raw layer reached 48.2% agreement but costs about five sixths of transformer depth and still modeled below break-even.

## Boundaries and scale limits

Small local corpus, distilgpt2 only, CPU-only probing, no end-to-end decoder latency, no KV-cache implementation, no GPT-2-small-or-larger robustness, and only raw LM-head plus linear ridge hidden prediction heads.

## Claim scope

On a local distilgpt2 frozen-activation probe, early hidden states contain above-control information about the final next-token argmax, but simple raw or ridge early-hidden predictors do not reach a cost-model break-even point for greedy self-speculative decoding.

## Why it stopped

Proxy/early falsification: the directly tested simple early-hidden predictors show above-control signal but insufficient acceptance proxy for practical speedup under the bounded cost model; this is not a full validation or universal impossibility result.

## Recommended next action

Stop this run as a bounded useful negative signal; a separate follow-up should implement confidence-gated self-speculative decoding and require measured wall-clock speedup rather than proxy agreement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Early Hidden Self-Speculation on distilgpt2
- Success threshold: At least 1.05x sustained tokens/sec over baseline greedy decoding with identical greedy outputs on held-out prompts and acceptance above the measured break-even threshold after overheads.
- Stop condition: Stop if confidence gating cannot exceed 1.0x measured speedup on distilgpt2 after bounded implementation and calibration, or if exact greedy-output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-hidden-state-prediction-42cbec20c485`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
