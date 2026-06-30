# Compressed Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-agent-evidence-ledger-29c1b399cf1c`
Run ID: `compressed-agent-evidence-ledger-29c1b399cf1c-20260523T022605364766+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Structured ledger encoding achieved 2.88x-3.37x plain JSON/context compression versus raw JSONL across 1k-8k event synthetic runs while maintaining 100% exact audit-query accuracy and tamper detection. A lossy sparse summary was smaller but answered only 8.5%-11.5% of audit queries in the same sweeps.

## Boundaries and scale limits

Only synthetic traces were tested, with up to 8,000 events per run and exact-rule evaluators. No real agent traces, tokenizer-specific tokenization, LLM summary baseline, human audit study, or production adversarial tamper model was evaluated.

## Claim scope

On deterministic synthetic agent-like traces with command records, artifact hashes, metrics, decisions, observations, and hash-chain links, a structured compressed ledger preserved exact audit-query answers and tamper detection while reducing plain JSON/context footprint versus raw JSONL.

## Why it stopped

No-paper closure: the local evidence is a useful synthetic mechanism signal, but it is not direct production evidence and should not be presented as full validation.

## Recommended next action

Run a bounded real-trace follow-up on 50-100 actual agent runs with exact audit tasks, tokenizer-specific token counts, a real LLM-summary baseline, and human audit-time measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace compressed evidence ledger audit benchmark
- Success threshold: Structured ledger reaches at least 95% exact audit answer accuracy, at least 2x tokenizer-measured context reduction versus raw JSONL, successful tamper detection on seeded mutations, and better answerability than the LLM summary baseline.
- Stop condition: Stop if real traces do not compress by at least 1.5x at 95% answer accuracy, if ledger construction requires manual trace-specific schemas, or if LLM summaries match answerability at lower context cost.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-agent-evidence-ledger-29c1b399cf1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
