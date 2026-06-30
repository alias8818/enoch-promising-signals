# Safety-First Cascade Router for Local Agent Refusal

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `safety-first-cascade-router-for-local-agent-refusal-7217e459d233`
Run ID: `safety-first-cascade-router-for-local-agent-refusal-7217e459d233-20260522T011259285938+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

OOD synthetic evidence supports the safety-first cascade mechanism as a risk-reduction tradeoff: unsafe false-allow fell from 22.54% for cheap NB direct classification to 1.87% for the safety-first cascade, with average cost rising from 1.0 to 6.01 relative units and safe false-refusal rising from 21.51% to 25.45%. A weaker simulated reviewer still reduced unsafe false-allow to 2.70%.

## Boundaries and scale limits

Proxy-only synthetic prompts; no real local-agent traces, no real LLM or human reviewer, no production latency measurements, and no broad adversarial robustness validation. In-distribution templates were too easy and favored the cheap classifier.

## Claim scope

On a deterministic synthetic local-agent refusal benchmark with an OOD template split, a lexical + cheap Naive Bayes + simulated stronger-review cascade reduced unsafe false-allow versus cheap direct classification, at higher false-refusal and relative compute cost.

## Why it stopped

No-paper closure: the result is useful but proxy-only, mixed by distribution, and not publication-grade direct evidence.

## Recommended next action

Run a bounded direct-evidence follow-up using real or human-labeled local-agent refusal traces and an actual local reviewer model instead of a simulated oracle.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of safety-first cascade refusal routing
- Success threshold: Unsafe false-allow reduced by at least 50% relative to cheap direct classification, average cost at or below 40% of always-review, and safe false-refusal increase no more than 5 absolute percentage points on held-out real/OOD data.
- Stop condition: Stop if real-trace cascade reduces unsafe false-allow by less than 25% relative or if safe false-refusal increases by more than 10 absolute percentage points at the target cost budget.

## Evidence references

- Artifact root: `<local-path>/projects/safety-first-cascade-router-for-local-agent-refusal-7217e459d233`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
