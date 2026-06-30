# Compressed Evidence Ledger for Small Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-evidence-ledger-for-small-tool-agents-d7caf384699e`
Run ID: `compressed-evidence-ledger-for-small-tool-agents-d7caf384699e-20260528T172603301807+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c885858a7e3

## What looked useful

Median transcript length was 22920 tokens and median static ledger length was 3480 tokens, a 6.59x compression ratio. The compressed ledger query view reached 1.000 accuracy at all tested budgets with median 7 context tokens, while the best raw baseline reached 0.262 accuracy at 2048 tokens.

## Boundaries and scale limits

Synthetic generated traces only; deterministic exact parser; assumes correct ledger construction; no real LLM answerer, real tools, natural traces, adversarial extraction noise, or live agent loop.

## Claim scope

On 500 synthetic two-hop tool-trace retrieval cases, a deterministic compressed evidence ledger preserved exact answerability under 128-2048 token context budgets while raw head, tail, random-window, and literal-keyword transcript excerpts lost most required evidence.

## Why it stopped

Synthetic proxy evidence supports the information-preservation mechanism but is not direct/full validation of real small tool agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is an LLM-in-the-loop replication with a small local instruct model and fallible ledger construction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop compressed evidence ledger test on naturalistic tool traces
- Success threshold: Ledger condition improves exact-match accuracy by at least 15 percentage points over the strongest raw/retrieval baseline at two or more budgets without increasing median context tokens.
- Stop condition: Stop if ledger construction accuracy falls below 90% on required facts or if model-answer accuracy is within 5 percentage points of the strongest baseline across all budgets.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-for-small-tool-agents-d7caf384699e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
