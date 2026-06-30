# LLM-in-the-loop compressed evidence ledger test on naturalistic tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-in-the-loop-compressed-evidence-ledger-test-on-natural-03eb90e2cb`
Run ID: `llm-in-the-loop-compressed-evidence-ledger-test-on-natural-03eb90e2cb-20260528T213003326966+0000`

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

- Parent run decision: Compressed Evidence Ledger for Small Tool Agents: enoch://control-plane/projects/compressed-evidence-ledger-for-small-tool-agents-d7caf384699e/runs/compressed-evidence-ledger-for-small-tool-agents-d7caf384699e-20260528T172603301807+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c885858a7e3

## What looked useful

Ledger context achieved 0.875 accuracy (21/24) versus 0.417 (10/24) for size-matched raw snippets, with a +0.458 accuracy delta at a 0.0151 ledger/raw character ratio. The predeclared useful-signal threshold was met, but this is not paper-positive evidence.

## Boundaries and scale limits

Small Tier 1 sample; one local small model; deterministic schema-aligned ledger and programmatically generated questions; no human labels; exact command-string recovery remained brittle.

## Claim scope

On 6 real Codex tool-trace JSONL files, a deterministic compressed evidence ledger consumed by Qwen2.5-1.5B-Instruct recovered exact command-count, failure-count, first-command, and last-exit audit facts more accurately than a same-character-budget raw transcript snippet.

## Why it stopped

Closed as no-paper useful signal: Tier 1 direct test supports the mechanism, but the evidence is too small and schema-aligned for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on 30-50 held-out real traces with independently authored audit questions and separate numeric, path, command-string, and final-decision slices.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out multi-slice compressed ledger QA on real Codex tool traces
- Success threshold: Ledger accuracy >= 0.80 overall, at least +0.20 over both baselines, and no slice below 0.65 exact-match accuracy.
- Stop condition: Stop if ledger accuracy is below 0.70 overall, if it fails to beat either baseline by +0.10, or if exact command/path slices remain dominated by formatting errors after tolerant and exact scoring are separated.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-compressed-evidence-ledger-test-on-natural-03eb90e2cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
