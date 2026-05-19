# Token-Entropy Routed Speculative Decoding

Status: `useful_signal`
Project ID: `token-entropy-routed-speculative-decoding-a47708aa33a1`
Run ID: `token-entropy-routed-speculative-decoding-a47708aa33a1-20260518T155625465288+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba2a2599325c

## What looked useful

Speculative decoding reduced target calls versus no-spec decoding, but entropy_routed_2_4_8 used 560 target calls versus 547 for fixed_4 and 452 for fixed_8. The inverted entropy ablation was also worse at 580 target calls.

## Boundaries and scale limits

Small model pair only; no KV-cache optimized serving implementation; one dataset; 1536 generated tokens per strategy; wall-clock timings are implementation-local and should not be read as production throughput.

## Claim scope

In a bounded direct speculative-decoding simulation using gpt2 as target, distilgpt2 as draft, Wikitext-2 prompts, 24 prompts, and 1536 generated tokens per strategy, simple draft-entropy routing of block length did not outperform fixed-k controls.

## Why it stopped

Bounded direct small-model test falsified the simple entropy-routed block-length policy as an improvement over fixed-k controls; this is not a full production-scale validation.

## Recommended next action

Stop this entropy-only routing line as no-paper evidence; any next run should replace entropy-only routing with a cost-aware or learned acceptance predictor and compare against fixed-k controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/token-entropy-routed-speculative-decoding-a47708aa33a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
