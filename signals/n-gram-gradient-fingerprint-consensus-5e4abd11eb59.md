# N-Gram Gradient Fingerprint Consensus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-gradient-fingerprint-consensus-5e4abd11eb59`
Run ID: `n-gram-gradient-fingerprint-consensus-5e4abd11eb59-20260525T214501069897+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e860e91d93dc

## What looked useful

Top-1 recovery at 512 filler examples improved from 0.36 with one observation to 0.96 with four and 1.00 with eight. At 2048 filler examples, top-1 improved from 0.08 with one observation to 0.76 with sixteen. Random top-1 baseline was 0.001 across 1000 candidates, and absent-target controls did not select a fixed candidate.

## Boundaries and scale limits

Small neural n-gram model only; synthetic token transitions; known finite candidate set; raw unclipped gradients; no natural-language corpus, transformer model, federated optimizer state, differential privacy, clipping, secure aggregation, or open-vocabulary candidate generation tested.

## Claim scope

In a synthetic 80-token neural n-gram language-model probe with a 1000-item candidate set containing the true 4-gram, full-gradient cosine fingerprints can recover present target n-grams from noisy aggregate gradients, and consensus across independent observations improves recovery under high filler-gradient noise.

## Why it stopped

Synthetic candidate-set evidence supports the mechanism but is not direct/full validation of a practical privacy attack or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same candidate-ranking attack on a small transformer or GPT-2-small-class model using natural text and realistic batch construction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text transformer check for n-gram gradient fingerprint consensus
- Success threshold: At 512 or more filler examples per observed aggregate gradient, consensus of at most 16 observations improves top-1 recovery by at least 2x over a single observation and reaches at least 0.25 top-1 while absent-target controls remain diffuse.
- Stop condition: Stop as negative if transformer natural-text recovery remains within 2x random top-1/top-5 baselines or absent-target controls produce similarly concentrated candidate selections.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-gradient-fingerprint-consensus-5e4abd11eb59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
