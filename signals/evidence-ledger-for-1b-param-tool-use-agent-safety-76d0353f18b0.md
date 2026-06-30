# Evidence Ledger for 1B Param Tool-Use Agent Safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-1b-param-tool-use-agent-safety-76d0353f18b0`
Run ID: `evidence-ledger-for-1b-param-tool-use-agent-safety-76d0353f18b0-20260529T204343609515+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/03809f7c3eca

## What looked useful

Unsigned hash-chain ledgers raised synthetic unsafe-trace recall from 0.25 to 0.875 but missed all coherent fabricated-ledger attacks; authenticated tool receipts achieved 1.0 recall and 0.0 false-positive rate on the tested synthetic attacks with about 0.052 ms mean validation latency.

## Boundaries and scale limits

No real 1B parameter model, real tool API, production logging system, human adversary, or large-scale serving workload was tested. Results are mechanism-level synthetic evidence, not model-safety validation.

## Claim scope

In a deterministic synthetic tool-use audit benchmark, evidence ledgers improved detection of trace-integrity, grounding, and denied-tool failures over final-answer-only checks, but unsigned ledgers failed against coherent fabricated evidence. Authenticated tool receipts closed that simulated failure mode.

## Why it stopped

Closed as no-paper useful signal: the result is a synthetic/proxy mechanism test and an early falsification of unsigned evidence ledgers as a sufficient safety boundary, not a full 1B model safety validation.

## Recommended next action

Run a bounded direct follow-up with a real approximately 1B tool-use model and verifier-held tool receipts, comparing unsigned versus authenticated traces under adversarial trace-authoring prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Authenticated Evidence Ledgers on Real 1B Tool-Use Traces
- Success threshold: Authenticated receipts improve unsafe-trace recall by at least 20 percentage points over unsigned ledgers with false-positive rate at or below 2% on benign traces.
- Stop condition: Stop if unsigned and authenticated ledgers perform within 5 percentage points of each other, or if benign false-positive rate exceeds 5% after fixing implementation bugs.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-1b-param-tool-use-agent-safety-76d0353f18b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
