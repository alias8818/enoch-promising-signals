# Tiny Pretraining with Bounded Data Selection: Quality Filtering Effects at Scale

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-pretraining-with-bounded-data-selection-quality-filtering-effects-at-scale-4552400e8255`
Run ID: `tiny-pretraining-with-bounded-data-selection-quality-filtering-effects-at-scale-4552400e8255-20260614T071052073101+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

Observed-quality top selection reduced clean NLL vs random by 0.050, 0.106, and 0.105 at 500, 2000, and 8000 candidate documents; quality-plus-diversity reduced rare-topic NLL by 0.055, 0.169, and 0.203; low-quality selection worsened clean NLL by 0.054, 0.291, and 0.343. Effects were directionally consistent in 5/5 seeds at each pool size.

## Boundaries and scale limits

Synthetic data and interpolated n-gram language model only; no transformer training, no real web corpus, no tokenizer effects, no optimizer dynamics, and no datacenter-scale validation. Candidate pools were at most 8000 synthetic documents with a 30000-token selected budget.

## Claim scope

In a deterministic synthetic corpus with document-level quality variation, fixed-token-budget selection of higher-quality documents improved held-out high-quality n-gram LM loss versus random selection across 5 seeds and candidate pools of 500, 2000, and 8000 documents. A quality-plus-diversity selector gave the best rare-topic held-out loss.

## Why it stopped

Closed as no-paper useful signal: the local result supports the quality-filtering mechanism in a synthetic n-gram proxy, but it is not publication-grade evidence for tiny transformer pretraining or real data-selection effects at scale.

## Recommended next action

Run a bounded direct-evidence follow-up with a tiny transformer on a real or semi-real corpus under the same selected-token budget, preserving random, observed-quality, low-quality, and quality-diversity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny transformer fixed-budget quality filtering on real corpus slices
- Success threshold: Observed-quality selection improves clean validation loss over random in at least 3/3 seeds by >=2% perplexity, and quality-diversity improves rare-domain perplexity by >=5% without degrading clean perplexity by more than 2% relative to observed-quality selection.
- Stop condition: Stop if smoke training exceeds the CPU-worker budget without GPU access, if selected-token accounting cannot be made equal across strategies, or if quality-based selection fails to beat random in 2 of the first 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-with-bounded-data-selection-quality-filtering-effects-at-scale-4552400e8255`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
