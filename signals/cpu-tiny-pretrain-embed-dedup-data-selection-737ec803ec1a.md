# CPU Tiny Pretrain Embed-Dedup Data Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-tiny-pretrain-embed-dedup-data-selection-737ec803ec1a`
Run ID: `cpu-tiny-pretrain-embed-dedup-data-selection-737ec803ec1a-20260521T203047816107+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d0704b980cfa

## What looked useful

Character-matched held-out bits-per-character was best for embed_relevance_dedup at 0.829261 mean, versus random 0.936005, exact_dedup 0.921507, embed_near_dedup 0.896871, and embed_relevance_only 0.846122. The result supports testing relevance plus near-dedup under matched sequence-item budgets, while the document-budget ablation shows relevance-only can look better when duplicate-heavy target text increases effective train characters.

## Boundaries and scale limits

Synthetic corpus only; hashed character n-gram embeddings instead of neural embeddings; character n-gram LM proxy instead of transformer pretraining; 3 seeds; no real tokenizer-level or downstream validation.

## Claim scope

On a deterministic synthetic corpus with target documents, off-target distractors, exact duplicates, and near duplicates, embedding relevance plus near-duplicate filtering improved character-matched held-out target-domain n-gram language-model loss versus random, exact-dedup, near-dedup-only, and relevance-only selectors.

## Why it stopped

Synthetic/proxy evidence is useful but insufficient for publication-grade validation; this is not a full validation of pretraining data selection.

## Recommended next action

Run a bounded real-corpus deepen test with matched sequence-item budgets, neural or production embeddings, a cosine-threshold sweep, and a tiny transformer validation-loss endpoint before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus matched-token embed-dedup data selection probe
- Success threshold: Relevance-plus-near-dedup achieves at least 3% lower mean token-level validation loss than both relevance-only and exact-dedup at matched sequence-item budget, with the effect present in at least 2 of 3 seeds.
- Stop condition: Stop as negative if relevance-plus-near-dedup fails to beat relevance-only or exact-dedup by 1% mean validation loss after 3 seeds, or if gains disappear across reasonable dedup thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-tiny-pretrain-embed-dedup-data-selection-737ec803ec1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
