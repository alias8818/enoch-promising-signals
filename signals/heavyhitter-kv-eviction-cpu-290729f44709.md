# HeavyHitter_KV_Eviction_CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heavyhitter-kv-eviction-cpu-290729f44709`
Run ID: `heavyhitter-kv-eviction-cpu-290729f44709-20260603T153459394206+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7dfe5b51a415

## What looked useful

Cache-observed heavy-hitter KV retention substantially reduced output RMSE versus sliding/random only when persistent heavy attention was strong; at moderate heavy strength it retained more full-attention mass and top-1 keys but produced worse output RMSE than sliding, showing attention-mass retention alone is not a reliable objective.

## Boundaries and scale limits

No real LLM, no learned multi-layer transformer, no perplexity/task-quality measurement, no optimized serving runtime, and no datacenter-scale validation. The result supports only a mechanism-level proxy claim.

## Claim scope

CPU-only synthetic autoregressive attention simulation at sequence length 2048, dimension 64, five seeds, KV budgets of 5%, 10%, and 20%, comparing sliding, random, cache-observed heavy hitter, and oracle heavy hitter eviction.

## Why it stopped

Synthetic proxy evidence is mixed: the mechanism works in strong-heavy traces but fails the broader standalone hypothesis under moderate heavy-hitter structure, so this run closes as no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded real-model trace validation on a small transformer with perplexity/next-token loss and an adaptive recent-floor heavy-hitter policy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace validation of adaptive heavy-hitter KV eviction
- Success threshold: At 10% and 20% KV budgets, adaptive heavy-hitter eviction reduces next-token loss or perplexity degradation versus sliding by at least 10% relative on concentrated-attention heads/layers without increasing CPU decode overhead by more than 10%.
- Stop condition: Stop if adaptive heavy-hitter eviction fails to beat sliding on next-token loss at both 10% and 20% KV budgets or if attention concentration does not predict policy benefit.

## Evidence references

- Artifact root: `<local-path>/projects/heavyhitter-kv-eviction-cpu-290729f44709`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
