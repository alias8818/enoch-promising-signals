# WAN-emulated adaptive error-feedback gradient compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `wan-emulated-adaptive-error-feedback-gradient-compression-621285000f`
Run ID: `wan-emulated-adaptive-error-feedback-gradient-compression-621285000f-20260608T130405226040+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gradient Compression for Volunteer Home Distributed Training: enoch://control-plane/projects/gradient-compression-for-volunteer-home-distributed-training-e42555ae870c/runs/gradient-compression-for-volunteer-home-distributed-training-e42555ae870c-20260608T063212286525+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

Residual pressure was a useful control signal: fixed 1% and 0.25% top-k EF saved more bytes but lost final accuracy and accumulated residual ratios of 8.8x and 25.5x, while adaptive EF kept residual ratio near 0.51x and reached 0.600/0.615 accuracy thresholds faster than dense in all tested WAN settings.

## Boundaries and scale limits

No real network stack, no multi-node collectives, no GPU communication overlap, no deep model, synthetic data only, 3 seeds, 160 steps, and an adaptive controller that settled at a conservative 25% payload.

## Claim scope

In a small local synthetic 8-worker logistic-regression training test with analytical WAN timing, residual-aware adaptive top-k error-feedback compression preserved dense-like final accuracy within 0.22 percentage points while reducing emulated WAN time by 1.06x to 1.25x, and it avoided the large residual buildup seen with aggressive fixed top-k compression.

## Why it stopped

Tier 1 local/synthetic evidence supports the mechanism but is not direct enough for a paper claim.

## Recommended next action

Run a bounded PyTorch multi-process follow-up on a public dataset using actual communication hooks or a network emulator, comparing dense, fixed top-k EF, and residual-aware adaptive EF on time-to-accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch network-emulated adaptive error-feedback compression on a real training workload
- Success threshold: Adaptive EF reaches the chosen validation-accuracy threshold in all seeds with at least 1.15x median wall-clock speedup versus dense and no more than 0.5 percentage point final accuracy loss, while fixed top-k either underperforms or requires a less efficient payload.
- Stop condition: Stop if adaptive EF fails to reach the dense validation threshold in 2 or more of 3 seeds, loses more than 1 percentage point final accuracy, or provides less than 1.05x median wall-clock speedup under the WAN emulator.

## Evidence references

- Artifact root: `<local-path>/projects/wan-emulated-adaptive-error-feedback-gradient-compression-621285000f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
