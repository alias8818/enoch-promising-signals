# Multi-seed evidence ledger versus stronger retrieval baselines for small local LLM memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-seed-evidence-ledger-versus-stronger-retrieval-basel-2219348c89`
Run ID: `multi-seed-evidence-ledger-versus-stronger-retrieval-basel-2219348c89-20260524T185753516729+0000`

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

- Parent run decision: Evidence ledger versus retrieval memory in a small local LLM agent: enoch://control-plane/projects/evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29/runs/evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29-20260524T154159930796+0000
- Parent run decision: Evidence-ledger consistency for small local agents: enoch://control-plane/projects/evidence-ledger-consistency-for-small-local-agents-28ea46080b37/runs/evidence-ledger-consistency-for-small-local-agents-28ea46080b37-20260524T075333128031+0000

## What looked useful

Evidence ledger conflict resolution produced a large reproducible accuracy gain over stronger retrieval baselines on a direct latest-memory QA benchmark, and ablations indicate the gain depends on keyed evidence plus conflict resolution rather than retrieval depth alone.

## Boundaries and scale limits

The run did not use real user logs, a real local LLM, trained rerankers, noisy ledger extraction, or natural-language answer generation. The full ledger consumed generator-provided structured evidence, so ingestion reliability remains untested.

## Claim scope

On deterministic synthetic small-assistant memory traces with five fixed seeds, about 6k notes per seed, and 288 latest-fact queries per seed, a structured evidence ledger with person keying, slot keying, and conflict resolution achieved 1.000 mean answer accuracy versus 0.506 for BM25 and 0.463 for hybrid reranked retrieval at top-k 16. Ledger ablations collapsed to 0.111-0.250 accuracy.

## Why it stopped

No-paper useful signal: the Tier 2 synthetic benchmark supports the mechanism, but the claim is not paper-positive because real local LLM ingestion and generation were proxied by deterministic extraction.

## Recommended next action

Run a bounded deepen test with a small local LLM doing noisy ledger extraction and answer generation on the same fixed-seed traces, then compare against the same retrieval baselines plus an LLM disambiguation baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy local-LLM ingestion for evidence ledger memory
- Success threshold: Mean ledger answer accuracy exceeds the strongest retrieval plus LLM-disambiguation baseline by at least 0.15 absolute across five fixed seeds while maintaining support recall at or above 0.90 and extraction F1 at or above 0.85.
- Stop condition: Stop as unsupported if noisy ledger accuracy is within 0.05 absolute of the strongest retrieval baseline, extraction F1 falls below 0.70 without a simple repair, or ledger ablations do not reduce accuracy by at least 0.10 absolute.

## Evidence references

- Artifact root: `<local-path>/projects/multi-seed-evidence-ledger-versus-stronger-retrieval-basel-2219348c89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
