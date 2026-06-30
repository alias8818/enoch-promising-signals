# Dynamic KV-cache eviction with attention-score thresholding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-kv-cache-eviction-with-attention-score-thresholding-45a6634402d2`
Run ID: `dynamic-kv-cache-eviction-with-attention-score-thresholding-45a6634402d2-20260605T163808782542+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/7be7d2f361d0

## What looked useful

At similar small cache sizes, threshold eviction was competitive on local attention, but in delayed retrieval thresholds 0.03 and 0.01 evicted 100% of future-critical targets and achieved 0% retrieval top-1 match. A moderate threshold, 0.003, improved retrieval MSE versus sliding-window 128 in this toy setup but retained about 117 tokens on average and still evicted 45.83% of retrieval targets.

## Boundaries and scale limits

No pretrained LLM, no multi-layer decoding, no real tokenizer/data distribution, no GPU serving throughput, and no production memory-pressure measurement were tested.

## Claim scope

Controlled single-layer causal-attention simulations show attention-score threshold KV eviction can match or slightly improve sliding-window cache/error tradeoffs in local and diffuse toy regimes, but aggressive thresholds are brittle in delayed retrieval.

## Why it stopped

Proxy-only useful signal with early falsification of aggressive thresholds in delayed retrieval; not a full validation and not paper-ready.

## Recommended next action

Run a bounded pretrained GPT-2-small-class decoding benchmark that compares threshold eviction, sliding-window, and a retrieval-protected hybrid at matched KV budgets; stop here for paper purposes because this run is proxy-only and mixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained decoding benchmark for retrieval-protected attention-threshold KV eviction
- Success threshold: At two matched KV budgets, the hybrid policy must reduce retrieval-target eviction by at least 25% versus naive thresholding while keeping perplexity degradation no worse than sliding-window and adding less than 10% decode overhead in the bounded benchmark.
- Stop condition: Stop if naive and hybrid thresholding both lose to sliding-window on perplexity or delayed-retrieval accuracy at matched budgets, or if threshold bookkeeping overhead exceeds the memory benefit in the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-cache-eviction-with-attention-score-thresholding-45a6634402d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
