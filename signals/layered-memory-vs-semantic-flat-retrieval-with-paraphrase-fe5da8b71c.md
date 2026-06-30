# Layered Memory vs Semantic Flat Retrieval With Paraphrase and Realistic Extraction Errors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-vs-semantic-flat-retrieval-with-paraphrase-fe5da8b71c`
Run ID: `layered-memory-vs-semantic-flat-retrieval-with-paraphrase-fe5da8b71c-20260620T000009131420+0000`

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

- Parent run decision: Layered Agent Memory vs Flat Retrieval on Multi-Session Tasks: enoch://control-plane/projects/layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6/runs/layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6-20260619T231801631829+0000
- Parent run decision: Layered Memory With Noisy Extraction vs Temporal Flat Retrieval: enoch://control-plane/projects/layered-memory-with-noisy-extraction-vs-temporal-flat-retr-8137fdb8cd/runs/layered-memory-with-noisy-extraction-vs-temporal-flat-retr-8137fdb8cd-20260619T233931759567+0000

## What looked useful

Layered entity+relation retrieval produced mean recall@1 of 0.7041 at 10% simulated extraction error, 0.4924 at 20%, 0.3462 at 30%, and 0.2508 at 40%, compared with the best flat baseline at 0.1615. Ablations showed entity-only and relation-only layers were weaker, and oracle extraction stayed at 1.0000, indicating the mechanism is sensitive to extraction quality but not just a smoke-test artifact.

## Boundaries and scale limits

The corpus, paraphrases, and extraction errors are synthetic. The dense semantic baseline is LSA/SVD over TF-IDF rather than a transformer embedding model. No real information-extraction model or real memory corpus was evaluated.

## Claim scope

In a deterministic synthetic memory benchmark with 2,504 fact memories, 5,008 paraphrased queries per seed, five fixed seeds, and simulated extraction-error rates from 0% to 40%, layered entity+relation retrieval improved recall@1 and MRR over flat TF-IDF, char TF-IDF, dense LSA, and hybrid LSA+char retrieval.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism but is not publication-grade because the decisive failure mode, extraction quality, was simulated rather than measured on real extracted memories.

## Recommended next action

Stop this run as no-paper useful signal; next run should repeat the protocol on a real memory/QA corpus with a real extractor and a transformer embedding baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Layered Memory Retrieval With Actual Extraction Errors
- Success threshold: Mean recall@1 improvement of at least 0.10 over the best flat transformer or lexical baseline across at least three fixed seeds, with no recall@5 regression larger than 0.02 and with reported real extractor error rates.
- Stop condition: Stop as negative if layered entity+relation retrieval fails to beat the best flat baseline by 0.05 recall@1 at measured extractor error rates, or if gains disappear when entity-only/relation-only controls are included.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-semantic-flat-retrieval-with-paraphrase-fe5da8b71c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
