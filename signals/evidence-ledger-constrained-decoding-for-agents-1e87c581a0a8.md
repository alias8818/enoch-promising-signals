# Evidence-Ledger Constrained Decoding for Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-constrained-decoding-for-agents-1e87c581a0a8`
Run ID: `evidence-ledger-constrained-decoding-for-agents-1e87c581a0a8-20260522T143904701171+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85a4b29ef1ec

## What looked useful

Across 30,000 synthetic tasks, constrained decoding achieved 1.0 ledger-valid output rate at every tested valid-mass setting, while unconstrained validity tracked base valid mass. Rejection sampling also reached 1.0 validity but required 50.1008 mean attempts and 148.2 p95 attempts at 0.02 valid mass. Including setup, naive constrained filtering beat rejection only at 0.02 valid mass and was slower at higher valid masses.

## Boundaries and scale limits

No real LLM, tokenizer, batched logits, tool execution, or human-authored agent traces were tested. The constrained implementation enumerates and filters complete candidates, so its setup cost is not representative of an optimized token-level FSA/trie decoder.

## Claim scope

In a synthetic complete-candidate agent-output benchmark, restricting generation to outputs accepted by an evidence-ledger validator eliminates unsupported evidence references. A naive per-task candidate-filter implementation is only faster than rejection sampling when base valid-output probability is very low.

## Why it stopped

Synthetic mechanism evidence is mixed: ledger constraints guarantee validity in the proxy, but the tested naive filtering implementation has setup overhead that prevents a practical efficiency claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement token-level ledger constraints over a real tokenizer and small open model to measure validity and throughput without complete-candidate enumeration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Evidence-Ledger Constrained Decoding on a Small Open Model
- Success threshold: Constrained decoding must achieve 100% ledger-valid outputs with median latency no worse than 1.5x rejection sampling at low valid probability and no worse than 2.0x unconstrained plus validation at moderate valid probability.
- Stop condition: Stop if token-level masking cannot be implemented locally, if validity falls below 100% due to tokenizer/schema mismatch, or if constrained decoding is more than 3x slower than rejection in two or more tested valid-probability regimes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-decoding-for-agents-1e87c581a0a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
