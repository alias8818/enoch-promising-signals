# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-e2725ddbc427`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-e2725ddbc427-20260602T115123615689+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3c64525017c9

## What looked useful

Natural text acceptance was very low: best Tiny Shakespeare mean accepted tokens was 0.068 with 3.95% draft-token accuracy and 0.299x estimated speed. A favorable high-repeat synthetic stream reached 1.297 mean accepted tokens and 67.94% draft-token accuracy at gamma 2, but still only 0.643x estimated speed because measured CPU verification of 3 tokens cost 3.57x a single-token step.

## Boundaries and scale limits

This was not a production transformer/KV-cache serving benchmark. Acceptance was measured against held-out text and synthetic streams, not actual sampled model continuations; verifier cost was proxied by NumPy matrix compute at sequence lengths 1, 3, 5, and 9.

## Claim scope

A simple CPU-side n-gram drafter, evaluated on held-out word-token streams with a measured single-thread NumPy CPU verifier-cost proxy, did not achieve estimated decoding speedup on natural text or on synthetic repeat controls.

## Why it stopped

Proxy early falsification rather than full validation: n-gram draft acceptance was below the measured CPU break-even threshold across natural text and favorable synthetic controls.

## Recommended next action

Stop this run as a proxy early falsification; only revisit with a real CPU transformer/KV-cache verifier if it can demonstrate substantially sublinear multi-token verification cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Verification for N-Gram Drafting
- Success threshold: At least 1.10x end-to-end tokens/sec improvement over baseline on a real CPU transformer runtime, with no quality-affecting change to the target model sampling distribution and at least 10k generated tokens per evaluated condition.
- Stop condition: Stop if measured multi-token verification cost requires mean accepted tokens above the maximum possible for the tested gamma, or if end-to-end throughput remains below 1.0x baseline on both small and medium CPU-runnable models.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-e2725ddbc427`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
