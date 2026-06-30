# Natural-language replay test for volunteer memory ledger updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-replay-test-for-volunteer-memory-ledger-u-98e626ac00`
Run ID: `natural-language-replay-test-for-volunteer-memory-ledger-u-98e626ac00-20260628T063554734349+0000`

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

- Parent run decision: Memory Ledger for Volunteer Coordination Agent: enoch://control-plane/projects/memory-ledger-for-volunteer-coordination-agent-877368b778a1/runs/memory-ledger-for-volunteer-coordination-agent-877368b778a1-20260628T053922119667+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/befc816e0544

## What looked useful

Template-like volunteer ledger updates replayed exactly, but realistic paraphrases and corrections missed enough events to reduce aggregate event accuracy to 0.543, ledger field accuracy to 0.583, and final-state exactness to 0.333 against a strict exact-replay threshold.

## Boundaries and scale limits

Three synthetic scenarios, 46 total updates, no real volunteer organization data, no LLM extractor, and no long-horizon replay. This is Tier 1 direct local evidence only.

## Claim scope

In a small controlled volunteer memory ledger replay benchmark, exact replay succeeds for near-template natural-language updates but fails for operational paraphrases, corrections, indirect phrasing, and shorthand when using a deterministic grammar-style extractor.

## Why it stopped

Controlled Tier 1 direct test failed the stated exact-replay threshold; this is an early falsification of simple deterministic natural-language replay, not full validation of all possible natural-language replay systems.

## Recommended next action

Run a bounded deepen test comparing a schema-constrained LLM/event extractor against this deterministic parser on at least 100 held-out volunteer ledger updates with corrections and paraphrases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Schema-constrained extractor test for volunteer ledger natural-language replay
- Success threshold: >= 0.90 event extraction accuracy, >= 0.95 ledger field accuracy, and 1.0 final-state exact rate on the held-out small-ledger benchmark.
- Stop condition: Stop if the schema-constrained extractor misses final-state exactness on more than one small ledger or falls below 0.90 event accuracy after ambiguity rules are fixed.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-replay-test-for-volunteer-memory-ledger-u-98e626ac00`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
