# Doctrine summaries vs indexed semantic retrieval on repeated agent traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `doctrine-summaries-vs-indexed-semantic-retrieval-on-repeat-a329e9b756`
Run ID: `doctrine-summaries-vs-indexed-semantic-retrieval-on-repeat-a329e9b756-20260621T152329075857+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on Repeated Agent Tasks: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-ca4a95357108/runs/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-ca4a95357108-20260621T145133593620+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66dd9f608611

## What looked useful

Doctrine summaries were context-efficient but routing to the correct doctrine family was brittle; full-trace retrieval beat doctrine-summary routing at every conflict level by 19.4 to 38.9 percentage points for the stronger doctrine TF-IDF condition.

## Boundaries and scale limits

Six synthetic repeated trace families, 24 training traces including distractors, 36 held-out traces per conflict level, five lexical-conflict levels, TF-IDF lexical retrieval rather than neural embedding retrieval, and action prediction rather than full agent task completion.

## Claim scope

In a controlled small repeated-agent-trace action-prediction test with dependency-free TF-IDF full-trace retrieval, compact doctrine summaries reduced context by about 87.6% but did not outperform indexed full-trace retrieval.

## Why it stopped

Small controlled direct lexical-index test falsified the success threshold; this is not a full semantic-retrieval validation.

## Recommended next action

Run a bounded deepen test with a real embedding index and an LLM or trained lightweight classifier for doctrine application before making any claim about semantic retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding retrieval versus LLM-applied doctrine summaries on repeated agent traces
- Success threshold: Doctrine-applied memory must beat neural embedding full-trace retrieval by at least 10 percentage points exact-action accuracy while preserving at least 50% context reduction on held-out repeated traces.
- Stop condition: Stop if embedding full-trace retrieval matches or beats all doctrine variants on two controlled corpora, or if doctrine context reduction comes only with more than 5 percentage points accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/doctrine-summaries-vs-indexed-semantic-retrieval-on-repeat-a329e9b756`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
