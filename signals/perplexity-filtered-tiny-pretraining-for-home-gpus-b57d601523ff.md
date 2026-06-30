# Perplexity-Filtered Tiny Pretraining for Home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-filtered-tiny-pretraining-for-home-gpus-b57d601523ff`
Run ID: `perplexity-filtered-tiny-pretraining-for-home-gpus-b57d601523ff-20260528T184003246316+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/afdbd41a7a28

## What looked useful

Low-reference-perplexity filtering won 0/5 calibrated seeds. High-reference-perplexity filtering won 4/5 seeds with mean eval loss 8.2451 versus 8.2633 for low-reference-perplexity and 8.2666 for random, suggesting simple easy-text filtering is not useful here while hard-example filtering may be worth a bounded follow-up.

## Boundaries and scale limits

Not full pretraining, not GPT-2-small scale, not multi-corpus, and not a long home-GPU run; uses Wikitext-2, a 2-layer 128-hidden scratch GPT-2-style model, 512 candidate chunks, 160 selected chunks per condition, and 160 optimizer steps per seed.

## Claim scope

Bounded Wikitext-2 tiny-LM experiment: selecting the lowest-distilgpt2-perplexity 128-token chunks did not improve held-out validation loss versus random or high-reference-perplexity controls under a 20,480-token matched training budget across five seeds.

## Why it stopped

Proxy-scale but direct target-metric early falsification: the proposed low-reference-perplexity filter failed to beat controls in a matched-token tiny pretraining setup and is not paper-ready.

## Recommended next action

Stop this project as no-paper negative/useful-signal evidence; run one bounded deepen follow-up on high-reference-perplexity or middle-band filtering with at least 1M selected tokens before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-Example Perplexity Filtering for Tiny Home-GPU Pretraining
- Success threshold: High or middle reference-perplexity filtering beats random and low-perplexity filtering by at least 0.03 held-out loss in mean across seeds without worse instability or throughput.
- Stop condition: Stop if high/middle filtering does not beat random by at least 0.01 mean held-out loss after 1M selected tokens or if gains reverse on the second corpus/domain.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-tiny-pretraining-for-home-gpus-b57d601523ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
