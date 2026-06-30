# Evaluate structured evidence ledgers on sandboxed small LLM tool agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evaluate-structured-evidence-ledgers-on-sandboxed-small-ll-4a5947cafb`
Run ID: `evaluate-structured-evidence-ledgers-on-sandboxed-small-ll-4a5947cafb-20260607T200458176002+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Structured Evidence Ledger Constrains Tool Misuse in Small Agents: enoch://control-plane/projects/structured-evidence-ledger-constrains-tool-misuse-in-small-agents-df13049acc87/runs/structured-evidence-ledger-constrains-tool-misuse-in-small-agents-df13049acc87-20260607T161634563882+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/94ace52d2eee

## What looked useful

Structured ledgers improved first lookup action accuracy (0.9556 vs 0.8667) but hurt second tool selection (0.3444 vs 0.8056) and end-to-end accuracy (0.0500 vs 0.1500), suggesting JSON ledger formatting can impede small-model use of intermediate evidence.

## Boundaries and scale limits

Synthetic task family; enumerated candidate action scoring rather than free-form tool-call generation; one small seq2seq model; no real external tools, production traces, chat-tuned model comparison, or long-horizon agents.

## Claim scope

In a constrained Tier 1 benchmark using google/flan-t5-base to score enumerated sandboxed tool actions and final answers over 180 paired synthetic employee-invoice tasks, structured JSON evidence ledgers underperformed raw noisy tool transcripts on end-to-end accuracy.

## Why it stopped

Early direct Tier 1 falsification for the constrained small-agent setup: the structured ledger condition consistently underperformed raw transcripts across three seeds, but this is not a full validation or global rejection of evidence ledgers.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing the line, test a chat-tuned small model with a tokenizer-friendly ledger format and free-form parser retries on the same task family.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test tokenizer-friendly ledgers on chat-tuned small tool agents
- Success threshold: Compact ledger improves mean end-to-end accuracy by at least 5 percentage points over raw transcript and does not reduce any tool-action phase by more than 2 percentage points across at least 180 paired tasks.
- Stop condition: Stop if compact ledger fails to beat raw transcript on end-to-end accuracy or repeats the second-tool selection degradation on two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-structured-evidence-ledgers-on-sandboxed-small-ll-4a5947cafb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
