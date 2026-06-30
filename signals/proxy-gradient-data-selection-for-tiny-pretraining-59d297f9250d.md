# Proxy-Gradient Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `proxy-gradient-data-selection-for-tiny-pretraining-59d297f9250d`
Run ID: `proxy-gradient-data-selection-for-tiny-pretraining-59d297f9250d-20260524T203645855286+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94333ccb4b8d

## What looked useful

Proxy-gradient selection achieved 1.000 mean target-compatible selection precision versus 0.235 for random and reduced mean target validation loss from 1.028 to 0.709, close to the oracle-target upper bound of 0.697. The loss-high control selected distractors and reached 5.100 loss.

## Boundaries and scale limits

Synthetic modular-sequence data only; tiny GRU proxy and target models only; 1600-example candidate pools; exact per-example gradients; no real text corpus, transformer baseline, long training, or production scoring-cost analysis.

## Claim scope

In a controlled synthetic mixed-domain next-token pretraining task, exact proxy-model validation-gradient alignment selected target-compatible examples and improved a separately initialized tiny GRU LM's target validation loss versus random and loss-high controls across three seeds.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-scale rather than direct real-corpus transformer pretraining validation.

## Recommended next action

Run one bounded real-corpus tiny-transformer confirmation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Tiny-Transformer Proxy-Gradient Data Selection
- Success threshold: Proxy-gradient must improve mean target validation loss by at least 5% relative to random and beat both loss-high and embedding-similarity controls across at least three seeds, while keeping scoring cost within 2x the strongest non-gradient selector.
- Stop condition: Stop if proxy-gradient does not beat random target validation loss on at least two of three seeds or if scoring cost is more than 2x the strongest non-gradient selector without a validation-loss gain.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-gradient-data-selection-for-tiny-pretraining-59d297f9250d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
