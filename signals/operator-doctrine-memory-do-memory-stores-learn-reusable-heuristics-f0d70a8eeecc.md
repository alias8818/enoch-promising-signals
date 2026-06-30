# Operator-Doctrine Memory: Do Memory Stores Learn Reusable Heuristics?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-do-memory-stores-learn-reusable-heuristics-f0d70a8eeecc`
Run ID: `operator-doctrine-memory-do-memory-stores-learn-reusable-heuristics-f0d70a8eeecc-20260628T151441970129+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d78c17e285c4

## What looked useful

Two-environment doctrine induction reached 0.99318 aggregate mean accuracy versus 0.92234 for episodic kNN, 0.24899 for global majority, and 0.24897 for label-shuffled memory. At 16 traces per environment, doctrine induction reached 0.97408 versus 0.74138 for episodic kNN.

## Boundaries and scale limits

CPU-only synthetic benchmark; 100 seeds, four train sizes, 1000 held-out tasks per seed/size; no natural-language traces, no LLM agent, no long-horizon planning, and no production memory backend.

## Claim scope

Structured doctrine-memory induction learned reusable per-family operator-selection heuristics in a synthetic trace benchmark and transferred them to held-out shifted tasks; this does not validate arbitrary memory stores or LLM operator memory.

## Why it stopped

Closed as no-paper useful signal: the local synthetic probe supports the mechanism but is proxy evidence, not direct validation of broad operator-doctrine memory claims.

## Recommended next action

Run a bounded natural-language trace follow-up where a small agent writes doctrine memories from solved tasks and must apply them to held-out task families, with memory-disabled and shuffled-memory controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language operator doctrine transfer benchmark
- Success threshold: Doctrine memory improves held-out task success by at least 10 percentage points over episodic retrieval and at least 25 percentage points over shuffled memory across 50 or more paired seeds.
- Stop condition: Stop if doctrine memory fails to beat episodic retrieval by 5 percentage points after 50 paired seeds or if generated memories cannot be parsed/applied reliably enough for a controlled comparison.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-do-memory-stores-learn-reusable-heuristics-f0d70a8eeecc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
