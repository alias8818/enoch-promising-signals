# Perplexity-Filtered Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-filtered-tiny-pretraining-a55f5650e198`
Run ID: `perplexity-filtered-tiny-pretraining-a55f5650e198-20260525T181141318549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dc65dc46b70

## What looked useful

Perplexity scores carried a weak data-quality signal: low-PPL filtering improved confirmation validation byte NLL by -0.00459 versus random on average, while high-PPL filtering worsened it by +0.00948. The 450-step run did not show a low-PPL advantage, so the effect is useful but not decisive.

## Boundaries and scale limits

Small single-corpus GPU probe only: byte-level tiny model, 1200 scored chunks, 260k-byte selected corpora, 5 paired seeds in confirmation, and no GPT/BPE-tokenized GPT-2-small-class baseline or downstream evaluation.

## Claim scope

On WikiText-2 chunks scored by distilgpt2, a 0.52M-parameter byte-level causal Transformer trained on matched byte budgets showed a small 1800-step validation benefit from low-perplexity filtering versus random selection, while high-perplexity filtering was worse.

## Why it stopped

The local direct evidence is mixed and too small for a paper: confirmation shows a small low-PPL benefit, but the earlier 450-step run did not and the paired 5-seed effect is not statistically decisive.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded deeper follow-up with a GPT/BPE-tokenized target model, at least 10 paired seeds, simple heuristic-filter controls, and longer matched-token training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Perplexity Filtering Check with Tokenized Tiny GPT
- Success threshold: Low-PPL filtering beats random and heuristic controls by at least 1% relative validation perplexity with paired confidence intervals excluding zero, while high-PPL remains worse than random.
- Stop condition: Stop if low-PPL fails to beat random by 0.5% relative validation perplexity after the planned paired medium run or if heuristic filters explain the full gain.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-tiny-pretraining-a55f5650e198`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
