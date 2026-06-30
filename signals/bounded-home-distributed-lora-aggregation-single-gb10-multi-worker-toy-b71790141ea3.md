# Bounded Home-Distributed LoRA Aggregation: Single-GB10 Multi-Worker Toy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-home-distributed-lora-aggregation-single-gb10-multi-worker-toy-b71790141ea3`
Run ID: `bounded-home-distributed-lora-aggregation-single-gb10-multi-worker-toy-b71790141ea3-20260619T123913217877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Near-IID federated LoRA factor averaging reached 0.6777 accuracy versus centralized LoRA at 0.6758, but default non-IID aggregation reached only 0.4183 best accuracy versus centralized 0.5420; doubling non-IID rounds to 16 did not close the gap. Naive home-distributed LoRA aggregation appears conditionally viable but brittle to non-IID local objectives.

## Boundaries and scale limits

No real multi-host networking, no real language model, one seed, synthetic data only, tiny adapter and classifier scale, no privacy/straggler/failure modeling, and no full GB10 memory-pressure validation.

## Claim scope

Toy single-GB10 experiment with four simulated workers training rank-4 LoRA adapters on a frozen synthetic linear classifier. Simple adapter aggregation matches centralized LoRA under near-IID worker shards but loses substantial accuracy under the tested non-IID shard shifts.

## Why it stopped

Proxy/toy evidence supports a mechanism and exposes a non-IID failure mode, but it is not direct language-model or multi-host evidence and is insufficient for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded small-transformer follow-up that tests a concrete non-IID mitigation against centralized LoRA and naive aggregation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer non-IID LoRA aggregation mitigation test
- Success threshold: Mitigated federated LoRA reaches at least 90% of centralized LoRA quality and improves at least 10 percentage points over naive aggregation on the non-IID setting without increasing communication beyond adapter deltas by more than 2x.
- Stop condition: Stop as negative if the mitigation fails to beat naive aggregation by at least 5 percentage points on two seeds or if centralized LoRA itself fails to improve meaningfully over the frozen base.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-home-distributed-lora-aggregation-single-gb10-multi-worker-toy-b71790141ea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
