# Quality-Filtered Data Selection via Lightweight DSIR Proxy for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-filtered-data-selection-via-lightweight-dsir-proxy-for-gpt-2-small-df2eec305fa2`
Run ID: `quality-filtered-data-selection-via-lightweight-dsir-proxy-for-gpt-2-small-df2eec305fa2-20260619T035822018707+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f26d7f39e047

## What looked useful

DSIR-style relevance is not sufficient as a quality-filtered selector under target-keyword spam. A simple repetition/lexical quality prior can make the selector robust in this bounded proxy, so future GPT-2-small data-selection tests should include explicit quality gating.

## Boundaries and scale limits

Synthetic corpora only; no GPT-2-small continued pretraining, no real Common Crawl/OpenWebText-scale data, and no downstream neural LM validation or task accuracy.

## Claim scope

In a bounded synthetic adversarial candidate-pool test, unigram DSIR alone selected target-keyword spam, while DSIR combined with a lightweight quality prior recovered clean target examples and nearly matched an oracle on held-out target bigram bits/token.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and cannot validate GPT-2-small training quality.

## Recommended next action

Run a bounded real-data deepen test: apply random, quality-only, DSIR-only, and DSIR-plus-quality selection to a small public text mixture, then continue-pretrain GPT-2-small or a small matched causal LM for a fixed token budget and compare validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small DSIR-plus-quality selection probe
- Success threshold: DSIR-plus-quality must reduce held-out validation loss versus random and DSIR-only by at least 3% at matched token budget without higher repetition/spam diagnostics.
- Stop condition: Stop if DSIR-plus-quality fails to beat random or DSIR-only on validation loss, or if preprocessing/model runtime exceeds the bounded local budget without checkpointed evidence.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-data-selection-via-lightweight-dsir-proxy-for-gpt-2-small-df2eec305fa2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
