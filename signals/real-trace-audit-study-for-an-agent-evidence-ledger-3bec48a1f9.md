# Real-trace audit study for an agent evidence ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9`
Run ID: `real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9-20260531T114810950760+0000`

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

- Parent run decision: Agent Evidence Ledger: enoch://control-plane/projects/agent-evidence-ledger-de8437d4cb37/runs/agent-evidence-ledger-de8437d4cb37-20260530T085611021728+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3158d7e70227

## What looked useful

On the frozen real trace, the ledger verifier achieved 63/63 correct controlled audit decisions, 0 false accepts, 0 false rejects, passed original hash-chain validation, and detected a deliberate exit-code mutation at ledger entry 1.

## Boundaries and scale limits

Single small trace snapshot with 40 JSONL rows, 12 command ledger entries, and 63 deterministic claims; no multi-agent traces, natural-language report audits, human/LLM auditor comparison, or adversarial omission tests.

## Claim scope

A deterministic append-only evidence ledger built from one frozen real Codex JSONL trace can verify controlled command/output audit claims, reject fabricated claims, and detect a simple ledger mutation.

## Why it stopped

Tier 1 direct real-trace threshold was met, but the evidence is a small controlled mechanism test and not publication-grade validation.

## Recommended next action

Run a bounded deepen study on at least 10 heterogeneous real agent traces with blinded raw-log versus ledger-assisted audit tasks before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded multi-trace audit benchmark for an agent evidence ledger
- Success threshold: Ledger-assisted auditing reaches at least 95% accuracy, no more than 2% false accepts on false or unsupported claims, and at least 20% lower median audit time than raw-log auditing on the bounded trace set.
- Stop condition: Stop if false accepts exceed 5% on the first 5 traces, if ledger construction fails on more than 20% of traces, or if ledger-assisted auditing is slower than raw-log auditing with no accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
