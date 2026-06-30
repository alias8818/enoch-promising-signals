# Real-agent repeated-task drift ledger verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-repeated-task-drift-ledger-verification-a65d7d34c3`
Run ID: `real-agent-repeated-task-drift-ledger-verification-a65d7d34c3-20260621T095552837786+0000`

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

- Parent run decision: Evidence-Ledger Agent: Direct Artifact Verification on Repeated Tasks: enoch://control-plane/projects/evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916/runs/evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916-20260621T093532303887+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

The ledger mechanism passed the predeclared small direct threshold: recall 1.000, false positive rate 0.000, and recall lift 0.500 over the best baseline. Baselines missed subtle constraint drift or over-flagged stable paraphrases.

## Boundaries and scale limits

Small deterministic Tier 1 corpus only; not live real-agent deployment evidence, not noisy LLM extraction evidence, not long-horizon production persistence, and not publication-grade validation.

## Claim scope

In a 20-task controlled replay corpus with explicit constraint labels, a structured repeated-task drift ledger detected all 12 drift cases with zero false positives and exceeded transcript-search and flat-retrieval baselines by at least 0.50 drift recall.

## Why it stopped

Controlled Tier 1 mechanism support was achieved, but this run remains no-paper because it used deterministic labeled replay rather than real-agent traces or live memory extraction.

## Recommended next action

Run a bounded deepen follow-up on at least 100 real agent repeated-task traces with verified drift labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real agent trace validation for repeated-task drift ledgers
- Success threshold: Ledger drift recall >= 0.85, false positive rate <= 0.10, and drift recall lift >= 0.20 over the best baseline on real agent traces.
- Stop condition: Stop if ledger recall falls below 0.70 or false positive rate exceeds 0.20 after the first 50 labeled real-agent episodes.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-repeated-task-drift-ledger-verification-a65d7d34c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
