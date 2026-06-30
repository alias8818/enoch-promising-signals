# Gossip Averaging for Two-Node Home Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-for-two-node-home-distributed-training-ec34899ff4b8`
Run ID: `gossip-averaging-for-two-node-home-distributed-training-ec34899ff4b8-20260608T190605252039+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/90c415cb3930

## What looked useful

On a severe non-IID synthetic sweep, averaging every 4 local steps stayed within 0.625 percentage points mean accuracy of centralized while no averaging lost 6.650 points. A 124M-parameter fp16 exchange is estimated at 19.88 s on 100 Mbps uplink and 49.64 s on 40 Mbps uplink, making frequent uncompressed home averaging impractical.

## Boundaries and scale limits

No physical two-host network, no real WAN jitter, no GPU training, no language-model training, no compression, no optimizer-state exchange, and no multi-hour validation were tested. Large-model feasibility is estimated from payload size and nominal uplink bandwidth only.

## Claim scope

Synthetic two-worker MLP training with exact pairwise parameter averaging shows that frequent two-node gossip can track centralized SGD under non-IID shards, but uncompressed GPT-2-small-class exchanges over home uplinks are too slow for every-step averaging.

## Why it stopped

No-paper useful signal: the mechanism works in a small synthetic probe, but the practical home-training claim needs compression and real two-host measurements before it can be considered viable.

## Recommended next action

Run a bounded follow-up that adds top-k or quantized delta compression and adaptive averaging periods to measure whether bandwidth can drop at least 10x while keeping the hard-sweep accuracy gap under 2 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed two-node gossip averaging under hard non-IID skew
- Success threshold: At least 10x byte reduction versus full fp16 averaging with mean accuracy gap no worse than 2 percentage points against centralized on the hard sweep.
- Stop condition: Stop if no compression setting reaches both 5x byte reduction and less than 3 percentage point mean accuracy gap, or if compression destabilizes any seed relative to no averaging.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-for-two-node-home-distributed-training-ec34899ff4b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
