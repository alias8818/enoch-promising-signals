# Bounded Sliding-Window Evidence Ledger for Context-Constrained Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-sliding-window-evidence-ledger-for-context-constrained-agents-42c74885e9bf`
Run ID: `bounded-sliding-window-evidence-ledger-for-context-constrained-agents-42c74885e9bf-20260529T030103328370+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

The evidence ledger consistently preserved query-relevant supporting facts better than a raw recent window under delayed recall, with paired absolute evidence-accuracy lifts from +0.0074 at budget 128 to +0.0436 at budget 1024 and tight 95% intervals.

## Boundaries and scale limits

No real LLM agent, prompt-token accounting, natural-language retrieval, multi-hop reasoning, adversarial prompting, or production trace data was tested. The run is CPU-only synthetic simulation and should not be treated as full validation for deployed context-constrained agents.

## Claim scope

In a deterministic synthetic delayed-recall stream with 800 entities, noisy distractors, changing facts, and fixed item budgets, a bounded per-key evidence ledger improved exact evidence-citation accuracy over a raw recent sliding window by about 10-11% relative across budgets 128-1024 over 40 seeds.

## Why it stopped

No-paper useful signal: the mechanism is supported in synthetic simulation, but direct agent evidence is required for a publishable claim.

## Recommended next action

Run a bounded direct LLM-agent follow-up with equal prompt-token budgets, realistic long-horizon tasks, and exact-citation scoring before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Token-Budgeted LLM Agent Test of a Bounded Evidence Ledger
- Success threshold: Evidence ledger achieves at least a 5 percentage point absolute gain in citation-faithful answer accuracy over recent-window memory at equal prompt-token budget without more than 15% latency overhead.
- Stop condition: Stop if the ledger fails to beat recent-window citation-faithful answer accuracy by at least 2 percentage points in a 50-task smoke set, or if prompt overhead consumes the budget before evidence can be retrieved.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-sliding-window-evidence-ledger-for-context-constrained-agents-42c74885e9bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
