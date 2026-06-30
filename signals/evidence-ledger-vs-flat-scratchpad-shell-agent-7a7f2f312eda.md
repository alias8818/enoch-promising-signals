# Evidence-ledger vs flat-scratchpad shell agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda`
Run ID: `evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda-20260610T060351799288+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/25cc1bb5a3c2

## What looked useful

Structured evidence retention preserved causal shell observations under noisy bounded-memory conditions; at 80 noise observations and 900-2200 character budgets, ledger mean fix accuracy was 0.9767-1.0000 versus flat scratchpad 0.0000-0.3017 across three seeds.

## Boundaries and scale limits

Proxy-only evidence: no live LLM, no real shell tool loop, no real repositories, deterministic inference, character budgets rather than tokenizer-specific prompt budgets. Flat scratchpad matches the ledger when noise is low or budget is large enough to retain all evidence.

## Claim scope

In a deterministic synthetic shell-diagnostic memory benchmark with fixed character budgets, noisy observations, and known causal evidence, a priority-compacted evidence ledger retained enough diagnostic evidence for higher fix accuracy than a recency-evicted flat scratchpad at tight budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic/proxy retention test rather than direct validation of a live shell agent.

## Recommended next action

Run a bounded live LLM shell-agent follow-up using the same generated task traces, token-budgeted ledger versus flat prompts, randomized evidence order, and hidden-ground-truth fix scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live shell-agent evidence-ledger memory test on generated diagnostic traces
- Success threshold: Evidence ledger improves fix accuracy by at least 10 percentage points over flat scratchpad at one or more tight token budgets without reducing accuracy at large budgets.
- Stop condition: Stop if ledger improvement is below 5 percentage points at all tight budgets or if ledger prompts increase invalid/unsupported fixes by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
