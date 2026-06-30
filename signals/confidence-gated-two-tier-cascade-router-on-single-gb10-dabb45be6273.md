# Confidence-Gated Two-Tier Cascade Router on Single GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-two-tier-cascade-router-on-single-gb10-dabb45be6273`
Run ID: `confidence-gated-two-tier-cascade-router-on-single-gb10-dabb45be6273-20260620T124602821216+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2b1df03f253

## What looked useful

A low threshold routed 7.9% of examples to tier two and achieved 0.8394 mean accuracy versus 0.8390 all-small and 0.8261 all-large, using 8.5% of the all-large linear-layer compute proxy and 0.1287 ms versus 0.5999 ms all-large latency. Higher thresholds routed more examples but degraded accuracy toward the weaker tier-two baseline.

## Boundaries and scale limits

Synthetic data only; three seeds; small MLP/large MLP proxy rather than LLM serving; no real workload, calibrated router, production batching, token lengths, or SLA/cost model.

## Claim scope

On one synthetic multiclass GPU probe, max-softmax confidence gating produced a clear cost/latency tradeoff and a tiny best-threshold accuracy gain over all-small, but it did not validate the intended stronger-second-tier cascade because the large tier underperformed the small tier overall in the main run.

## Why it stopped

No-paper proxy closure: the synthetic GB10 probe produced a useful routing diagnostic, but the main evidence is mixed and the stronger second-tier premise failed, so it is not a full validation.

## Recommended next action

Run a bounded direct follow-up on a real public classification or QA workload with a verified stronger tier-two model and validation-set threshold calibration; stop if routed-slice accuracy is not higher for tier two than tier one.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validated confidence-gated cascade on a real workload with a stronger second tier
- Success threshold: On held-out test data, cascade accuracy is at least 98% of all-tier-two accuracy while routing no more than 50% of examples to tier two and beating all-small accuracy by at least 1 percentage point.
- Stop condition: Stop as negative if tier two does not beat tier one on the validation low-confidence slice or if the calibrated cascade cannot beat all-small without routing more than 50% of examples.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-two-tier-cascade-router-on-single-gb10-dabb45be6273`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
