# Streaming KV Eviction by Cumulative Attention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `streaming-kv-eviction-by-cumulative-attention-a21a1bef34bd`
Run ID: `streaming-kv-eviction-by-cumulative-attention-a21a1bef34bd-20260608T042803356341+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/51f62cf8b7b9

## What looked useful

Cumulative-attention eviction consistently beat recency at all tested budgets and offsets; it beat seeded random on the 1024-token sweep and beat five-seed random means on 512-token offset checks, but remained far worse than a full-cache reference and showed mixed single-seed comparisons at budget 128.

## Boundaries and scale limits

Single small pretrained decoder, WikiText-2 only, short windows, inference-only teacher-forced NLL, Python cache slicing, no production serving throughput test, no long-context downstream tasks, and no larger-model replication.

## Claim scope

On distilgpt2 streaming teacher-forced WikiText-2 windows of 512-1024 tokens, cumulative-attention KV eviction improves next-token NLL versus sliding-window recency and the mean of seeded random eviction, especially at 16-64 token KV budgets.

## Why it stopped

Bounded local evidence supports the mechanism but is too narrow and mixed for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a multi-model, multi-corpus deepen test with random-seed controls and an overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model robustness test for cumulative-attention KV eviction
- Success threshold: Cumulative attention beats recency and random-seed mean NLL on at least 80% of model-corpus-budget cells and has less than 20% runtime overhead versus recency in the same Python or serving harness.
- Stop condition: Stop if cumulative attention fails to beat random-seed mean on more than half of cells or if score-maintenance overhead exceeds 50% without a compensating NLL gain.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-kv-eviction-by-cumulative-attention-a21a1bef34bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
