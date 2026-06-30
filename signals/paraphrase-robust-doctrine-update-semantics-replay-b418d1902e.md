# Paraphrase-robust doctrine update semantics replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `paraphrase-robust-doctrine-update-semantics-replay-b418d1902e`
Run ID: `paraphrase-robust-doctrine-update-semantics-replay-b418d1902e-20260629T032209213579+0000`

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

- Parent run decision: Natural-language doctrine memory replay with inferred update semantics: enoch://control-plane/projects/natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d/runs/natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d-20260629T014616125618+0000
- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on Repeated Tasks: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c/runs/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c-20260629T012802002978+0000

## What looked useful

Across five seeds and 2160 task evaluations per strategy, layered doctrine memory averaged 0.9278 accuracy versus 0.3884 for the strongest baseline, with mean absolute gain 0.5394. The primary seed scored 0.9190 versus 0.3727.

## Boundaries and scale limits

Synthetic templates, hand-written synonym/canonicalization schema, no LLM agent, no real operator traces, no production memory backend, and no large-scale corpus validation.

## Claim scope

In a deterministic synthetic replay benchmark with 2-4 conflicting doctrine updates per task and paraphrased queries, layered doctrine memory using canonical slots plus latest-update semantics substantially outperformed transcript search and flat retrieval baselines.

## Why it stopped

No-paper closure: the local synthetic benchmark supports the mechanism but is proxy evidence rather than direct/full validation of agent memory behavior.

## Recommended next action

Run a bounded deepen follow-up with held-out LLM-generated or real replay traces, replacing the hand-written canonicalizer with an embedding or model-based semantic mapper while preserving the same latest-update oracle.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-trace paraphrase doctrine replay with latest-update oracle
- Success threshold: At least 500 held-out tasks, layered memory accuracy at least 0.85, and at least 0.20 absolute gain over the strongest non-layered retrieval baseline.
- Stop condition: Stop as unsupported if layered memory accuracy is below 0.70 or its absolute gain over the strongest retrieval baseline is below 0.10 on the held-out corpus.

## Evidence references

- Artifact root: `<local-path>/projects/paraphrase-robust-doctrine-update-semantics-replay-b418d1902e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
