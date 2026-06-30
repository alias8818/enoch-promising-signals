# Bounded Distributed Home Training: GB10 + LAN Peers Toy Proof

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-distributed-home-training-gb10-lan-peers-toy-proof-12c6ac7f4586`
Run ID: `bounded-distributed-home-training-gb10-lan-peers-toy-proof-12c6ac7f4586-20260629T061222038717+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58869bd8e939

## What looked useful

The mechanism worked, but it was slower and slightly lower quality than GPU-only: GPU-only reached 0.6452 eval accuracy and 0.9364 loss in 1.0105 s, while GB10 plus two CPU peers reached about 0.629 eval accuracy and 0.998 loss with 1.21-1.32 s wall time. Rank-0 CUDA compute was fast, but it waited on slower CPU peers, making straggler control the dominant issue.

## Boundaries and scale limits

Peers were local CPU processes over loopback TCP, not real LAN machines. The test used a 332,808-parameter synthetic MLP and 245,760 synthetic examples, not a GPT-2-small-class model, real corpus, real multi-host networking, peer churn, or long-duration training.

## Claim scope

On one GB10 host, a PyTorch Gloo/TCP loopback toy run can coordinate one CUDA rank with two CPU peer ranks using synchronous parameter averaging and can converge near a GPU-only synthetic-classification control at equal global example count.

## Why it stopped

Bounded loopback proxy completed and produced a useful no-paper signal: the orchestration mechanism works, but the tested peer setup did not improve throughput or quality versus GPU-only and does not validate real LAN scaling.

## Recommended next action

Run the same toy trainer on at least two physical LAN machines and add an asynchronous or stale-update variant; stop treating loopback CPU peers as evidence that home LAN peers improve GB10 training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-machine LAN FedAvg with asynchronous peer updates
- Success threshold: A real multi-host LAN run reaches the same evaluation loss as GPU-only within 5 percent while improving wall-clock throughput by at least 10 percent, or clearly identifies the peer/communication threshold where benefit starts.
- Stop condition: Stop if real LAN synchronous and asynchronous variants both remain at least 10 percent slower than GPU-only at equal quality, or if peer setup/network instability prevents reproducible runs after two independent attempts.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-distributed-home-training-gb10-lan-peers-toy-proof-12c6ac7f4586`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
