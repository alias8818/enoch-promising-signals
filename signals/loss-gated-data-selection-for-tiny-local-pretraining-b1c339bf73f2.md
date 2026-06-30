# Loss-gated data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `loss-gated-data-selection-for-tiny-local-pretraining-b1c339bf73f2`
Run ID: `loss-gated-data-selection-for-tiny-local-pretraining-b1c339bf73f2-20260612T231907373846+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5ed6553a91ed

## What looked useful

Mid-loss gating selected 83.55% target examples from a pool where random selection selected 50.15%, reduced target validation loss by 0.2007 on average versus random, and landed within 0.0500 target loss of a label-aware oracle. Low-loss and high-loss selection were both worse than random, matching the mechanism that too-easy and noisy examples are harmful.

## Boundaries and scale limits

Synthetic data only; 3 seeds; 2-layer 96-dim Transformer; 4096-example pool; 1536 selected examples; 220 target training steps; no real text corpus, tokenizer, downstream task, GPT-2-small-class model, or long-run validation.

## Claim scope

In a synthetic tiny-language-model pretraining proxy with easy, target, and random-noise sequence sources, a probe-model mid-loss gate enriched target-distribution examples and reduced held-out target next-token loss versus random equal-budget selection across three seeds.

## Why it stopped

No-paper closure because the result is a synthetic proxy useful signal, not direct evidence for real local pretraining or publication-grade validation.

## Recommended next action

Run a bounded real-corpus follow-up using the same probe-loss gate on a small local text corpus with equal-token random and quality-filter baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus bounded validation of mid-loss gated tiny pretraining
- Success threshold: Mid-loss gate beats random target validation loss on every seed with mean relative loss reduction of at least 2% and does not underperform the simple quality baseline by more than 1%.
- Stop condition: Stop as unsupported if the mid-loss gate fails to beat random on at least two of three seeds or if gains disappear when token budget and deduplication are controlled.

## Evidence references

- Artifact root: `<local-path>/projects/loss-gated-data-selection-for-tiny-local-pretraining-b1c339bf73f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
