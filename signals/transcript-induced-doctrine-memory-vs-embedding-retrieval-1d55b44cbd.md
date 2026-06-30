# Transcript-Induced Doctrine Memory vs Embedding Retrieval for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `transcript-induced-doctrine-memory-vs-embedding-retrieval-1d55b44cbd`
Run ID: `transcript-induced-doctrine-memory-vs-embedding-retrieval-1d55b44cbd-20260611T075947993268+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on Repeated Agent Tasks: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-82b33427e799/runs/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-82b33427e799-20260611T063301820911+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

Retrieval top-3 supplied the governing rule on 100% of paired tickets and achieved 47.9% exact accuracy versus 5.6% for transcript context; retrieval won 69 discordant pairs versus 8 transcript-only wins, sign-test p=3.14e-13. A no-distractor transcript ablation still favored retrieval by 37.5 percentage points.

## Boundaries and scale limits

Three synthetic seeds, 144 paired tickets, one compact local instruction model, simple hashed word/bigram embeddings, exact action-token scoring, and no real organizational transcripts or production vector database.

## Claim scope

In a synthetic repeated-agent doctrine benchmark using Qwen/Qwen2.5-0.5B-Instruct on GB10, top-3 hashed embedding retrieval substantially outperformed full transcript doctrine context for exact action selection.

## Why it stopped

Tier 1 direct evidence produced a useful no-paper signal: transcript-induced doctrine context was not competitive with embedding retrieval in this controlled setting, but the evidence is too synthetic and model-limited for publication-grade closure.

## Recommended next action

Run a bounded deepen follow-up with stronger local models and realistic multi-turn traces to test whether the transcript deficit persists beyond this compact-model synthetic benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-Scale and Trace-Realism Check for Doctrine Retrieval Advantage
- Success threshold: Retrieval beats transcript-only by at least 15 percentage points paired exact accuracy on 200 or more paired realistic-trace tickets while maintaining at least 95% retrieval hit rate and lower prompt-token cost.
- Stop condition: Stop if transcript-only matches retrieval within 5 percentage points across stronger models, if retrieval hit rate drops below 90% under realistic traces, or if both methods remain below 50% exact accuracy due to model/output-format failure.

## Evidence references

- Artifact root: `<local-path>/projects/transcript-induced-doctrine-memory-vs-embedding-retrieval-1d55b44cbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
