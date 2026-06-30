# Agent Memory with Semantic Compression and Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-with-semantic-compression-and-operator-doctrine-8a86fffac1db`
Run ID: `agent-memory-with-semantic-compression-and-operator-doctrine-8a86fffac1db-20260619T221506561166+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/81e1a396ab58

## What looked useful

Across five seeds, layered_doctrine_memory reached 0.833 mean accuracy versus 0.814 for flat_retrieval and 0.523 for transcript_search, with 0 false recall and lower doctrine violation rate than flat retrieval.

## Boundaries and scale limits

Synthetic symbolic replay only; no real operator corpus, no LLM answer generation, no production trace latency/token measurement, and no large-scale multi-domain validation.

## Claim scope

In a deterministic synthetic repeated-agent replay harness, layered semantic memory with operator-doctrine priority improves accuracy modestly over flat retrieval and substantially reduces retrieved memory footprint versus raw transcript search.

## Why it stopped

Closed as no-paper useful proxy evidence; the result supports the mechanism directionally but does not validate it on real agent behavior or human/operator data.

## Recommended next action

Run a bounded direct replay follow-up with an LLM answerer on realistic repeated-agent transcripts, comparing the same four memory strategies on recall, doctrine compliance, false recall, token cost, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM transcript replay for layered operator-doctrine memory
- Success threshold: Layered doctrine memory beats flat retrieval by at least 1 absolute accuracy point, has equal or lower doctrine violation rate, and uses at least 25% fewer retrieved tokens on a minimum of 500 scored LLM replay queries.
- Stop condition: Stop as negative if layered doctrine memory fails to beat flat retrieval on accuracy or doctrine violations, or if its token savings disappear under realistic transcript retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-with-semantic-compression-and-operator-doctrine-8a86fffac1db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
