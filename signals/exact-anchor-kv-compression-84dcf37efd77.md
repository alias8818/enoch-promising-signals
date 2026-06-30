# Exact-Anchor KV Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-kv-compression-84dcf37efd77`
Run ID: `exact-anchor-kv-compression-84dcf37efd77-20260608T032817364487+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Exact-anchor retention reduced mean relative attention-output error by 16.6% at 4k/8:1 compression and 10.6% at 16k/16:1 compression in anchor-heavy synthetic cases, while diffuse controls showed no useful advantage.

## Boundaries and scale limits

No real pretrained model KV traces, perplexity, next-token distribution, multi-layer cache, production decode latency, or long-context serving benchmark was run. Evidence is limited to PyTorch synthetic attention workloads up to sequence length 16384 and 16:1 compression.

## Claim scope

Synthetic direct attention/KV-cache tests show that preserving calibration-salient anchors exactly while bucket-compressing the remaining KV entries reduces attention-output reconstruction error when attention has planted anchor structure.

## Why it stopped

Current result is a synthetic direct-mechanism useful signal, not full validation or paper-ready evidence.

## Recommended next action

Run a bounded real-model KV-trace follow-up on GPT-2-small-class or similar local models, using an anchor-salience gate and measuring next-token KL/perplexity plus decode overhead against bucket-only and uniform-exact controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for exact-anchor compression
- Success threshold: At 8:1 or stronger compression, exact-anchor retention improves next-token KL or perplexity delta by at least 10% over bucket-only and uniform-exact controls on anchor-concentrated traces, with no regression when the anchor gate disables on diffuse traces.
- Stop condition: Stop if real-model traces do not show anchor concentration or if exact-anchor retention fails to beat bucket-only/uniform-exact controls by at least 5% on next-token KL or perplexity delta.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-84dcf37efd77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
