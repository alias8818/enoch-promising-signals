# Async gossip averaging of home LoRA adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-gossip-averaging-of-home-lora-adapters-91a0c0f2f786`
Run ID: `async-gossip-averaging-of-home-lora-adapters-91a0c0f2f786-20260525T050931143930+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/11a49bfa7e02

## What looked useful

Async gossip is plausible only when the averaged representation is stable. Delta-space averaging/canonicalization avoids the LoRA gauge failure in the toy test, while naive factor averaging can corrupt even functionally identical adapters.

## Boundaries and scale limits

Synthetic dense linear adapters only; no transformer LoRA, no real user data, no real residential network, no privacy or quantization layer, and no datacenter-scale or long-duration validation.

## Claim scope

In a small synthetic linear LoRA regression setting with 16 non-IID clients, asynchronous pairwise gossip can reach the shared low-rank target error and slightly improve client MSE versus isolated local adapters, but naive factor-space averaging is not representation invariant and fails under equivalent random gauge reparameterizations.

## Why it stopped

Proxy-only synthetic evidence produced a useful mechanism signal and an early falsification of naive factor averaging, but it is not full validation of home LoRA adapter gossip.

## Recommended next action

Run a bounded direct follow-up on a tiny transformer LoRA task with non-IID client splits, comparing factor gossip, canonicalized/delta gossip, server FedAvg, and isolated adapters under matched communication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny transformer LoRA gossip with canonicalized adapter averaging
- Success threshold: Canonicalized or delta-space async gossip is within 5% relative validation loss of server FedAvg and improves over isolated adapters on at least two of three seeds, while naive factor averaging shows either worse stability or a documented alignment requirement.
- Stop condition: Stop if all gossip variants fail to beat isolated adapters or if canonicalized/delta averaging exceeds the communication/compute budget by more than 2x for the same validation quality.

## Evidence references

- Artifact root: `<local-path>/projects/async-gossip-averaging-of-home-lora-adapters-91a0c0f2f786`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
