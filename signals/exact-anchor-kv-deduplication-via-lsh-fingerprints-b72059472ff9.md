# Exact-Anchor KV Deduplication via LSH Fingerprints

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-deduplication-via-lsh-fingerprints-b72059472ff9`
Run ID: `exact-anchor-kv-deduplication-via-lsh-fingerprints-b72059472ff9-20260609T011623557554+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3202d22de330

## What looked useful

Repeated token anchors produced exact duplicate KV blocks only in the content-only control. With learned absolute positions and RoPE-style positioned keys, 647 repeated token blocks produced zero exact full-KV duplicate blocks; LSH generated candidates but all failed exact verification in the positional cases.

## Boundaries and scale limits

No real pretrained model KV traces, no multi-layer serving system, no fused cache implementation, and no long-context production benchmark. The result tests a necessary exact-equality condition rather than full deployment performance.

## Claim scope

Bounded local algebraic probe of exact full-KV block deduplication using planted repeated token anchors, LSH candidate generation, and exact verification under content-only, learned-absolute, and RoPE-style KV constructions.

## Why it stopped

Proxy plus medium local confirmation, not full validation, showed early falsification of exact full-KV reuse for positional transformer caches.

## Recommended next action

Stop this exact full-KV dedup line as a no-paper useful signal; run a bounded deepen follow-up on V-only deduplication or position-factorized pre-RoPE key storage using real small-model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: V-only and position-factorized KV dedup on real small-model traces
- Success threshold: At least 10% exact cache-memory reduction on repeated-span prompts with bitwise or tolerance-justified exact attention-logit reconstruction and less than 5% candidate-verification overhead in a small-model trace benchmark.
- Stop condition: Stop if real small-model traces show under 2% V/pre-RoPE duplicate savings or if exact reconstruction changes attention logits beyond the chosen numerical tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-deduplication-via-lsh-fingerprints-b72059472ff9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
