# Speculative Decoding with Exact Anchor Verification for Fast Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-decoding-with-exact-anchor-verification-for-fast-inference-cd5791b2f671`
Run ID: `speculative-decoding-with-exact-anchor-verification-for-fast-inference-cd5791b2f671-20260610T195031136818+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7baa2397cd09

## What looked useful

Anchor-only verification reduced target queries by 2x-8x, but produced substantial distribution drift in every tested setting: mean token KL 0.080-0.177, 12-token prefix TV 0.453-0.857, and target-model log-probability gaps from -15.65 to -55.71 nats.

## Boundaries and scale limits

CPU-only synthetic Markov LM; no transformer, GPU serving, optimized kernel, or large-model latency validation. Query reduction is a proxy rather than a wall-clock inference result.

## Claim scope

Sparse exact anchor verification that samples/checks only anchor positions and copies draft interior tokens does not preserve the target autoregressive distribution in a controlled Markov-language-model proxy.

## Why it stopped

Proxy early falsification: sparse exact anchor checks alone fail distributional exactness before transformer-scale benchmarking is warranted.

## Recommended next action

Stop this sparse-anchor shortcut as an exact decoding method; only revisit with an explicit conditional bridge correction algorithm and proof/test of exactness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact Conditional Bridge Correction Between Speculative Anchors
- Success threshold: On the same Markov harness, mean token KL <= 0.005 and prefix TV no worse than a same-sample target-vs-target control, plus at least 1.5x measured wall-clock speedup on a small transformer versus non-speculative decoding.
- Stop condition: Stop if bridge correction requires target evaluation of every interior token or fails the Markov exactness threshold.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-exact-anchor-verification-for-fast-inference-cd5791b2f671`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
