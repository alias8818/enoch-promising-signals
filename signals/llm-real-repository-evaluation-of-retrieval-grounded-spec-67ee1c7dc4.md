# LLM Real-Repository Evaluation of Retrieval-Grounded Spec Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-real-repository-evaluation-of-retrieval-grounded-spec-67ee1c7dc4`
Run ID: `llm-real-repository-evaluation-of-retrieval-grounded-spec-67ee1c7dc4-20260621T105353723633+0000`

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

- Parent run decision: Retrieval-Based Spec Draft from Local Document Store: enoch://control-plane/projects/retrieval-based-spec-draft-from-local-document-store-6fb35da485b7/runs/retrieval-based-spec-draft-from-local-document-store-6fb35da485b7-20260621T100602031200+0000
- Parent run decision: Real-Corpus Evaluation of Retrieval-Grounded Spec Drafting: enoch://control-plane/projects/real-corpus-evaluation-of-retrieval-grounded-spec-drafting-9c501ca3e5/runs/real-corpus-evaluation-of-retrieval-grounded-spec-drafting-9c501ca3e5-20260621T102222712619+0000

## What looked useful

BM25 retrieval recovered some gold changed files (mean retrieval recall 0.2847) but generated spec changed-file recall was only 0.0972 versus 0.0833 for no retrieval, with paired bootstrap CI spanning zero; oracle context reached 0.4583 file recall, indicating retrieval/context selection is the bottleneck.

## Boundaries and scale limits

Two public repositories, 12 commit-derived tasks, one small local code LLM, deterministic greedy decoding, file/term recall metrics only, no human spec-quality judgments, no issue-to-PR benchmark, and no multi-model replication.

## Claim scope

On 12 real held-out commits from click and rich, Qwen/Qwen2.5-Coder-1.5B-Instruct with BM25 file retrieval did not materially improve implementation-spec changed-file recall over a no-retrieval baseline; oracle file context substantially improved file recall.

## Why it stopped

Medium local validation found mixed/negative direct metrics for BM25 retrieval-grounded spec drafting; evidence supports a retrieval bottleneck mechanism but not publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded deepen follow-up with code-aware retrieval on at least 40 real tasks and a pre-registered +0.15 changed-file recall threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Code-Aware Retrieval for Real-Repository Spec Drafting
- Success threshold: Code-aware retrieval beats no retrieval by >=0.15 paired changed-file recall and beats BM25 by >=0.10, with no negative paired gold-term recall delta.
- Stop condition: Stop if code-aware retrieval fails either recall threshold or reduces gold-term recall, or if oracle context no longer improves over no retrieval on the expanded task set.

## Evidence references

- Artifact root: `<local-path>/projects/llm-real-repository-evaluation-of-retrieval-grounded-spec-67ee1c7dc4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
