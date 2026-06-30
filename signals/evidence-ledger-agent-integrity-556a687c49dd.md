# Evidence-Ledger Agent Integrity

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-integrity-556a687c49dd`
Run ID: `evidence-ledger-agent-integrity-556a687c49dd-20260524T220110997952+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

Across 5,000 traces per attack class, ledger verification detected 100% of six tamper/failure classes with 0% false positives on honest traces. A semantic transcript baseline also had 0% false positives but missed coordinated rewrites where claim and evidence were edited together, yielding 83.33% overall detection versus 100% for the ledger.

## Boundaries and scale limits

Synthetic structured facts only; no real LLM agent, natural-language entailment, retrieval corpus, compromised signer, distributed storage, or production latency validation was tested.

## Claim scope

In a deterministic synthetic agent-trace benchmark, an append-only evidence ledger with sealed claim/evidence hashes and hash-chain verification detects unsupported claims and post-hoc or coordinated trace rewrites that plain transcript and final-state semantic transcript checks can miss.

## Why it stopped

The result supports only a synthetic mechanism claim and is not full validation of evidence-ledger integrity for real agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to integrate the ledger into a real LangGraph-style agent harness and replay adversarial natural-language tasks against transcript, semantic-audit, and ledger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Integrity Replay
- Success threshold: Ledger detects at least 95% of injected unsupported/tampered claims, improves over semantic transcript auditing by at least 10 percentage points on coordinated rewrite or equivalent persistence attacks, keeps false positives at or below 2%, and adds less than 10% runtime overhead in the replay harness.
- Stop condition: Stop if ledger detection is not materially better than semantic transcript auditing on persistence attacks, false positives exceed 5%, or runtime overhead exceeds 25% after straightforward batching/caching.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-integrity-556a687c49dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
