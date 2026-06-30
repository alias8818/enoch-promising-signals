# Layered memory with operator-doctrine updates vs flat retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-with-operator-doctrine-updates-vs-flat-retrieval-8006d4c97c50`
Run ID: `layered-memory-with-operator-doctrine-updates-vs-flat-retrieval-8006d4c97c50-20260621T170538257598+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73774bf46032

## What looked useful

Layered doctrine state scored 24/24 versus flat retrieval at 18/24 and transcript search at 21/24, showing that explicit update/supersession state can prevent stale or noisy retrieval hits in this bounded replay setting.

## Boundaries and scale limits

Synthetic tasks only; no production traces, embeddings, LLM generation, adversarial paraphrases, long-horizon sessions, or statistical replication beyond the fixed 24-query replay set.

## Claim scope

On 12 synthetic deterministic replay episodes with explicit doctrine keys and superseding operator updates, layered doctrine memory avoided stale-rule retrieval failures and exceeded flat token-overlap retrieval by 0.25 accuracy.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and mechanism-level, not direct production or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with embedding retrieval plus LLM answer generation on larger paraphrased replay traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding-and-LLM replay test for layered doctrine memory
- Success threshold: Layered doctrine memory accuracy >= flat embedding retrieval accuracy + 0.15 with no increase in doctrine-staleness failures.
- Stop condition: Stop if the layered method fails to beat flat embedding retrieval by 0.05 accuracy or if most wins disappear under paraphrased queries.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-with-operator-doctrine-updates-vs-flat-retrieval-8006d4c97c50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
