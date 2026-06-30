# Gradient-Matched Tiny Data Selection for Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64`
Run ID: `gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64-20260528T070613325937+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

Gradient-top selection chose 100% target-domain examples across three bounded seeds, achieved target loss 1.088 +/- 0.018 versus random 1.901 +/- 0.054, nearly matched oracle target selection at 1.057 +/- 0.022, and anti-aligned selection degraded target loss to 6.440 +/- 0.196.

## Boundaries and scale limits

Synthetic separable domains only; tiny 1-2 layer Transformer models; three bounded seeds; selection measured at initialization; no natural text, GPT-2-small-class model, long pretraining, or downstream task validation.

## Claim scope

In a bounded synthetic next-token language-modeling probe with four separable Markov domains, selecting tiny pretraining subsets by per-example gradient cosine to a small target reference gradient recovered target-domain examples and improved held-out target loss versus random selection.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct full validation of local pretraining; domains were highly separable with target-vs-distractor gradient score AUC 1.0.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should test natural-text and near-target-domain robustness before any scale-only validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text robustness for gradient-matched tiny data selection
- Success threshold: Gradient matching reduces target held-out LM loss by at least 5% versus random and beats high-loss plus embedding-similarity baselines in at least two of three seeds without collapsing mixed-domain loss by more than 20% relative to random.
- Stop condition: Stop if gradient matching fails to beat random target loss in two seeds, if it only works by selecting trivially labeled domains, or if runtime exceeds the local bounded budget without checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-matched-tiny-data-selection-for-local-pretraining-e961c3e82c64`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
