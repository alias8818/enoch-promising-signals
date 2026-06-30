# Tiered agent cascade with early-exit structural verifier

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-agent-cascade-with-early-exit-structural-verifier-652df3f5ec33`
Run ID: `tiered-agent-cascade-with-early-exit-structural-verifier-652df3f5ec33-20260609T140313542766+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7d58c3a87292

## What looked useful

Structure-only early exit saved 84.87% relative cost but reduced accuracy by 21.20 percentage points versus strong-only; a limited semantic guard saved 80.10% cost but still lost 12.37 points overall, with success concentrated on the arithmetic task where the guard exactly checked correctness.

## Boundaries and scale limits

Synthetic stochastic agents, relative cost units, and toy invoice/arithmetic/route tasks only; no real LLM calls, production traces, token latency, or human-labeled datasets were used.

## Claim scope

In a 30,000-case deterministic synthetic simulator, structural early-exit cascades greatly reduced relative cost and improved well-formedness, but structural-only acceptance caused large semantic accuracy loss when well-formed wrong answers were possible.

## Why it stopped

Closed as no-paper useful signal because this proxy run early-falsifies the strong structural-only safety claim but does not provide direct real-agent evidence.

## Recommended next action

Run a bounded direct benchmark with actual LLM tiers on 300-1,000 labeled tasks, including executable semantic-verifier and schema-only task families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Tiered Cascade Benchmark With Semantic Verifier Ablations
- Success threshold: At least 50% measured cost reduction versus strong-only with no more than 3 percentage-point accuracy loss on tasks with executable semantic verifiers, and clear failure or fallback behavior on schema-only tasks.
- Stop condition: Stop if schema-only early exit loses more than 5 accuracy points or if semantic-verifier tasks fail to reach 30% measured cost reduction without accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-agent-cascade-with-early-exit-structural-verifier-652df3f5ec33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
