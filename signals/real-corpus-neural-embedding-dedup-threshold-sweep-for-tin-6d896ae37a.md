# Real-corpus neural-embedding dedup threshold sweep for tiny GPT pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-neural-embedding-dedup-threshold-sweep-for-tin-6d896ae37a`
Run ID: `real-corpus-neural-embedding-dedup-threshold-sweep-for-tin-6d896ae37a-20260614T093252096679+0000`

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

- Parent run decision: Embedding-dedup threshold sweep for tiny pretraining: enoch://control-plane/projects/embedding-dedup-threshold-sweep-for-tiny-pretraining-73f53ee98730/runs/embedding-dedup-threshold-sweep-for-tiny-pretraining-73f53ee98730-20260614T091200768413+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/665fad9cd7d2

## What looked useful

Moderate semantic embedding dedup thresholds removed substantial document mass and degraded tiny GPT validation loss under equal-step training; very high threshold 0.98 removed little data and did not show a robust benefit.

## Boundaries and scale limits

Test used 1,200 training paragraphs, 220 validation paragraphs, a 4-layer 128-width GPT-style model, 240 training steps per variant, and a simple greedy embedding dedup implementation. It did not test larger corpora, GPT-2-small-class models, long convergence, exact/hash dedup controls, or publication-grade robustness.

## Claim scope

On a Tier 1 WikiText-2 tiny GPT pretraining test with bert-tiny neural embeddings, greedy cosine dedup at 0.90 and 0.95 consistently worsened held-out validation loss versus no dedup across three seeds; 0.98 was effectively neutral and seed-sensitive.

## Why it stopped

Tier 1 direct small real-corpus validation found consistent degradation at 0.90/0.95 and no robust win at 0.98, so the threshold-sweep idea is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; if deepened, test only the high-threshold near-duplicate regime with exact/hash dedup controls and both equal-compute and equal-unique-token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: High-threshold neural near-duplicate dedup versus exact dedup under fair token budgets
- Success threshold: A high-threshold neural dedup setting improves mean held-out validation loss by at least 0.01 versus no dedup and exact/hash dedup in at least three seeds without removing more than 10% of documents.
- Stop condition: Stop if no high-threshold setting beats both controls on mean validation loss, or if improvements appear only under one budget accounting mode.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-neural-embedding-dedup-threshold-sweep-for-tin-6d896ae37a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
