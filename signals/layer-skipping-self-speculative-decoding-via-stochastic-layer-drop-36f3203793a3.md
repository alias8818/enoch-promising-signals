# Layer-Skipping Self-Speculative Decoding via Stochastic Layer Drop

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `layer-skipping-self-speculative-decoding-via-stochastic-layer-drop-36f3203793a3`
Run ID: `layer-skipping-self-speculative-decoding-via-stochastic-layer-drop-36f3203793a3-20260601T002210925416+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3e2a40b3a776

## What looked useful

Naive stochastic layer drop fails on acceptance/cost tradeoff: the best stochastic configuration accepted only 4.61% of draft tokens and estimated 0.606x greedy speed; the highest stochastic acceptance reached 41.6% but still estimated only 0.588x greedy speed. Best overall prefix control estimated 0.655x greedy speed. Correctness was preserved by verifier fallback.

## Boundaries and scale limits

Tested 8 prompts, 24 generated tokens per prompt, GPT-2 12-layer target, keep probabilities 0.25/0.5/0.75, gamma 2/4/6, and local no-cache GPU forward timings. This does not test trained skip robustness, learned policies, larger models, diverse benchmarks, KV-cache serving kernels, or production end-to-end latency.

## Claim scope

On GPT-2 small with untrained identity layer skipping, stochastic Bernoulli layer-drop drafts and prefix-layer controls preserve exact greedy decoding under full-model verification but do not produce a speedup in a bounded local timing proxy.

## Why it stopped

Bounded GPT-2 proxy/early falsification: every tested untrained layer-drop configuration preserved exact greedy outputs but estimated a slowdown rather than a speedup.

## Recommended next action

Stop this no-paper line for untrained stochastic layer-drop drafting; only revisit with a trained or calibrated skip policy and a cache-aware serving benchmark.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/layer-skipping-self-speculative-decoding-via-stochastic-layer-drop-36f3203793a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
