# Operator-Doctrine Memory vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-dc0b9ac0dcc9`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-dc0b9ac0dcc9-20260611T013822310162+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

Flat retrieval matched doctrine memory at 100% accuracy on the literal-term control. In the paraphrased-current stress condition, flat TF-IDF retrieval had 0% coverage/accuracy at k=5 and k=50, while doctrine memory had 100% coverage/accuracy by retrieving the normalized operator-domain rule group.

## Boundaries and scale limits

No real doctrine corpus, no human-authored queries, no embedding retriever/reranker, no LLM-in-the-loop answering, and no multi-turn memory persistence were tested. The stress win is a proxy for canonicalization and structure, not a full validation of operator-doctrine memory.

## Claim scope

Synthetic local benchmark of operator/domain doctrine lookup with current-vs-retired rules, distractors, and a paraphrased-current stress condition. Structured doctrine memory helped only when normalized fields preserved current rule identity that flat lexical retrieval could not recover.

## Why it stopped

Proxy evidence is mixed: the broad claim is not supported because flat retrieval is perfect when canonical terms match, and the positive mechanism result depends on a synthetic paraphrase/noise stress condition rather than direct real-corpus evidence.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on a small human-authored doctrine corpus with BM25, embedding retrieval, reranking, and the same structured-memory adjudicator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored doctrine corpus test for structured memory under stale-rule distractors
- Success threshold: Structured doctrine memory exceeds the best flat baseline by at least 10 absolute accuracy points at equal or lower mean context tokens, with no more than 2 percentage points regression on literal-term queries.
- Stop condition: Stop as unsupported if embedding/reranked flat retrieval matches structured memory within 5 accuracy points at comparable context size, or if structured extraction cannot reliably identify current rules.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-dc0b9ac0dcc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
