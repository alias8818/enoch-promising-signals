# Perplexity-based Data Selection for CPU Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-based-data-selection-for-cpu-tiny-pretraining-6912adf7a600`
Run ID: `perplexity-based-data-selection-for-cpu-tiny-pretraining-6912adf7a600-20260524T033951193217+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c6d5d87a4c4e

## What looked useful

Low-perplexity selection achieved mean held-out target NLL 0.6692 versus 0.8076 for random and 4.4478 for high-perplexity at equal character budget over 32 seeds; low beat random in 27/32 seeds with one-sided sign-test p about 5.65e-05.

## Boundaries and scale limits

Synthetic template text only; character n-gram LM proxy only; selector perfectly separated target and distractor domains; no real corpus, tokenizer, transformer, deduplication, or long training validation.

## Claim scope

In a controlled synthetic mixed-domain corpus, selecting equal-character training data by low perplexity under a target-trained character n-gram selector improved held-out target loss for a tiny character n-gram LM versus random and high-perplexity controls.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic n-gram proxy, not direct publication-grade tiny neural pretraining evidence.

## Recommended next action

Run a bounded real-corpus follow-up using equal-token low/random/high perplexity selection and a CPU-trainable tiny neural LM before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus equal-token perplexity selection for CPU tiny neural LM pretraining
- Success threshold: Low-perplexity selection beats random held-out target NLL in at least 4 of 5 seeds and improves mean NLL by at least 3 percent at equal token budget without collapse on a near-domain distractor split.
- Stop condition: Stop if low-perplexity selection fails to beat random in 3 or more seeds, if gains vanish under equal-token accounting, or if selection quality is explained only by trivial domain labels.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-data-selection-for-cpu-tiny-pretraining-6912adf7a600`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
