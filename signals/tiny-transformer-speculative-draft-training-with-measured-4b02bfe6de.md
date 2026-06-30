# Tiny Transformer Speculative Draft Training with Measured Timing-Floor Anti-Cheat

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-transformer-speculative-draft-training-with-measured-4b02bfe6de`
Run ID: `tiny-transformer-speculative-draft-training-with-measured-4b02bfe6de-20260610T233551342566+0000`

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

- Parent run decision: Speculative Draft Model Training with Timing-Floor Anti-Cheat: enoch://control-plane/projects/speculative-draft-model-training-with-timing-floor-anti-cheat-5dbff1d50a89/runs/speculative-draft-model-training-with-timing-floor-anti-cheat-5dbff1d50a89-20260610T230849650313+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

The trained draft reached 0.873 validation argmax match to the frozen target and improved speculative acceptance over random draft control (0.273 vs 0.0006), but anti-cheat-adjusted throughput was only 0.646x target-only, below the 1.05x threshold. The validation-to-rollout gap suggests offline distillation alone is insufficient for this setup.

## Boundaries and scale limits

Synthetic data, greedy decoding, CPU timing, one seed, tiny weakly trained target, no GPT-2-small-class baseline, no real text, no GPU serving stack, and no stochastic speculative sampling.

## Claim scope

In a CPU Tier 1 controlled small test with a 118k-parameter frozen tiny transformer target and a 22k-parameter trained draft on synthetic sequences, offline draft distillation improved validation argmax match and beat a random draft control but failed the measured timing-floor speculative decoding success threshold.

## Why it stopped

Direct small controlled test failed both explicit thresholds: trained draft acceptance 0.273 < 0.45 and anti-cheat-adjusted speedup 0.646x < 1.05x. This is an early small-scale falsification, not a full validation or universal negative.

## Recommended next action

Stop this run as a no-paper Tier 1 useful signal; if continuing the line, run a bounded on-policy draft-training follow-up that directly targets rollout acceptance under the same timing-floor accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: On-policy tiny draft training for timing-floor speculative decoding
- Success threshold: On-policy draft achieves acceptance >= 0.45 and anti-cheat-adjusted speedup >= 1.05x versus target-only, while beating the offline-distilled draft on both metrics.
- Stop condition: Stop if on-policy training still yields acceptance < 0.45 or adjusted speedup < 1.05x under the same timing-floor accounting, or if gains only appear without the timing floor.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-speculative-draft-training-with-measured-4b02bfe6de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
