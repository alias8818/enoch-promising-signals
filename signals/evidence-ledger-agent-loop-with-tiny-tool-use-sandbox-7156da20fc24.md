# Evidence-Ledger Agent Loop with Tiny Tool-Use Sandbox

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-with-tiny-tool-use-sandbox-7156da20fc24`
Run ID: `evidence-ledger-agent-loop-with-tiny-tool-use-sandbox-7156da20fc24-20260608T223917957683+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/767958d5e25e

## What looked useful

The ledger mechanism produced 100% exact accuracy and 100% supported answers on 10,000 ledger-agent task runs, versus 74.24% accuracy and 25.76% unsupported wrong answers for the baseline, with mean per-task elapsed time rising from 0.00205 ms to 0.00650 ms.

## Boundaries and scale limits

Synthetic Python policies only; no real LLM planner, no natural adversarial corpus, no production tool latency, no long-horizon evidence management, and no external API side effects were tested.

## Claim scope

In a deterministic synthetic benchmark of 10 tiny tool-answerable tasks over 1,000 trials, an evidence-ledger loop with allowlisted sandbox tools and final-answer verification eliminated unsupported wrong answers compared with a no-ledger baseline policy.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence for the mechanism, not direct publication-grade validation of LLM agents.

## Recommended next action

Run a bounded local LLM deepen benchmark using the same ledger and sandbox harness on natural-language tool-use tasks, comparing unsupported-answer rate against a same-tools no-ledger baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local LLM Evidence-Ledger Tool-Use Benchmark
- Success threshold: At least 200 LLM task attempts with unsupported-answer rate reduced by >=50% versus baseline, exact accuracy no more than 5 percentage points worse than baseline, and saved traces for all repaired or blocked answers.
- Stop condition: Stop if the local LLM cannot reliably emit parseable tool calls after a small prompt calibration, or if the ledger loop reduces exact accuracy by more than 10 percentage points on the first 50 attempts.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-with-tiny-tool-use-sandbox-7156da20fc24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
