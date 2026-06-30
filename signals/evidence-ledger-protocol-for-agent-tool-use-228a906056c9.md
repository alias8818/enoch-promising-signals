# Evidence Ledger Protocol for Agent Tool-Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-protocol-for-agent-tool-use-228a906056c9`
Run ID: `evidence-ledger-protocol-for-agent-tool-use-228a906056c9-20260619T022652426655+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/efec7b54c810

## What looked useful

The scaffold was converted from placeholders into an executable verifier and labeled corpus. The verifier matched 9/9 expected accept/reject verdicts and 5/5 named failure-case reasons with zero structural errors.

## Boundaries and scale limits

Synthetic corpus only: 9 labeled claims and 6 evidence entries. No real LLM tool-use traces, no human annotation study, and no comparison against ungated narrative audit baselines.

## Claim scope

A dependency-free evidence-ledger verifier can enforce explicit claim-to-evidence references, evidence quality thresholds, missing-reference rejection, unrelated-evidence rejection, and contradiction rejection on a small synthetic corpus.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic protocol test rather than direct validation on real agent tool-use traces.

## Recommended next action

Run a bounded deepen follow-up on real tool-using LLM traces with hidden drift/trap labels and compare false accept/reject rates against an ungated narrative baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real trace validation for evidence-ledger tool-use claim gating
- Success threshold: At least 30 labeled traces, at least 20 trap/unsupported claims, and a false-accept reduction of 30% or more versus the baseline without more than a 10% absolute increase in false rejects.
- Stop condition: Stop if the verifier cannot reduce false accepts by at least 10% on the first 10 labeled traces or if trace labels cannot be made reproducible and non-private.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-protocol-for-agent-tool-use-228a906056c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
