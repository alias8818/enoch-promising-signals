# Held-out multi-slice compressed ledger QA on real Codex tool traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-multi-slice-compressed-ledger-qa-on-real-codex-to-78dae0fda5`
Run ID: `held-out-multi-slice-compressed-ledger-qa-on-real-codex-to-78dae0fda5-20260529T021621105587+0000`

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

- Parent run decision: Compressed Evidence Ledger for Small Tool Agents: enoch://control-plane/projects/compressed-evidence-ledger-for-small-tool-agents-d7caf384699e/runs/compressed-evidence-ledger-for-small-tool-agents-d7caf384699e-20260528T172603301807+0000
- Parent run decision: LLM-in-the-loop compressed evidence ledger test on naturalistic tool traces: enoch://control-plane/projects/llm-in-the-loop-compressed-evidence-ledger-test-on-natural-03eb90e2cb/runs/llm-in-the-loop-compressed-evidence-ledger-test-on-natural-03eb90e2cb-20260528T213003326966+0000

## What looked useful

Full ledger accuracy was 0.875 versus 0.181 for equal-budget raw transcript, but only +0.051 over stats-only and -0.060 versus no-timeline; the full multi-slice threshold failed even though compression versus raw was strongly useful.

## Boundaries and scale limits

Single local 1.5B instruction model, 24 traces, exact programmatic QA labels, deterministic hand-built ledger, and no human adjudication or open-ended final-decision reconstruction.

## Claim scope

On 24 fixed-seed held-out real Codex tool traces, a deterministic compact ledger lets Qwen2.5-1.5B-Instruct answer exact trace QA much more accurately than an equal-character raw transcript snippet, but the tested full multi-slice ledger does not outperform compact ablations by the predeclared margin.

## Why it stopped

Tier 2 fixed-seed direct test failed the predeclared ablation threshold: full_ledger - stats_only_ledger was +0.051, below the +0.10 requirement, and no_timeline_ledger outperformed full_ledger.

## Recommended next action

Stop this run as no-paper useful signal; test a redesigned non-redundant slice benchmark before making any multi-slice ledger claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-redundant slice QA for compact Codex evidence ledgers
- Success threshold: Full multi-slice ledger accuracy >= 0.80, >= +0.20 over raw_budget, >= +0.10 over compact keyed-ledger baseline, and each slice-removal ablation reduces its target slice accuracy by at least 0.15.
- Stop condition: Stop as negative if compact keyed facts match or exceed the full multi-slice ledger, or if slice-removal ablations do not selectively reduce target slice accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-multi-slice-compressed-ledger-qa-on-real-codex-to-78dae0fda5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
