# Memory Ledger for Volunteer Coordination Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-ledger-for-volunteer-coordination-agent-877368b778a1`
Run ID: `memory-ledger-for-volunteer-coordination-agent-877368b778a1-20260628T053922119667+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/befc816e0544

## What looked useful

Ledger memory achieved 1.0000 assignment match rate, 0.0000 constraint violation rate, and 1.0000 state-probe accuracy, matching full transcript reconstruction while avoiding 235.54 historical event scans/request and using 2.75x fewer serialized bytes/request. Recency windows were smaller but produced stale-state assignment violations of 22.1% to 28.5%.

## Boundaries and scale limits

Tested only on synthetic structured events: 200 seeds, 60 volunteers, 600 events per seed, 37,787 requests. No natural-language extraction, real volunteer data, live operator workflow, privacy deletion, or LLM-agent behavior was validated.

## Claim scope

In a deterministic synthetic volunteer-coordination stream with structured updates, a persistent current-state memory ledger matched full transcript reconstruction on assignment correctness and state probes while reducing per-request context scans and serialized context bytes.

## Why it stopped

No-paper useful signal: the result supports the structured-ledger mechanism only in a synthetic deterministic benchmark, not a direct real-world or LLM-agent validation.

## Recommended next action

Run a bounded natural-language replay follow-up where an LLM or extractor writes ledger updates from messy volunteer messages and is compared against transcript retrieval under equal token/cost budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language replay test for volunteer memory ledger updates
- Success threshold: Ledger-based agent reaches at least 0.90 assignment match rate, less than 0.05 constraint violation rate, and at least 2x lower context/token cost than full transcript retrieval without materially worse deletion/update handling.
- Stop condition: Stop if natural-language extraction errors cause ledger assignment match rate below 0.80 or constraint violation rate above 0.10 on two independent prompt/extractor settings.

## Evidence references

- Artifact root: `<local-path>/projects/memory-ledger-for-volunteer-coordination-agent-877368b778a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
