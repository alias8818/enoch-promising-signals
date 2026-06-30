# Evidence-ledger consistency for small local agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-consistency-for-small-local-agents-28ea46080b37`
Run ID: `evidence-ledger-consistency-for-small-local-agents-28ea46080b37-20260524T075333128031+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Ledger bookkeeping gave full active-evidence behavior without retaining a full transcript in context. Large-memory transcript search caught up to the ledger, showing the advantage is memory organization under pressure rather than superiority over complete history. Summary memory retained a retraction fallback failure mode even with large capacity.

## Boundaries and scale limits

The run used synthetic structured statements and deterministic agents, not actual small LLM parsing/generation, embedding retrieval, human-authored tasks, multi-agent coordination, or production latency/token-cost measurements. It validates a memory-accounting mechanism, not a full real-agent system.

## Claim scope

In a deterministic synthetic local-agent benchmark with structured evidence statements, updates, retractions, distractors, and bounded memory baselines, an explicit evidence ledger preserved 100% answer accuracy and source consistency while recent-window and summary-memory agents missed active older evidence under memory pressure.

## Why it stopped

Closed as no-paper useful signal: this was a synthetic mechanism test with moderate evidence, not a direct validation on real local LLM agents.

## Recommended next action

Run a bounded direct small-LLM-agent follow-up that uses noisy natural-language evidence and compares ledger memory against transcript search and retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger versus retrieval memory in a small local LLM agent
- Success threshold: Across at least 30 randomized task streams, ledger memory improves answer accuracy by at least 10 percentage points over the best bounded baseline while keeping unsupported citations below 2% and adding no more than 25% latency overhead.
- Stop condition: Stop if ledger extraction errors exceed 10%, if the best retrieval/transcript baseline is within 3 percentage points of ledger accuracy, or if latency/token overhead makes the ledger impractical for the local-agent budget.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-consistency-for-small-local-agents-28ea46080b37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
