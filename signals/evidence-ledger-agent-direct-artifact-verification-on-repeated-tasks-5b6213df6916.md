# Evidence-Ledger Agent: Direct Artifact Verification on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916`
Run ID: `evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916-20260621T093532303887+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Direct artifact verification reduced invalid-artifact false acceptance from 39/39 under a claim-only baseline to 0/39 on the seeded repeated-task benchmark, with 0/81 false rejects.

## Boundaries and scale limits

Synthetic artifacts only; no real LLM/tool-agent trajectories, no adversarial metadata tampering beyond digest/content mismatch, and no human operator outcome measurement.

## Claim scope

In a deterministic synthetic repeated-task benchmark with 120 text artifacts, direct artifact verification by path, content, and sha256 rejected all seeded stale/corrupted artifacts that a claim-only done-status baseline accepted.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct real-agent validation or publication-grade evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should replay real tool-using agent trajectories with hidden repeated-task drift traps through the same verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent repeated-task drift ledger verification
- Success threshold: At least 80% relative reduction in false accepts versus claim-only review and no more than 5% false rejects on valid artifacts.
- Stop condition: Stop if direct verification fails to reduce false accepts by at least 50% or rejects more than 10% of valid artifacts in the real-agent corpus.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-direct-artifact-verification-on-repeated-tasks-5b6213df6916`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
