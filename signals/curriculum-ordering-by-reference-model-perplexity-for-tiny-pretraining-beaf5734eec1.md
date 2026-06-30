# Curriculum ordering by reference-model perplexity for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-ordering-by-reference-model-perplexity-for-tiny-pretraining-beaf5734eec1`
Run ID: `curriculum-ordering-by-reference-model-perplexity-for-tiny-pretraining-beaf5734eec1-20260621T130852482956+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/612f04cc27a5

## What looked useful

Reference-model perplexity appears useful for constructing non-monotonic tiny-pretraining curricula, but the simple low-perplexity-to-high-perplexity curriculum was worse than random in this probe. Middle_out achieved mean final validation loss 7.1090 versus random 7.1248; easy_to_hard was 7.1369.

## Boundaries and scale limits

Single dataset, one reference model, 180 validation documents, 240 optimizer steps per seed, three seeds, no downstream transfer, no larger-corpus or longer-training validation.

## Claim scope

On a bounded WikiText-2 proxy with 720 train documents, distilgpt2 reference scoring, and 9.3M-parameter GPT-style tiny models trained for 491,520 tokens across three seeds, monotonic easy-to-hard reference-perplexity ordering did not improve validation loss over random, while a median-difficulty-first middle_out ordering produced the best mean final validation loss.

## Why it stopped

No-paper closure: the direct small-scale evidence is useful but mixed, and the original monotonic easy-to-hard curriculum is not supported; the positive middle_out signal is too small and narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen test with more documents, at least five seeds, longer training, and matched random replicates to determine whether median-difficulty-first ordering has a persistent effect beyond this small proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Median-difficulty-first reference-perplexity curriculum for tiny LM pretraining
- Success threshold: middle_out mean final validation loss at least 0.02 lower than matched random with the advantage present in at least 4 of 5 seeds, without worse early instability.
- Stop condition: Stop if middle_out fails to beat matched random by at least 0.01 mean validation loss or wins in fewer than 3 of 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-by-reference-model-perplexity-for-tiny-pretraining-beaf5734eec1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
