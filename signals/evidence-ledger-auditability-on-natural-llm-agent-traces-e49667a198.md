# Evidence Ledger Auditability on Natural LLM Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-auditability-on-natural-llm-agent-traces-e49667a198`
Run ID: `evidence-ledger-auditability-on-natural-llm-agent-traces-e49667a198-20260524T212401560112+0000`

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

- Parent run decision: Real-Agent Evidence Ledger Trace Benchmark: enoch://control-plane/projects/real-agent-evidence-ledger-trace-benchmark-fe07925f79/runs/real-agent-evidence-ledger-trace-benchmark-fe07925f79-20260524T211351445492+0000
- Parent run decision: Low-Memory Agent Evidence Ledger: enoch://control-plane/projects/low-memory-agent-evidence-ledger-521c7369895f/runs/low-memory-agent-evidence-ledger-521c7369895f-20260524T205907430216+0000

## What looked useful

Across three fixed seeds and 1,800 total cases, ledger_full achieved precision 1.00, recall 1.00, and clean false-positive rate 0.00; the raw-transcript baseline achieved precision 1.00, recall 0.20, and clean false-positive rate 0.00. Ablations showed hash removal reduced recall to 0.40 and support-check removal reduced recall to 0.60.

## Boundaries and scale limits

Validation used deterministic injected faults over natural traces, not independently labeled naturally occurring defects; no human adjudication or external agent-trace corpus was used.

## Claim scope

On 80 local natural Codex agent JSONL traces with 6,578 events and 4,232 command events, a hash-chained evidence ledger with explicit support facts detected seeded trace-integrity and support-fault injections better than a raw-transcript baseline.

## Why it stopped

Mechanism supported under Tier 2 local seeded-fault validation, but evidence is not paper-positive because labels are injected and the corpus is local Enoch traces.

## Recommended next action

Stop this branch as no-paper useful-signal evidence; the next meaningful deepen test is blinded adjudication on naturally occurring defects rather than more injected local faults.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Human Adjudication of Evidence-Ledger Flags on Natural Agent Trace Defects
- Success threshold: Ledger recall at least 25 percentage points above raw-transcript baseline with clean/control false-positive rate no more than 10 percentage points higher, on at least 200 independently adjudicated trace-defect cards.
- Stop condition: Stop if blinded adjudication shows less than 10 percentage points recall improvement or more than 10 percentage points false-positive-rate regression versus raw transcript review.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditability-on-natural-llm-agent-traces-e49667a198`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
