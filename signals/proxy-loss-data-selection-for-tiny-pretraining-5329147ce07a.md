# Proxy-Loss Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-loss-data-selection-for-tiny-pretraining-5329147ce07a`
Run ID: `proxy-loss-data-selection-for-tiny-pretraining-5329147ce07a-20260529T235303360140+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3f2524755b31

## What looked useful

Lowest-proxy-loss data selection appears harmful under a small token budget in this setup (+0.089 mean validation loss vs random, 0/3 wins). Proxy loss still carries weak selection signal because highest-loss examples were marginally better than random on average (-0.0044 validation loss, 2/3 wins), suggesting hard-example selection is the only plausible follow-up direction.

## Boundaries and scale limits

Three seeds, WikiText-2 only, byte-level tokenizer, tiny Transformer models, short training schedules, 2048 candidate sequences, 384 selected sequences, and validation-only language-model loss. No GPT-2-small-class, tokenizer-based, C4/FineWeb/TinyStories, downstream, or long-run validation was performed.

## Claim scope

On a local byte-level WikiText-2 tiny causal-LM subset-selection test, selecting lowest proxy-loss examples consistently underperformed random selection; selecting highest proxy-loss examples showed only a very small, non-paper-ready edge.

## Why it stopped

Proxy/local early falsification of the naive low-proxy-loss selection policy, not a full validation of proxy-loss data selection at pretraining scale.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded tokenizer-based TinyStories or small C4 shard test of high-proxy-loss selection versus random and diversity baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-Example Proxy-Loss Selection on Tokenizer-Based TinyStories
- Success threshold: High-proxy-loss selection beats random by at least 0.02 validation loss or 1 percent perplexity with non-overlapping 95 percent confidence intervals across budgets, and low-proxy-loss does not beat random.
- Stop condition: Stop if high-proxy-loss selection fails to beat random on both budgets or if the gain is below 0.01 validation loss with overlapping confidence intervals.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-loss-data-selection-for-tiny-pretraining-5329147ce07a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
