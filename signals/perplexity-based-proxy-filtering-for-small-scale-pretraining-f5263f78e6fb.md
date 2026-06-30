# Perplexity-Based Proxy Filtering for Small Scale Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-based-proxy-filtering-for-small-scale-pretraining-f5263f78e6fb`
Run ID: `perplexity-based-proxy-filtering-for-small-scale-pretraining-f5263f78e6fb-20260528T064453898360+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

Low-PPL-only filtering was seed-sensitive: low minus random validation loss deltas were +0.0014, -0.0470, and +0.0361 nats, mean -0.0032. High-PPL selection was consistently worse than random across all three seeds, mean +0.0279 nats, suggesting proxy perplexity may be more useful for excluding high-perplexity tails than for greedily taking the lowest-PPL documents.

## Boundaries and scale limits

This run used WikiText-2 only, 45k selected tokens per condition, 160 optimizer steps, one proxy model, and no downstream task evaluation. It is not evidence about web-scale filtering, GPT-2-small-class training, larger proxy scorers, or long-run data-quality effects.

## Claim scope

On a bounded WikiText-2 small-pretraining test with 700 candidate documents, 45k selected tokens, a 4-layer GPT-2-style target model, and three seeds, selecting the lowest distilgpt2-perplexity documents did not reliably improve held-out validation loss versus random selection. Selecting the highest-perplexity tail was consistently worse than random.

## Why it stopped

Direct small-scale evidence did not meet the success threshold for reliable low-PPL filtering improvement over random; this is a bounded early falsification of the strong low-PPL-only claim, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should evaluate tail-trimming, not low-PPL-only selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tail-Trimmed Proxy Perplexity Filtering for Small Pretraining
- Success threshold: Tail-trimmed random beats random by at least 0.03 nats mean validation loss with the same sign in at least 4 of 5 seeds and is better than low-PPL-only selection.
- Stop condition: Stop if tail trimming fails to beat random by 0.01 nats mean validation loss or if the sign is inconsistent across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-proxy-filtering-for-small-scale-pretraining-f5263f78e6fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
