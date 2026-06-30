# Per-Head 4-Bit KV Eviction for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-eviction-for-long-context-on-cpu-ebd56ca5444c`
Run ID: `per-head-4-bit-kv-eviction-for-long-context-on-cpu-ebd56ca5444c-20260521T224904395740+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba50c91d1226

## What looked useful

Per-head scoring should not be claimed against tail/LRU alone: the experiment found 27-39% lower mean relative output error versus global tail eviction, but only 1.5-1.8% lower error versus global scored head-token eviction at the same 4-bit budget.

## Boundaries and scale limits

Tested only synthetic traces at 1024 tokens, 12 heads, 64-dimensional K/V, two retained-token budgets, and three random seeds. No trained LLM perplexity, real KV traces, long-context task accuracy, or optimized CPU 4-bit kernel was tested.

## Claim scope

On synthetic heterogeneous CPU attention traces, per-head scored 4-bit KV eviction reduces attention-output error substantially versus a simple global recent-window cache, but only marginally versus a stronger global scored head-token eviction baseline.

## Why it stopped

No-paper closure: bounded synthetic evidence is useful but mixed, and the apparent gain mostly disappears against a stronger scored baseline.

## Recommended next action

Run a bounded real-model trace/perplexity experiment comparing per-head scored 4-bit KV eviction against global scored head-token eviction at equal byte budgets before considering this idea paper-worthy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model per-head 4-bit KV eviction against scored head-token baseline
- Success threshold: Per-head scored 4-bit eviction achieves at least 10% lower perplexity delta, logit KL, or attention-output error than global scored head-token eviction at the same byte budget on real-model traces.
- Stop condition: Stop if per-head scored eviction is within 5% of global scored eviction or worse across real-model budgets, since the synthetic result would not translate into a distinct practical mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-eviction-for-long-context-on-cpu-ebd56ca5444c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
