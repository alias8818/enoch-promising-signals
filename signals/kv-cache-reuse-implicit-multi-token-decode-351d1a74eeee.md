# KV-cache reuse implicit multi-token decode

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-reuse-implicit-multi-token-decode-351d1a74eeee`
Run ID: `kv-cache-reuse-implicit-multi-token-decode-351d1a74eeee-20260605T012940937738+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/08462091ff1f

## What looked useful

Omitting the first generated token's K/V changed second-token logits in 0/7000 exact-ish random-transformer cases across prefix lengths 4, 16, and 64. Full-scale top-1 mismatch was 39.66% at prefix length 4, 1.8% at prefix length 16, and 2.3% at prefix length 64; the constructed dependency control mismatched 100%.

## Boundaries and scale limits

CPU-only NumPy probe; no trained LLM, no optimized serving kernel, no real prompts, no learned multi-token head, and no speculative verification path were tested.

## Claim scope

Bounded proxy evidence shows that naive implicit multi-token decoding by reusing only prefix KV and omitting intermediate generated-token K/V is not exact for causal decoders; second-token logits changed in every tiny-transformer trial and a constructed previous-token dependency failed in 100% of trials.

## Why it stopped

Proxy/early falsification, not full validation: the tested prefix-KV-only shortcut does not preserve autoregressive logits once intermediate generated-token K/V is omitted.

## Recommended next action

Stop this naive exactness path; only pursue a follow-up if it adds an explicit learned multi-token head or verifier and measures acceptance, quality, and speed against sequential KV decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verified multi-token head versus prefix-KV-only shortcut
- Success threshold: At least 1.2x verified end-to-end decode throughput on the same prompts with byte-identical final outputs versus sequential decoding, plus an ablation showing the gain is not from measurement noise.
- Stop condition: Stop if verified throughput is below 1.05x, acceptance rate is too low to offset verification overhead, or outputs are not byte-identical after verification.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-reuse-implicit-multi-token-decode-351d1a74eeee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
