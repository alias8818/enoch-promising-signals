# Constrained Evidence Ledger Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `constrained-evidence-ledger-agent-5664a4c79317`
Run ID: `constrained-evidence-ledger-agent-5664a4c79317-20260523T045104370199+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Across 5,000 cases per setting, the admissible-only ledger reduced false assertion rates from 19.54%, 39.68%, and 59.94% to 0% at adversarial rates 0.25, 0.50, and 0.75, with coverage of 97.5%, 94.74%, and 91.8%. Bootstrap intervals for false-assertion deltas were strictly negative.

## Boundaries and scale limits

Synthetic templated facts only; deterministic policies rather than real LLM agents; simple top-k retrieval simulation; source admissibility is supplied by tags; no real-corpus, human-labeled, or long-horizon agent evaluation.

## Claim scope

In a deterministic synthetic document-QA benchmark with explicit source admissibility tags and controlled inadmissible contradictions, an admissible-entry evidence ledger reduced false assertions versus an unconstrained first-hit reader while preserving at least 91.8% coverage.

## Why it stopped

No-paper useful signal: the local synthetic proxy supports the mechanism but is not direct/full validation of real LLM-agent behavior.

## Recommended next action

Run a bounded LLM-backed follow-up on a small real or semi-real corpus to test whether admissible evidence-ledger constraints still reduce false assertions when extraction and retrieval are imperfect.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-backed admissible evidence ledger on real-document QA
- Success threshold: At least 40% relative false-assertion reduction versus the prompting-only citation baseline at coverage >= 75%, with manually auditable examples showing ledger constraints caused the correction or abstention.
- Stop condition: Stop if extraction errors or retrieval misses dominate so that ledger constraints cannot be isolated, or if false-assertion reduction is below 20% at coverage above 75%.

## Evidence references

- Artifact root: `<local-path>/projects/constrained-evidence-ledger-agent-5664a4c79317`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
