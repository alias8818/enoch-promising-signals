# Counter-example harvesting loop for retry success

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counter-example-harvesting-loop-for-retry-success-0815a6cb9a70`
Run ID: `counter-example-harvesting-loop-for-retry-success-0815a6cb9a70-20260628T020134722736+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7fccdab20de

## What looked useful

Counter-example harvesting reached 447/500 successes (0.894) versus 235/500 (0.470) for failure-note-only retries, 301/500 (0.602) for random retry, and 4/500 (0.008) for one-shot. The absolute gain over failure-note-only was 0.424.

## Boundaries and scale limits

500 synthetic tasks, 20 seeds, 4 retry attempts, symbolic candidate rules only; no live LLM agents, natural-language extraction, production retry traces, or large-scale operator-memory retrieval were tested.

## Claim scope

In a deterministic synthetic rule-induction replay with sparse initial observations, storing validation-derived counter-examples before retrying improves bounded retry success over failure-note-only and one-shot baselines.

## Why it stopped

No-paper closure: the mechanism is supported by synthetic/proxy evidence, but direct evidence on real agent retry behavior is required before any paper-positive claim.

## Recommended next action

Run a bounded deepen follow-up on real or LLM-generated retry transcripts where counter-examples must be extracted from natural-language failures and compared against matched failure-summary retries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language retry transcript counter-example harvesting
- Success threshold: Counter-example harvesting improves final success rate by at least 15 absolute percentage points over failure-summary retry with non-overlapping or clearly separated uncertainty intervals, without increasing mean attempts by more than 25%.
- Stop condition: Stop if extraction fails to produce valid concrete counter-examples on more than 40% of tasks or if the success-rate gain is below 5 absolute percentage points after the fixed corpus.

## Evidence references

- Artifact root: `<local-path>/projects/counter-example-harvesting-loop-for-retry-success-0815a6cb9a70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
