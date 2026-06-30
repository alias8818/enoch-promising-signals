# Tiny agent evidence ledger reduces ungrounded tool use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-reduces-ungrounded-tool-use-0053ed7547d6`
Run ID: `tiny-agent-evidence-ledger-reduces-ungrounded-tool-use-0053ed7547d6-20260607T091733344571+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed5c7ff6fa8c

## What looked useful

Ledger-gated policy reduced ungrounded tool calls from 0.671 per task to 0.000 in the main 1,000-task run, while record-only matched baseline. The effect persisted across proposal-noise levels 0.10, 0.20, 0.50, and 0.70.

## Boundaries and scale limits

Synthetic tasks only; no real LLM planner, no real external tools, no prompt-injection setting, no long-horizon benchmark, and no human evaluation. Main result used 1,000 tasks at one noise level plus four 1,000-task noise-sweep settings.

## Claim scope

In a deterministic synthetic customer/invoice tool-use benchmark with a stochastic tiny-agent proposal model, execution-time evidence-ledger gating eliminated unsupported tool-call arguments under paired proposal streams.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-level rather than publication-grade validation on real LLM agents and real tool traces.

## Recommended next action

Run a bounded real-LLM follow-up using the same evidence-ledger gate on a public or locally generated tool-use benchmark with distractor records and trace-level unsupported-argument scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM evidence-ledger gate on distractor tool-use tasks
- Success threshold: Ledger-gated agent reduces unsupported tool-call arguments by at least 50% versus both controls with no more than a 5 percentage point success-rate drop on at least 200 tasks.
- Stop condition: Stop if the gated real-LLM agent does not reduce unsupported tool-call arguments by at least 25% in a 50-task pilot or if gating causes more than a 10 percentage point success-rate drop.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-reduces-ungrounded-tool-use-0053ed7547d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
