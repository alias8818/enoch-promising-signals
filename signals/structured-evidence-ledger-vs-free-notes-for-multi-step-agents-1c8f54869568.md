# Structured Evidence Ledger vs Free Notes for Multi-Step Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-vs-free-notes-for-multi-step-agents-1c8f54869568`
Run ID: `structured-evidence-ledger-vs-free-notes-for-multi-step-agents-1c8f54869568-20260611T060231832448+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46bcacdb967d

## What looked useful

The result isolates contradiction handling as the likely mechanism: ledger and free notes both reached 100% accuracy in benign and high-noise/no-contradiction controls, while ledger exceeded free notes by 0.621 to 0.824 accuracy in contradiction conditions with paired bootstrap 95% CIs excluding zero.

## Boundaries and scale limits

Proxy-only evidence: no real LLM agent loop, no natural-language summarization behavior, no real tool-use benchmark, and no full-scale validation. The run used 8,000 synthetic tasks total and completed in 5.625 seconds on one CPU process.

## Claim scope

In a local synthetic 4-hop evidence-chaining benchmark with fixed memory budgets, a keyed evidence ledger with reliability/timestamp conflict handling matched free notes when evidence had no contradictions and substantially outperformed free-form append-only notes when contradictions were present.

## Why it stopped

Evidence is a bounded synthetic proxy that supports the mechanism but is not direct or publication-grade validation of multi-step LLM agents.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should deepen by swapping ledger vs free-note memory inside a real LLM or small open-weight multi-step QA/tool-use agent with fixed prompts, token budgets, and contradiction-heavy traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent validation of structured evidence ledger vs free notes on contradiction-heavy multi-step QA
- Success threshold: Ledger improves contradiction-condition final-answer accuracy by at least 10 percentage points over free notes with paired 95% CI excluding zero, while no-contradiction accuracy drops by no more than 2 percentage points.
- Stop condition: Stop if ledger does not beat free notes by at least 5 percentage points on contradiction-heavy tasks after a 200-task pilot, or if trace audits show failures are dominated by generation errors unrelated to memory representation.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-vs-free-notes-for-multi-step-agents-1c8f54869568`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
