# Evidence Ledger Protocol for Tool-Use Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-protocol-for-tool-use-agents-ce245d4b6f70`
Run ID: `evidence-ledger-protocol-for-tool-use-agents-ce245d4b6f70-20260621T181337298802+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/52274d0f1558

## What looked useful

The ledger validator achieved precision 1.0, recall 1.0, and F1 1.0 on 30,000 synthetic validation cases, while the transcript baseline achieved precision 1.0, recall 0.6, and F1 0.75 because it missed all tampered-output and reordered-chain cases.

## Boundaries and scale limits

Synthetic traces only; no real LLM tool agents, external tool APIs, concurrent tool streams, long-horizon workflows, signed remote attestations, or human/model-graded natural-language claim support.

## Claim scope

On generated two-tool traces with labeled corruption mutations, a hash-chained evidence ledger with explicit claim citations detects payload tampering and event reordering that a transcript-only citation baseline misses.

## Why it stopped

Synthetic bounded mechanism test supports the ledger idea but is not direct production-agent or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate the same ledger protocol on real tool-use agent traces with injected provenance faults and model/human claim-support grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent trace benchmark for evidence-ledger validation
- Success threshold: At least 0.90 recall, at least 0.95 precision, and a statistically clear recall improvement over transcript-only validation on realistic traces, with overhead low enough for interactive agent logging.
- Stop condition: Stop if ledger recall is below 0.80 on any core provenance-fault class, false-positive rate exceeds 0.10 on clean traces, or overhead makes interactive logging impractical.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-protocol-for-tool-use-agents-ce245d4b6f70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
