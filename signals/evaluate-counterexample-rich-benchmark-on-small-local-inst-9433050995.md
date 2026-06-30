# Evaluate counterexample-rich benchmark on small local instruct models with matched controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evaluate-counterexample-rich-benchmark-on-small-local-inst-9433050995`
Run ID: `evaluate-counterexample-rich-benchmark-on-small-local-inst-9433050995-20260613T224215006240+0000`

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

- Parent run decision: Counterexample-Rich Reliability Benchmark for Small Local Agents: enoch://control-plane/projects/counterexample-rich-reliability-benchmark-for-small-local-agents-b8824552a7dd/runs/counterexample-rich-reliability-benchmark-for-small-local-agents-b8824552a7dd-20260613T222035029921+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffdbb53a6b0a

## What looked useful

Matched controls had 100% accuracy for both models. Counterexample accuracy fell to 75.0% for Phi-4-mini but only 91.7% for Qwen2.5-7B, so the preregistered both-model 15 pp penalty threshold was not met. Misses concentrated in default-overriding counterexamples.

## Boundaries and scale limits

Only two local quantized instruct models, 12 matched pairs per model, CPU-only llama.cpp execution, one deterministic decoding setting, synthetic multiple-choice items, no bootstrap confidence intervals or larger benchmark audit.

## Claim scope

A 12-pair matched synthetic counterexample benchmark showed a large counterexample penalty for Phi-4-mini-instruct-Q4 but not for Qwen2.5-7B-Instruct-Q4 under deterministic local llama.cpp inference.

## Why it stopped

Direct Tier 1 test completed, but the stated threshold failed because Qwen2.5-7B showed only an 8.3 pp counterexample penalty.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, build a larger harder audited matched-pair benchmark and require at least a 15 pp counterexample penalty with confidence intervals across three or more small local instruct models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder audited counterexample benchmark across small local instruct models
- Success threshold: Each tested model has counterexample accuracy at least 15 percentage points below matched controls, and the bootstrap 95% confidence interval for the aggregate penalty excludes 0.
- Stop condition: Stop if a stronger 7B-class model remains below a 10 percentage point penalty after 50 audited pairs, because the current benchmark mechanism would not be robust enough for the proposed claim.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-counterexample-rich-benchmark-on-small-local-inst-9433050995`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
