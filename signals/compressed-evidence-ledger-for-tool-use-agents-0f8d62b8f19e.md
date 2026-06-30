# Compressed Evidence Ledger for Tool-Use Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e`
Run ID: `compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e-20260602T112211185029+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66e0858ba973

## What looked useful

Across 303 total trials including smoke, main, and sweeps, ledger accuracy and provenance accuracy were 1.0 in every tested configuration. Main-run same-budget tail accuracy was 0.594 and lexical retrieval accuracy was 0.663; provenance accuracy was 0.195 and 0.307 respectively.

## Boundaries and scale limits

No real agent traces, no LLM extraction or answer generation, no adversarial/malformed tool outputs, no learned memory baseline, and no production context-window evaluation were tested.

## Claim scope

On deterministic synthetic tool-use traces with parseable entity facts, a structured compressed evidence ledger preserved latest target facts and provenance at roughly 23-41% of raw trace tokens, outperforming same-budget tail and lexical retrieval baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/parser-based and does not directly validate real tool-use agents.

## Recommended next action

Run a bounded deepen test using real or LLM-generated heterogeneous tool traces, an LLM answerer, and a stronger retrieval/memory baseline before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Tool-Trace Evidence Ledger Evaluation
- Success threshold: Ledger condition improves answer accuracy by at least 10 percentage points and provenance accuracy by at least 20 percentage points over the best same-budget baseline while using no more than 40% of raw trace tokens.
- Stop condition: Stop if ledger extraction errors exceed 20% of required facts or if best-baseline accuracy is within 5 percentage points of ledger accuracy at equal token budget.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
