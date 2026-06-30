# Exact-Anchor KV Compression for Needle Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-needle-retrieval-b4f62fd28a4b`
Run ID: `exact-anchor-kv-compression-for-needle-retrieval-b4f62fd28a4b-20260602T104915195035+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66e0858ba973

## What looked useful

Exact-anchor KV retention is a valid mechanism for sparse needle retrieval only if the true anchor is identified and kept; the naive policy is budget-fragile under anchor clutter, so future work must solve anchor precision/priority before real-model claims.

## Boundaries and scale limits

No real LLM, no learned anchor detector, no multi-layer cache dynamics, no natural prompt generation, and only 2048-8192 token synthetic contexts with 64-dimensional random keys and 750 trials per grid cell.

## Claim scope

Synthetic single-attention KV-cache retrieval with oracle-marked needle anchors: exact retention of the needle KV entry preserves retrieval under 8x-32x compression when marked anchors fit within budget, but unprioritized anchor retention degrades sharply when noisy/distractor anchors exceed budget.

## Why it stopped

Bounded synthetic proxy supports the mechanism but also early-falsifies the naive unprioritized exact-anchor policy under noisy anchors; this is not full LLM validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should implement a priority-scored anchor selector in a small real transformer KV-cache intervention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Priority-Scored Exact Anchors in a Small Transformer Needle Task
- Success threshold: At 16x compression with candidate anchors at least 2x over budget, priority-scored exact anchors achieve at least 90% retrieval accuracy and at least 15 percentage points over unprioritized exact anchors across three random seeds.
- Stop condition: Stop if the priority scorer cannot retain the true anchor above 75% under over-budget candidate anchors or if gains over recency/uniform are below 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-needle-retrieval-b4f62fd28a4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
