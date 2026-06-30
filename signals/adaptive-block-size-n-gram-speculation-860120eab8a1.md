# Adaptive block-size n-gram speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `adaptive-block-size-n-gram-speculation-860120eab8a1`
Run ID: `adaptive-block-size-n-gram-speculation-860120eab8a1-20260524T043733109500+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9b19fa4a73f3

## What looked useful

On 120k held-out bytes, fixed_16 maximized raw verifier-call savings at 2.044 target tokens per verifier call but wasted 7.317 draft tokens per target. Fixed_2 was best when draft tokens cost 0.2 verifier calls, with 1.064 target tokens per unit cost. The best adaptive variant reached 1.031 on that metric, and validation-calibrated adaptive policies transferred poorly.

## Boundaries and scale limits

Does not measure transformer target latency, tokenizer-level behavior, GPU/KV-cache batching, stochastic sampling quality, or large-corpus robustness. Full LLM serving evidence could overturn the proxy result only if target-forward latency dominates draft cost enough to change the cost optimum.

## Claim scope

Byte-level trace replay on Tiny Shakespeare with train-only n-gram drafting, fixed block baselines, naive adaptive confidence/recent policies, and validation-calibrated first-token-confidence policies. Adaptive block sizing did not beat the best fixed block under cost-aware speculative decoding metrics.

## Why it stopped

Proxy replay evidence did not support adaptive block-size n-gram speculation over tuned fixed block sizes under cost-aware metrics; this is not a full LLM validation.

## Recommended next action

Stop this project as a proxy early falsification; only revisit if implementing a model-level speculative decoder that can measure wall-clock target latency and tuned fixed-block controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-block-size-n-gram-speculation-860120eab8a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
