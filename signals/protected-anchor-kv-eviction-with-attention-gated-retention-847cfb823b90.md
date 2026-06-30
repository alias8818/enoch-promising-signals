# Protected-Anchor KV Eviction with Attention-Gated Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `protected-anchor-kv-eviction-with-attention-gated-retention-847cfb823b90`
Run ID: `protected-anchor-kv-eviction-with-attention-gated-retention-847cfb823b90-20260529T180242450152+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ece0442c89b7

## What looked useful

Protected-anchor plus attention-gated retention eliminated anchor misses and won total miss rate in 13/16 synthetic conditions, especially at cache capacity 64 or larger. It failed at capacity 32 when sparse anchor reuse made a fixed 16-anchor reserve consume too much cache.

## Boundaries and scale limits

No real transformer, perplexity, serving throughput, real attention traces, learned anchor detection, or downstream task accuracy was tested. Evidence is bounded to a short CPU simulator grid.

## Claim scope

Synthetic fixed-capacity KV-cache eviction simulator with known prompt-prefix anchors, local references, sparse anchor reuse, and occasional non-anchor long-range references.

## Why it stopped

No-paper useful signal: the result is synthetic/proxy evidence with a clear mechanism and failure mode, not direct publication-grade model evidence.

## Recommended next action

Run a bounded GPT-2-small-class direct test with real attention traces and equal KV budgets, using a capacity-aware anchor reserve versus sliding, attention-EMA, and at least one established KV eviction baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small Direct Test for Capacity-Aware Protected Anchor KV Eviction
- Success threshold: At two or more KV budgets, capacity-aware protected anchors reduce anchor/needle failures by at least 25% relative to the best non-protected baseline while keeping perplexity or local-token miss regression under 2%.
- Stop condition: Stop if real-model metrics show less than 10% anchor/needle improvement or more than 2% perplexity/locality regression at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/protected-anchor-kv-eviction-with-attention-gated-retention-847cfb823b90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
