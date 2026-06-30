# Perplexity-Diversity Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-diversity-data-selection-for-tiny-pretraining-8416872a6032`
Run ID: `perplexity-diversity-data-selection-for-tiny-pretraining-8416872a6032-20260528T030244400770+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58cdd723e86b

## What looked useful

Low unigram proxy-perplexity filtering was worse than random on mean final validation loss (+0.0480 loss, 1/5 wins). Adding lexical diversity increased mean pairwise cosine distance to 0.8465 and improved over low-proxy-perplexity-only on mean loss (-0.0296, 3/5 wins), but remained worse than random on mean loss (+0.0184, 2/5 wins).

## Boundaries and scale limits

Tiny local run only: 900 candidate documents, 180 selected documents, 120k training tokens per strategy per seed, 700 optimizer steps, Wikitext-2 only, unigram proxy perplexity, lexical diversity only. Not evidence against neural-perplexity or semantic-diversity selectors at larger scale.

## Claim scope

On Wikitext-2 tiny causal-LM pretraining with a unigram proxy-perplexity scorer and lexical TF-IDF diversity, the joint low-proxy-perplexity plus diversity selector increased measured diversity and partly improved over low-proxy-perplexity-only selection, but did not robustly improve validation loss over random selection across five seeds.

## Why it stopped

Bounded direct tiny-pretraining evidence did not support the hypothesis versus random selection; this is an early falsification of the simple unigram-perplexity plus lexical-diversity implementation, not a full validation or broad rejection of all perplexity-diversity selection.

## Recommended next action

Stop this simple-proxy variant as no-paper evidence; the next bounded test should replace the unigram proxy with a pretrained neural proxy and replace lexical TF-IDF diversity with semantic embedding diversity under the same fixed-token evaluation harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Perplexity and Semantic Diversity for Tiny Pretraining Selection
- Success threshold: Mean final validation loss at least 0.05 lower than random and proxy-perplexity-only controls, with lower loss in at least 4 of 5 paired seeds versus random.
- Stop condition: Stop as negative if the joint neural/semantic selector fails to beat random on mean final validation loss or wins fewer than 4 of 5 paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-diversity-data-selection-for-tiny-pretraining-8416872a6032`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
