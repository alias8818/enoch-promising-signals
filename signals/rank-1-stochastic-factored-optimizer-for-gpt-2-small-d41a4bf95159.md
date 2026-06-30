# Rank-1 stochastic factored optimizer for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rank-1-stochastic-factored-optimizer-for-gpt-2-small-d41a4bf95159`
Run ID: `rank-1-stochastic-factored-optimizer-for-gpt-2-small-d41a4bf95159-20260605T014214603778+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/210199ea0250

## What looked useful

Factored optimizer state reduced GPT-2-small-shaped state from 995.5 MB for AdamW to 1.29 MB. Dense factored RMS nearly matched AdamW on MiniGPT after 200 steps (val loss 2.4645 vs 2.3954), while rank1sf lagged badly (4.3840 at lr 3e-4, 3.7378 at lr 1e-3, 4.3983 with k=4).

## Boundaries and scale limits

No full GPT-2-small pretraining, no long-horizon web-text run, no full tokenizer/corpus validation, and only a small learning-rate/rank-sample sensitivity check. The training-quality result is an early mechanism/proxy test.

## Claim scope

Local evidence on GPT-2-small-shaped optimizer state and a 4-layer MiniGPT byte-level causal-LM run: rank-1 stochastic factored updates greatly reduce optimizer state but substantially underperform AdamW and a dense factored RMS control on short-horizon validation loss.

## Why it stopped

Proxy early falsification: the rank-1 stochastic update preserved memory savings but lost too much optimization signal versus both AdamW and the dense factored control in the bounded causal-LM test.

## Recommended next action

Stop this rank-1 stochastic proposal as a no-paper useful signal; run a separate bounded follow-up on dense factored RMS for GPT-2-small-class fine-tuning or longer MiniGPT training.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Dense factored RMS optimizer for GPT-2-small-class language modeling
- Success threshold: Dense factored RMS final validation loss within 5% relative of AdamW at the same token budget while using at least 100x less optimizer state.
- Stop condition: Stop if dense factored RMS is more than 10% worse than AdamW validation loss after the calibrated token budget or requires hyperparameters that erase the memory/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-stochastic-factored-optimizer-for-gpt-2-small-d41a4bf95159`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
