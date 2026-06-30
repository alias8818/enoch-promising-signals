# Peer-to-peer 1-bit Adam for two 10GB home GPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `peer-to-peer-1-bit-adam-for-two-10gb-home-gpu-training-a2fbb748254c`
Run ID: `peer-to-peer-1-bit-adam-for-two-10gb-home-gpu-training-a2fbb748254c-20260607T145808429687+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14ba056c8bbc

## What looked useful

Across three seeds, dense Adam sync reached 0.7829 mean validation accuracy; 1-bit no-residual reached 0.7774 with 120.0 MB modeled communication over 600 steps versus 3.84 GB for dense. Naive residual/error-feedback reached only 0.7540, so the mechanism is mixed and implementation-sensitive.

## Boundaries and scale limits

Not tested on two physical 10GB GPUs, real peer-to-peer transport, real packed serialization, VRAM-constrained models, or language-model training; byte savings are modeled with ideal bit packing.

## Claim scope

Single-GB10, two-logical-worker CUDA proxy shows ideal 1-bit sign-plus-scale gradient exchange into Adam can reduce modeled communication by about 32x while preserving near-dense accuracy on a synthetic linear-teacher classification task.

## Why it stopped

Proxy-only closure: the run supports a communication/convergence mechanism but does not directly validate the two-10GB-home-GPU peer-to-peer training claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same variants on two physical consumer GPUs with measured peer transport and a small language-model workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct two-consumer-GPU peer transport test for 1-bit Adam
- Success threshold: 1-bit no-residual achieves at least 20% lower measured communication-bound step time than dense while staying within 1% relative validation loss or within 1 percentage point accuracy-equivalent metric after the bounded run.
- Stop condition: Stop if measured pack/transfer/unpack overhead erases communication savings or if validation quality falls more than 1 percentage point/equivalent versus dense in two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/peer-to-peer-1-bit-adam-for-two-10gb-home-gpu-training-a2fbb748254c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
