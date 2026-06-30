# Evidence Ledger Falsifiability Protocol for Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d`
Run ID: `evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d-20260610T133944366191+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f040bdbdf971

## What looked useful

The useful design signal is that evidence ledgers need strict source-content and claim-consistency validation. A citation-presence or id-only protocol detected only 32.1% of adversarial false claims in the 5,000-task synthetic benchmark, while strict validation detected 100.0% in this oracle setting.

## Boundaries and scale limits

Synthetic-only protocol test with generated evidence and controlled corruptions; no real LLM agents, real retrieval corpora, ambiguous natural-language claims, human reviewers, or production workflows were evaluated.

## Claim scope

In a deterministic synthetic oracle benchmark, strict claim-level evidence ledgers that validate evidence id existence, quote integrity, semantic alignment, and numeric consistency made injected false claims fully falsifiable and reduced audit search effort compared with unstructured answers; citation-id-only ledgers remained vulnerable under adversarial corruption.

## Why it stopped

No-paper useful signal: the result is a synthetic/proxy mechanism test, not a full validation of agent reliability in real deployments.

## Recommended next action

Run a bounded real-agent follow-up on 100-300 retrieval-grounded QA tasks comparing no-ledger, citation-only ledger, and strict evidence-ledger validators on false-claim recall, false-positive rate, and human audit time.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Strict Evidence Ledger Audit Benchmark
- Success threshold: Strict evidence-ledger validation improves false-claim recall by at least 25 percentage points over citation-only ledgers while keeping false-positive rate under 10% and reducing median audit actions per claim versus unstructured answers.
- Stop condition: Stop if strict validation fails to improve recall by 10 percentage points over citation-only validation, exceeds 20% false-positive rate, or requires more human audit actions than unstructured review on the median task.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
