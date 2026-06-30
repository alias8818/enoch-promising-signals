# Evidence ledger versus retrieval memory in a small local LLM agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29`
Run ID: `evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29-20260524T154159930796+0000`

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

- Parent run decision: Evidence-ledger consistency for small local agents: enoch://control-plane/projects/evidence-ledger-consistency-for-small-local-agents-28ea46080b37/runs/evidence-ledger-consistency-for-small-local-agents-28ea46080b37-20260524T075333128031+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Evidence ledger full accuracy was 0.938 versus 0.292 for retrieval, with the correct source present in all retrieval contexts; failures were mostly stale-evidence conflict resolution rather than missing evidence.

## Boundaries and scale limits

Single synthetic dataset seed, one small local model, oracle-style structured ledger construction, simple lexical retrieval baseline, no real agent histories, no learned extraction, no multi-model or multi-seed robustness.

## Claim scope

In a 48-query synthetic current-state task using Qwen/Qwen2.5-0.5B-Instruct locally, a structured evidence ledger outperformed raw lexical top-k retrieval memory on value-plus-source accuracy while using fewer memory tokens.

## Why it stopped

Tier 1 controlled small direct test produced a useful mechanism signal but not publication-grade evidence.

## Recommended next action

Run a bounded deepen test across at least 5 seeds and 2 small local models, adding a recency-aware/reranked retrieval baseline and a noisy ledger-extraction condition.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed evidence ledger versus stronger retrieval baselines for small local LLM memory
- Success threshold: Ledger full value-plus-source accuracy exceeds the best retrieval baseline by at least 10 percentage points on mean paired accuracy while using no more memory tokens, and remains above 80% accuracy under 5% simulated ledger extraction noise.
- Stop condition: Stop if a stronger retrieval baseline closes the mean accuracy gap below 5 percentage points, if ledger extraction noise below 5% collapses ledger accuracy below 70%, or if results reverse on either tested model.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
