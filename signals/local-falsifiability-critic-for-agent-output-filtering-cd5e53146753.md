# Local Falsifiability Critic for Agent Output Filtering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-falsifiability-critic-for-agent-output-filtering-cd5e53146753`
Run ID: `local-falsifiability-critic-for-agent-output-filtering-cd5e53146753-20260525T200321417231+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

Evidence-consistency checking, not mere specificity, created the gain: the critic reached 0.875 accuracy, 1.000 precision, 0.667 recall, and 1.000 specificity, while the specificity-only ablation reached 0.625 accuracy, 0.500 precision, 0.667 recall, and 0.600 specificity. Bootstrap accuracy delta vs specificity-only was +0.2498 mean with 5th to 95th percentile +0.2339 to +0.2661.

## Boundaries and scale limits

Synthetic/proxy benchmark only: 240 generated tasks, 1920 generated final-answer cases, no real LLM agent traces, no open-domain retrieval, no human utility labels, and no model-based judge baseline. Correct natural-language answers outside the structured claim contract were rejected.

## Claim scope

In a deterministic synthetic benchmark with a known local evidence store and explicit claim-slot outputs, a local falsifiability critic improved filtering accuracy and eliminated false accepts relative to confidence, checkword, pass-all, and specificity-only baselines.

## Why it stopped

No-paper closure: the current result is useful synthetic/proxy evidence and exposes a structured-output dependency, but it is not direct validation on real agent outputs.

## Recommended next action

Run a bounded deepen follow-up on real local agent traces that require explicit claim-slot final answers, with independent correctness labels and the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace falsifiability critic with explicit claim-slot final answers
- Success threshold: False accepts reduced by at least 30% versus specificity-only with recall at or above 70% on acceptable structured outputs and no more than 10% unsupported accepts.
- Stop condition: Stop as negative if the critic fails to reduce false accepts by 15% versus specificity-only, if recall on acceptable structured outputs falls below 50%, or if most real traces lack extractable claim slots.

## Evidence references

- Artifact root: `<local-path>/projects/local-falsifiability-critic-for-agent-output-filtering-cd5e53146753`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
