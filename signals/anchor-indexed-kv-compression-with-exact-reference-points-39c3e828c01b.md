# Anchor-Indexed KV Compression with Exact Reference Points

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-compression-with-exact-reference-points-39c3e828c01b`
Run ID: `anchor-indexed-kv-compression-with-exact-reference-points-39c3e828c01b-20260531T125920857253+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/66bf5b7704cf

## What looked useful

Exact anchor reference points give a smoothness-dependent compression signal, but anchor-only reconstruction is not a viable standalone KV-cache compression method for real pretrained traces. Future tests should add residuals, learned reconstruction, or adaptive anchors rather than rely on fixed exact anchors alone.

## Boundaries and scale limits

Synthetic AR(1) traces up to sequence length 512 and distilgpt2 Q/K/V captures up to 192 tokens on short technical prose; no end-to-end decoder-cache patch, long-context benchmark, perplexity run, throughput study, quantization, residual coding, adaptive anchors, or 7B+ model validation.

## Claim scope

Fixed-stride anchor-only KV reconstruction preserves causal attention outputs only for very smooth synthetic K/V traces; on a short distilgpt2 pretrained trace it produces large attention-output error even when storing about 27% of K/V vectors.

## Why it stopped

Bounded direct attention replay found large relative output error on distilgpt2 despite favorable memory ratios, so the standalone anchor-only hypothesis is a proxy/early falsification rather than a full validation.

## Recommended next action

Stop this anchor-only line as no-paper evidence; run a bounded follow-up that adds a small residual budget between exact anchors and requires low attention-output error on pretrained Q/K/V traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact Anchors with Low-Budget Residual KV Reconstruction
- Success threshold: At stride 4 or larger, achieve mean relative attention-output error <= 0.15 and mean attention KL <= 0.10 across distilgpt2 layers while using <= 0.35 effective KV memory.
- Stop condition: Stop if residual coding cannot reduce mean relative output error below 0.30 at <= 0.50 effective KV memory on distilgpt2, because it would not justify larger-model validation.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-with-exact-reference-points-39c3e828c01b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
