# KV-Cache Linear Probe Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-linear-probe-drafting-c7dd87616b44`
Run ID: `kv-cache-linear-probe-drafting-c7dd87616b44-20260525T125641553934+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40dd4190e197

## What looked useful

Layer-5 K/V probes carried non-trivial linearly decodable next-token signal: 19.58% actual next-token accuracy versus 3.96% unigram, 0.59% copy, and 1.86% shuffled-label control. The target model assigned mean probability 0.1094 to the probe top-1 token, about 33.37% of its own mean top-1 probability.

## Boundaries and scale limits

Small-model local proxy only: no direct speculative decoding loop, no serving latency benchmark, no larger-model validation, no multi-corpus robustness, and no comparison to hidden-state probes or auxiliary draft models.

## Claim scope

On frozen distilgpt2 with WikiText-2, linear classifiers trained on concatenated per-position K/V cache vectors decode next-token drafting signal well above unigram, copy, and shuffled-label controls, with the best layer-5 probe reaching 19.58% next-token accuracy and 20.41% teacher-greedy agreement on 2048 held-out positions.

## Why it stopped

Current run is a small proxy mechanism test, not full validation; it supports a useful signal but lacks direct acceptance, latency, and scale evidence required for a paper-ready claim.

## Recommended next action

Run a bounded direct speculative-decoding acceptance experiment using the trained layer-5 K/V probe and compare accepted tokens per target forward against unigram, shuffled-label, and hidden-state-probe controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct speculative acceptance for K/V linear probe drafts
- Success threshold: Layer-5 K/V probe achieves at least 15% teacher-verified one-token acceptance and at least 3x the shuffled-label control acceptance without probe overhead exceeding the saved target compute in the measured loop.
- Stop condition: Stop if the K/V probe acceptance is below 10%, less than 2x shuffled-label control, or wall-clock overhead eliminates any target-forward savings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-linear-probe-drafting-c7dd87616b44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
