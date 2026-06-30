# Info-density scoring for tiny pretraining data selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `info-density-scoring-for-tiny-pretraining-data-selection-50a79b249526`
Run ID: `info-density-scoring-for-tiny-pretraining-data-selection-50a79b249526-20260525T000240946560+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fd8e49665696

## What looked useful

Naive density selected 76.1% random noise and 0% target facts, yielding 8.7265 mean validation loss and 0% fact-probe accuracy, versus random selection at 1.6014 loss and a diverse target oracle at 0.8993 loss. High local entropy/density is therefore unsafe without a relevance or quality gate.

## Boundaries and scale limits

Evidence is from a synthetic corpus, a tiny GRU language model, 700 candidate documents, 3 repeats per strategy, and short CPU-only training. It does not validate or falsify quality-gated density scoring on real corpora or GPT-2-class transformer pretraining.

## Claim scope

In a controlled synthetic tiny-pretraining selection task with target facts, boilerplate, off-target facts, and random-token noise, a naive unsupervised information-density score based on local entropy, type-token ratio, zlib compression density, and mild rarity failed as a standalone selector under a fixed 2200-token budget.

## Why it stopped

Proxy early falsification: the tested naive density score selected mostly random noise and underperformed random by 7.13 validation-loss points, while an oracle confirmed the target task was learnable under the same budget.

## Recommended next action

Stop this run as a proxy early falsification of naive standalone information-density selection; the concrete next bounded test is a quality-gated density selector on a real small corpus with noise controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-gated information density on real tiny pretraining data
- Success threshold: Quality-gated density must beat random and quality-only controls by at least 5% relative held-out perplexity with lower or equal noise fraction across at least 3 seeds.
- Stop condition: Stop if quality-gated density still selects more high-entropy noise than random or fails to beat the quality-only control on held-out loss.

## Evidence references

- Artifact root: `<local-path>/projects/info-density-scoring-for-tiny-pretraining-data-selection-50a79b249526`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
