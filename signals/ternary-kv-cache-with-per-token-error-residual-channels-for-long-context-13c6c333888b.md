# Ternary KV Cache with Per-Token Error-Residual Channels for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-kv-cache-with-per-token-error-residual-channels-for-long-context-13c6c333888b`
Run ID: `ternary-kv-cache-with-per-token-error-residual-channels-for-long-context-13c6c333888b-20260609T102335331503+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58d8e0541c11

## What looked useful

Across five seeds, int4 at 4.125 bits per KV element reached 0.0715 mean relative attention-output MSE, while ternary plus 8 residual channels at the same 4.125 bits reached 0.2434; ternary plus 16 residual channels still reached only 0.1822 at 6.125 bits.

## Boundaries and scale limits

No real trained-model KV traces, end-to-end perplexity, task accuracy, or packed-kernel throughput were measured; evidence is synthetic and proxy-level.

## Claim scope

Cache-level synthetic attention tests up to 8192 tokens show that per-token ternary KV caches with exact residual channels improve over plain ternary but do not match a simple per-token int4 baseline when residual index/value overhead is counted.

## Why it stopped

Early proxy falsification: synthetic cache-level evidence does not support competitiveness with int4 under honest bit accounting, though real-model traces could still overturn the result.

## Recommended next action

Stop this project as a no-paper useful signal unless a follow-up can test real GPT-2-class KV-cache traces with equal-bit int4 controls and lower-overhead residual coding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model KV Trace Test for Ternary Residual Cache Coding
- Success threshold: At the same effective bits per KV element as int4, ternary residual coding must achieve no worse than 1.10x int4 relative attention-output MSE and no worse than 0.02 absolute perplexity or loss degradation versus int4 on the tested corpus.
- Stop condition: Stop if real-model traces reproduce a greater than 2x attention-output error gap versus int4 at equal bit budget or if metadata overhead prevents a matched-budget comparison.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-kv-cache-with-per-token-error-residual-channels-for-long-context-13c6c333888b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
