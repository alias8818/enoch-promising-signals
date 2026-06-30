# Paged-attention prefix KV aliasing under mixed shared-prefix traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paged-attention-prefix-kv-aliasing-under-mixed-shared-pref-954ef8cacd`
Run ID: `paged-attention-prefix-kv-aliasing-under-mixed-shared-pref-954ef8cacd-20260605T062401095272+0000`

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

- Parent run decision: Prefix KV Deduplication for Batch Long Context: enoch://control-plane/projects/prefix-kv-deduplication-for-batch-long-context-f182f8f1f1f0/runs/prefix-kv-deduplication-for-batch-long-context-f182f8f1f1f0-20260605T015001070281+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

Immutable full-prefix-page aliasing preserved KV content correctness in all 60 Tier 1 controlled cases, but the 30% every-case peak-page reduction threshold failed on mixed traces: reduction ranged from 9.63% to 50.23%, with 50% no-share mixes averaging 19.08%.

## Boundaries and scale limits

No real GPU attention kernel, production allocator, scheduler, request arrival/departure process, or real serving trace was measured. The result supports page-table correctness and bounded memory behavior only, not end-to-end latency or production memory savings.

## Claim scope

Controlled small direct simulator for paged KV cache full-prefix-page aliasing under mixed shared-prefix traces with 32 to 64 requests, 16-token pages, 48 decode steps, and mixed shared/unique/adversarial-tail prompt prefixes.

## Why it stopped

Tier 1 direct controlled evidence supports correctness but falsifies the stated every-case 30% peak-page reduction threshold on mixed traces with substantial unique-prefix traffic; this is not full production validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should replay a real paged-attention implementation or realistic trace buckets and stratify savings by full-page prefix reuse density.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-engine prefix KV aliasing stratified by prefix reuse density
- Success threshold: Zero correctness mismatches and at least 30% peak KV memory reduction in high-reuse buckets, with explicit failure or below-threshold reporting for low-reuse buckets rather than averaging them away.
- Stop condition: Stop if real-engine replay shows any correctness mismatch, or if high-reuse buckets still fail to reach 30% peak KV memory reduction after controlling for page size and prefix alignment.

## Evidence references

- Artifact root: `<local-path>/projects/paged-attention-prefix-kv-aliasing-under-mixed-shared-pref-954ef8cacd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
