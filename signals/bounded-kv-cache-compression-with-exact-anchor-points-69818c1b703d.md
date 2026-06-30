# Bounded KV Cache Compression with Exact Anchor Points

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-cache-compression-with-exact-anchor-points-69818c1b703d`
Run ID: `bounded-kv-cache-compression-with-exact-anchor-points-69818c1b703d-20260609T222718882670+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/767dbb40cbe1

## What looked useful

Exact anchors preserved anchor retrieval in the base synthetic setting, but naive span summaries exposed an objective mismatch: count-mass summaries matched full attention output with mean relative L2 around 0.008 while collapsing anchor/recent exact retrieval; no-mass summaries preserved retrieval but had high output error.

## Boundaries and scale limits

No pretrained LLM, no real decoding, no GPU/kernel latency, no downstream long-context tasks, and no formal worst-case bound. Results are synthetic NumPy attention probes on a CPU worker.

## Claim scope

Attention-level synthetic KV-cache benchmark only: exact anchors improve retrieval versus sink+recent, and count-weighted block summaries approximate full attention outputs at 7.7x-11.7x slot compression but can mask exact-token retrieval.

## Why it stopped

Closed as no-paper useful signal: the synthetic attention evidence is mixed and exposes a concrete masking failure rather than validating the compression idea for real LLM inference.

## Recommended next action

Run a bounded follow-up that adds anchor-aware summary gating or score caps and tests whether it can keep mean relative L2 below 0.05 while preserving at least 0.95 anchor and recent retrieval on the same benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-aware gating for bounded KV span summaries
- Success threshold: On the base 4096-token synthetic benchmark, achieve mean relative L2 <= 0.05, cosine >= 0.99, anchor retrieval >= 0.95, recent retrieval >= 0.95, and at least 7x slot compression.
- Stop condition: Stop if no gated policy beats both count-mass retrieval and no-mass output error at the same block size, or if a small pretrained LM check shows the synthetic improvement does not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-compression-with-exact-anchor-points-69818c1b703d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
