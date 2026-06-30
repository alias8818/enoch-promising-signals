# Ledger anchoring in a local tiny language-agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ledger-anchoring-in-a-local-tiny-language-agent-harness-642f59c44a`
Run ID: `ledger-anchoring-in-a-local-tiny-language-agent-harness-642f59c44a-20260529T213541938038+0000`

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

- Parent run decision: Evidence-ledger anchoring for tiny CPU-bound agents: enoch://control-plane/projects/evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6/runs/evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6-20260529T101321005606+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Ledger anchoring achieved 1.000 mean final-state accuracy under context-only corruption versus 0.260 for context-only scratch memory, a +0.740 improvement, and detected 3453/3453 tampered ledger episodes in the tamper condition. A no-corruption control showed both variants at 1.000 accuracy.

## Boundaries and scale limits

Tested only on a deterministic tiny DSL harness with synthetic context and ledger perturbations: 8 seeds, 2000 episodes per seed, 24 instructions per episode. No real LLM planner, natural-language tasks, prompt injection, long-context degradation, or external tool environment was evaluated.

## Claim scope

In a controlled local tiny DSL agent harness, replaying an append-only hash-chained ledger as the source of truth prevents between-step mutable scratch-context drift from corrupting final program state and detects committed ledger-entry tampering.

## Why it stopped

No-paper closure: Tier 1 mechanism support in a controlled tiny harness is useful but not publication-grade direct evidence for language-model agents.

## Recommended next action

Run a bounded deepen follow-up that wraps the same ledger API around an actual local small-model or stochastic tool-agent loop on semi-structured DSL tasks with transcript edits, measuring completion, detection, and recovery against a context-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger anchoring around a real local tiny model/tool-agent loop
- Success threshold: Ledger anchoring improves perturbed-task completion by at least 20 percentage points over context-only memory, detects at least 95% of committed tamper events, and loses no more than 5 percentage points in no-perturbation completion.
- Stop condition: Stop if the real local agent cannot complete at least 70% of no-perturbation tasks, if ledger overhead dominates the run by more than 2x without recovery benefit, or if tamper detection falls below 95%.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-anchoring-in-a-local-tiny-language-agent-harness-642f59c44a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
