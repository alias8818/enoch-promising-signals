# Learned KV Eviction for Bounded Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-kv-eviction-for-bounded-home-inference-94b9bd93d112`
Run ID: `learned-kv-eviction-for-bounded-home-inference-94b9bd93d112-20260529T131153276340+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277f7d0bf68a

## What looked useful

Learned eviction beat LRU on predictable traces across 8/8 seeds at all tested capacities, with the largest gain at capacity 64 (+0.0297 weighted hit-rate and about 41% of the LRU-to-Belady gap). The same learned scorer lost to LRU on shifted traces across 0/8 seeds, showing distribution-shift fragility.

## Boundaries and scale limits

Proxy-only CPU simulation: no real transformer decode loop, no real prompts, no perplexity/task-quality measurement, no GPU serving latency or memory-bandwidth measurement, and no production drift handling.

## Claim scope

On synthetic attention-like KV access traces, a ridge-regression learned eviction scorer trained on stable reuse features improves weighted hit rate over FIFO/LRU when the feature/reuse relationship persists, especially at tight cache capacity, but loses to LRU under a reversed feature shift.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and mixed: it supports the mechanism under stable features but also demonstrates an early robustness failure under feature shift.

## Recommended next action

Run a bounded direct transformer decode experiment with drift-aware learned eviction versus LRU/sliding-window/sink-token baselines on long-context prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Long-Context Decode Test for Drift-Aware Learned KV Eviction
- Success threshold: At equal KV budget, learned eviction improves quality/perplexity or retained-attention metrics over LRU/sliding-window by at least 2% without more than 5% decode-latency overhead, and does not regress by more than 1% under the shifted condition.
- Stop condition: Stop if the integrated learned policy fails to beat LRU/sliding-window on quality or retained-attention metrics in the stable condition, or if drift handling cannot prevent shifted-condition regressions within the latency budget.

## Evidence references

- Artifact root: `<local-path>/projects/learned-kv-eviction-for-bounded-home-inference-94b9bd93d112`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
