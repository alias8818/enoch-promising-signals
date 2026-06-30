# Capability-Masked Agent Policy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `capability-masked-agent-policy-53fa446a6807`
Run ID: `capability-masked-agent-policy-53fa446a6807-20260605T030714104835+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/96acb1bd8a94

## What looked useful

Runtime capability awareness is necessary in the benchmark: the unmasked policy's invalid tool-call rate rises from 19.9% in-distribution to 88.9% under very sparse availability. However, both mask-input-only and inference-hard-mask-only controls match the full capability-masked policy at 100% accuracy, 0% invalid calls, and reward 1.0 across five seeds.

## Boundaries and scale limits

Synthetic contextual classification only; no real LLM agent traces, no multi-step planning, no noisy or stale masks, no long-horizon tool execution, and no large-model training.

## Claim scope

In a synthetic single-step tool-routing benchmark with runtime availability masks, capability information eliminates invalid tool calls, but the full training-time capability-masked policy does not outperform simpler mask-input-only or inference-hard-mask controls.

## Why it stopped

Bounded synthetic evidence supports capability awareness but does not support a differentiated capability-masked policy contribution over simpler controls.

## Recommended next action

Stop this as a no-paper useful signal; any next test should use a harder multi-step or noisy-mask environment that can distinguish training-time capability masking from simple inference-time hard masking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Multi-Step Capability-Mask Agent Benchmark
- Success threshold: Full capability-masked policy improves mean reward by at least 5% absolute or reduces invalid/recovery failures by at least 25% relative versus both simpler mask controls under noisy-mask evaluation.
- Stop condition: Stop if the full policy fails to beat both simpler controls on reward or invalid/recovery failures after five seeded runs in the multi-step benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/capability-masked-agent-policy-53fa446a6807`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
