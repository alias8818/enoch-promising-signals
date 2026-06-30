# Long-Context INT2 Residual Sliding Window

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `long-context-int2-residual-sliding-window-6843e20ea632`
Run ID: `long-context-int2-residual-sliding-window-6843e20ea632-20260604T151142533083+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5996c637976a

## What looked useful

Across 228 synthetic measurements, residual INT2 reduced output relative MSE versus pure sliding eviction by large margins while preserving old-token access. At 8192 tokens in far-retrieval, W=256 residual INT2 achieved top1 match 0.995 and rel MSE 0.1666, while W=256 sliding eviction had top1 match 0.000 and rel MSE 1.083. In recency, W=256 residual INT2 reached rel MSE 0.00368 at estimated 4.70x compression.

## Boundaries and scale limits

No real transformer perplexity, generation, retrieval benchmark, training adaptation, or packed INT2 GPU kernel was tested. Memory compression is estimated analytically from packed INT2 plus metadata rather than measured in a production cache implementation.

## Claim scope

Synthetic single-layer attention proxy shows that INT2-compressed old KV entries plus a recent high-precision residual window preserves attention outputs far better than pure sliding-window eviction when attention can target old tokens, with estimated KV-cache compression of about 3.3x to 5.2x for tested residual windows at 8192 tokens.

## Why it stopped

Closed as a no-paper useful signal because the evidence is a synthetic attention proxy, not direct model-quality or kernel-throughput validation.

## Recommended next action

Run a bounded frozen-transformer KV-cache ablation on a small long-context retrieval/perplexity task using the same residual INT2, full INT2, and sliding-eviction policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen Transformer KV-Cache Residual INT2 Ablation
- Success threshold: At 2048 to 8192 context length, residual INT2 should reduce retrieval/perplexity degradation by at least 30% versus sliding eviction at a comparable memory budget, while remaining within 10% relative quality loss versus full-precision KV on the selected task.
- Stop condition: Stop if residual INT2 fails to beat sliding eviction on direct model metrics at comparable memory in two independent seeds/tasks, or if implementation overhead makes the cache policy slower or larger than the full-precision baseline for the tested scale.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-int2-residual-sliding-window-6843e20ea632`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
