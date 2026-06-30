# Operator-Doctrine Memory for Volunteer Coordination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-for-volunteer-coordination-857311ff4d77`
Run ID: `operator-doctrine-memory-for-volunteer-coordination-857311ff4d77-20260621T021433811568+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/656162164e51

## What looked useful

Across a five-seed sweep of 640 generated cases, layered_doctrine_memory achieved mean accuracy 1.000 versus mean best-baseline accuracy 0.647, with mean layered-minus-best-baseline accuracy 0.353. Main seed 857311 showed 128/128 layered accuracy versus 79/128 transcript_search and 72/128 flat_retrieval.

## Boundaries and scale limits

Synthetic generated cases only; no live volunteer data, no natural-language extraction, no privacy or human workflow validation, and no LLM-agent memory-write decisions were tested.

## Claim scope

On a deterministic synthetic volunteer-coordination replay benchmark with structured authoritative updates and stale conflicting notes, typed latest-state operator-doctrine memory outperformed no memory, transcript search, and flat retrieval on assignment accuracy.

## Why it stopped

Closed as useful no-paper proxy evidence because the result is synthetic and structurally favors typed latest-state memory; it is not a live or extraction-backed validation.

## Recommended next action

Run a bounded extraction-backed replay on natural-language volunteer coordination transcripts with matched retrieval budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Extraction-backed operator-doctrine memory on natural-language volunteer coordination replay
- Success threshold: At least 0.15 absolute accuracy improvement over the best baseline and at least 30% relative reduction in stale-conflict errors on 100 or more held-out natural-language cases.
- Stop condition: Stop if extractor precision on update facts is below 0.85 or layered memory improves by less than 0.05 absolute accuracy over the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-volunteer-coordination-857311ff4d77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
