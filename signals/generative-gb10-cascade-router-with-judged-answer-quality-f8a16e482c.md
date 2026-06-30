# Generative GB10 cascade router with judged answer quality

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `generative-gb10-cascade-router-with-judged-answer-quality-f8a16e482c`
Run ID: `generative-gb10-cascade-router-with-judged-answer-quality-f8a16e482c-20260629T135751285942+0000`

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

- Parent run decision: Confidence-Gated Two-Tier Local Cascade Router on GB10: enoch://control-plane/projects/confidence-gated-two-tier-local-cascade-router-on-gb10-af6393a2f58c/runs/confidence-gated-two-tier-local-cascade-router-on-gb10-af6393a2f58c-20260629T133732437341+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/75d15a93c823

## What looked useful

Generated self-evaluation features produced a small but measurable cost-quality improvement over confidence-only routing in a controlled proxy, while the 80% escalation rate and large gap to the oracle bound show the mechanism is not strong enough for a paper-ready claim.

## Boundaries and scale limits

This run used synthetic tasks, simulated weak/strong answerers, exact oracle judging, and a small MLP router. It did not test real LLM outputs, real LLM-as-judge reliability, human preferences, production latency, token economics, multi-model serving, or GB10 memory pressure with resident models.

## Claim scope

In a synthetic exact-judge benchmark on GB10, a learned router using generated weak-answer self-evaluation features reached 95.065% judged quality at 80.01% escalation and 7.4008 relative cost, cheaper than a confidence-only threshold reaching at least 95% quality at 84.455% escalation and 7.7564 relative cost.

## Why it stopped

Proxy-only synthetic validation supports a mechanism but does not directly validate a generative GB10 cascade router with judged answer quality.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should replace synthetic solvers with real small/large local models and a held-out exact-answer QA set while preserving the same baselines and cost-quality sweep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model GB10 cascade router on exact-answer QA
- Success threshold: At a fixed quality target of at least 95% of always-strong quality, the learned generated-feature router reduces relative cost by at least 10% versus confidence-only routing and the result persists on a held-out distribution-shift split.
- Stop condition: Stop if the learned router fails to beat confidence-only by at least 5% relative cost at the quality target, if judge labels are too noisy to rank policies, or if GB10 cannot hold the selected local models without memory pressure.

## Evidence references

- Artifact root: `<local-path>/projects/generative-gb10-cascade-router-with-judged-answer-quality-f8a16e482c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
