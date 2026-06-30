# Evidence-Ledger Mandate for Tool-Using Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-mandate-for-tool-using-agents-794ea2d7eb52`
Run ID: `evidence-ledger-mandate-for-tool-using-agents-794ea2d7eb52-20260629T135742220114+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0b7c62679c96

## What looked useful

Mandatory claim-to-evidence ledgers made seeded missing, unknown, wrong-source, mismatched-observation, unsupported-derived, and stale-evidence faults mechanically detectable in controlled tool-use traces. A weak final-answer-only gate accepted all seeded invalid traces.

## Boundaries and scale limits

Synthetic traces only; no real LLM agents, real external tools, human adjudication, private operator traces, open-ended semantic claims, or long-horizon multi-turn workflows were evaluated.

## Claim scope

In a deterministic synthetic benchmark of 200 tool-use traces with typed exact and comparison claims, a strict evidence-ledger gate rejected all seeded unsupported claims while accepting all valid traces.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and not a broad validation of real tool-using agents.

## Recommended next action

Run a bounded real-agent transcript evaluation with blinded labels and the same strict ledger gate before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence-ledger gate on blinded tool-use transcripts
- Success threshold: False accept rate reduced by at least 50% relative to baseline, with false reject rate no more than 10 percentage points above baseline on valid supported claims.
- Stop condition: Stop if the strict ledger gate fails to reduce false accepts by 25% or more, or if false rejects exceed baseline by more than 20 percentage points in the first 30 labeled transcripts.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-mandate-for-tool-using-agents-794ea2d7eb52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
