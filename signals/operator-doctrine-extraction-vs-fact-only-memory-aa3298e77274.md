# Operator-Doctrine Extraction vs Fact-Only Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-extraction-vs-fact-only-memory-aa3298e77274`
Run ID: `operator-doctrine-extraction-vs-fact-only-memory-aa3298e77274-20260610T194029429654+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

Doctrine extraction reached 0.925 mean OOD balanced accuracy versus 0.683 for kNN fact memory and 0.500 for exact-majority memory; random-label controls stayed at chance for both kNN and doctrine extraction.

## Boundaries and scale limits

The run used generated DNF-style doctrines over seven symbolic facts and 20 trials per condition. It did not test natural-language operator corpora, production LLM memory, messy workflow traces, or long-horizon adaptation.

## Claim scope

On a finite synthetic symbolic policy benchmark, greedy operator-doctrine extraction from examples generalizes better than exact or kNN fact-only memory on held-out role/region combinations, while showing no advantage on random-label controls.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct/full validation of real operator-doctrine memory systems.

## Recommended next action

Stop this run as a no-paper useful signal; next, test the same comparison on a small natural-language operator-case corpus with blinded held-out decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language operator doctrine extraction benchmark
- Success threshold: Doctrine memory improves held-out balanced accuracy by at least 10 percentage points over fact-only retrieval without increasing false positives by more than 5 percentage points.
- Stop condition: Stop if doctrine memory is within 3 balanced-accuracy points of fact-only retrieval or materially increases false positives on the held-out set.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-extraction-vs-fact-only-memory-aa3298e77274`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
