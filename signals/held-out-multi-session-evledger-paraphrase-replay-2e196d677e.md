# Held-out multi-session EvLedger paraphrase replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-multi-session-evledger-paraphrase-replay-2e196d677e`
Run ID: `held-out-multi-session-evledger-paraphrase-replay-2e196d677e-20260619T215852386031+0000`

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

- Parent run decision: EvLedger: Minimal Evidence Ledger for Agent Reliability on Repeated Tasks: enoch://control-plane/projects/evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d/runs/evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d-20260619T211210112448+0000
- Parent run decision: Replay EvLedger on real repeated tool-agent traces with paraphrase drift: enoch://control-plane/projects/replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862/runs/replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862-20260619T214300934539+0000

## What looked useful

EvLedger reached 0.9708 answer accuracy versus 0.3433 for transcript search and 0.2550 for flat retrieval. Removing paraphrase normalization dropped accuracy to 0.5217, and removing recency dropped accuracy to 0.1908, supporting both proposed mechanisms in this bounded setting.

## Boundaries and scale limits

Synthetic hand-templated replay data only; deterministic extraction and answering; no LLM agent loop, real operator transcripts, noisy entity resolution, or large-scale deployment traces.

## Claim scope

In a deterministic synthetic multi-session replay benchmark with 5 fixed seeds and 1200 queries, an EvLedger-style canonical event ledger with paraphrase normalization and latest-event selection outperformed lexical transcript and flat retrieval baselines on direct answer accuracy, source-event top-1, and MRR.

## Why it stopped

Tier 2 synthetic mechanism evidence was produced, but the result is not paper-positive because it lacks real or semi-real agent transcript validation and LLM extraction/generation failure modes.

## Recommended next action

Run one bounded deepen follow-up on semi-real anonymized multi-session agent transcripts or LLM-generated noisy replay logs with the same strategy matrix and success threshold before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semi-real EvLedger paraphrase replay with LLM extraction noise
- Success threshold: EvLedger answer accuracy exceeds both transcript_search and flat_retrieval by at least 0.20 absolute, with bootstrap 95% confidence intervals that do not overlap the best baseline, and both ablations lose at least 0.10 absolute accuracy.
- Stop condition: Stop as no-paper negative if EvLedger fails to beat the best real baseline by 0.10 absolute or if either required mechanism ablation shows less than 0.05 absolute degradation.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-multi-session-evledger-paraphrase-replay-2e196d677e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
