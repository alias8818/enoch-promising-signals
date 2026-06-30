# Medium-scale low-perplexity filtering confirmation for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-scale-low-perplexity-filtering-confirmation-for-tin-b7ddca2259`
Run ID: `medium-scale-low-perplexity-filtering-confirmation-for-tin-b7ddca2259-20260522T204651428591+0000`

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

- Parent run decision: Perplexity-based data filtering for tiny local pretraining: enoch://control-plane/projects/perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744/runs/perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744-20260522T203135046009+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72a1352c3750

## What looked useful

Low-perplexity filtering appears useful primarily as noise/off-distribution removal in this controlled tiny-pretraining setting. The clean-only low-vs-random advantage was tiny and changed sign in one seed, so the stronger clean-corpus filtering claim remains unsupported.

## Boundaries and scale limits

Three seeds, 450k selected characters per condition, 450 training steps, character-level 4-layer tiny Transformer, trigram perplexity scorer, WikiText-2, and synthetic corruption for the mixed pool. This is not GPT-2-small-class, neural-scorer, natural-web-noise, or long-run evidence.

## Claim scope

In a Tier-1 controlled WikiText-2 tiny-pretraining test, low-perplexity filtering improved held-out clean validation loss versus random/high controls when the candidate pool included corrupted text, and consistently beat the high-perplexity clean tail. It did not robustly beat random selection among already-clean examples.

## Why it stopped

The Tier-1 direct tiny-pretraining test confirmed a noise-removal mechanism but did not produce publication-grade or broadly robust evidence for low-perplexity filtering on clean pretraining corpora.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded deepen test on naturally noisy web text with a neural perplexity scorer and tokenizer-level GPT-style tiny model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-noise neural-scorer low-perplexity filtering test for tiny GPT pretraining
- Success threshold: Across at least three seeds, low-perplexity selection beats random selection by mean held-out validation loss >= 0.02 nats on naturally noisy data and does not degrade clean held-out validation relative to random by more than 0.005 nats.
- Stop condition: Stop if low-perplexity selection fails to beat random by 0.02 nats, degrades clean held-out validation by more than 0.005 nats, or only beats high-perplexity tails while matching random.

## Evidence references

- Artifact root: `<local-path>/projects/medium-scale-low-perplexity-filtering-confirmation-for-tin-b7ddca2259`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
