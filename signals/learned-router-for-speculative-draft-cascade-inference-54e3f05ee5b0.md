# Learned Router for Speculative Draft-Cascade Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-router-for-speculative-draft-cascade-inference-54e3f05ee5b0`
Run ID: `learned-router-for-speculative-draft-cascade-inference-54e3f05ee5b0-20260525T044921115956+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4fd1de6819f7

## What looked useful

Learned routing across draft sizes can be useful when context features predict acceptance and latency is calibrated, but the mechanism is brittle to deployment cost shifts. Future work should make the router explicitly cost-calibrated before real-model validation.

## Boundaries and scale limits

Evidence is synthetic and trace-level only. It does not include real transformer logits, measured GPU latency, batching effects, KV-cache behavior, or online serving adaptation. A latency-miscalibration stress case reversed the gain, with learned routing losing about 6.1% relative to the static-small baseline.

## Claim scope

In controlled synthetic speculative-decoding traces with stable draft costs, a NumPy-trained contextual router improves expected verified tokens per unit cost over static-best and tuned entropy-threshold draft selection by about 1.0% to 2.8% relative, while recovering most of the contextual oracle benefit.

## Why it stopped

Synthetic trace evidence is useful but not direct end-to-end inference evidence, and the latency-miscalibration stress test shows a practical failure mode.

## Recommended next action

Run a bounded real-trace replay using small target/draft language models with measured draft latencies and an online cost-calibrated router; do not write a paper from the current synthetic-only evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace cost-calibrated router replay for speculative draft cascades
- Success threshold: Learned cost-calibrated routing improves measured or replayed tokens per second by at least 3% over the best non-learned baseline with a paired confidence interval excluding zero, and does not underperform static-best under a predefined latency-shift stress case.
- Stop condition: Stop if real-trace replay shows less than 1% gain over static-best or any statistically clear regression under latency shift after cost calibration.

## Evidence references

- Artifact root: `<local-path>/projects/learned-router-for-speculative-draft-cascade-inference-54e3f05ee5b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
