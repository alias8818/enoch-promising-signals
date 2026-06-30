# Self-Speculative Decoding via Early-Layer Exit Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-layer-exit-drafting-a77375cc6cbd`
Run ID: `self-speculative-decoding-via-early-layer-exit-drafting-a77375cc6cbd-20260528T114013538369+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/636baa95d018

## What looked useful

Later early exits often rank the full-depth token in the top 10, but top-1 agreement, one-step speculative distribution overlap, and 4-token draft acceptance are far below the proxy speedup threshold. Best DistilGPT2 exit accepted 0.468 tokens per 4-token draft versus 3.667 required by the layer-cost proxy; best GPT-2-small exit accepted 0.450 versus 4.000 required.

## Boundaries and scale limits

Small GPT-2-family pretrained models only; 94 DistilGPT2 and 60 GPT-2-small usable validation snippets; 64-token contexts; 4-token greedy draft windows; no trained auxiliary exit head; no cache-aware serving latency implementation; no large-model or broad-corpus validation.

## Claim scope

On DistilGPT2 and GPT-2-small validation snippets, untrained early-layer exits formed by projecting intermediate hidden states through the final layer norm and tied LM head do not provide enough draft-token acceptance for self-speculative decoding speedup.

## Why it stopped

Proxy-scale but direct early-exit probes on two GPT-2-family models failed the acceptance threshold for speedup; this is an early falsification of the untrained mechanism, not a full validation of all trained self-speculative decoding variants.

## Recommended next action

Stop this run as a no-paper useful negative for untrained exits; the next bounded test should train or calibrate a lightweight early-exit head and require measured acceptance plus wall-clock speedup before considering larger serving benchmarks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Head for GPT-2-Small Self-Speculative Drafting
- Success threshold: On held-out text, a 4-token draft at an exit no deeper than 50% of GPT-2-small must average at least 3 accepted tokens per draft and show at least 1.15x measured wall-clock throughput over standard greedy decoding.
- Stop condition: Stop as negative if the trained/calibrated 50% exit remains below 2 accepted tokens per 4-token draft or fails to improve measured wall-clock throughput after a cache-aware implementation.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-layer-exit-drafting-a77375cc6cbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
