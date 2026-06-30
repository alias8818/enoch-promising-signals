# Async gossip averaging for home CPU distributed training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-gossip-averaging-for-home-cpu-distributed-training-14b03b98391b`
Run ID: `async-gossip-averaging-for-home-cpu-distributed-training-14b03b98391b-20260522T114508647686+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/10b0868b9e9f

## What looked useful

Async gossip removes barrier cost versus synchronous averaging, but on the tested home-link synthetic objective the no-communication local-only control reached the target faster than gossip. The mechanism is useful only when online consensus or a deployable shared model is required during training.

## Boundaries and scale limits

Proxy-only evidence: no real multi-host networking, no PyTorch or language-model training, no node churn, no NAT behavior, simplified communication model, and a convex synthetic objective where local-only training is unusually competitive.

## Claim scope

In a deterministic synthetic linear-regression simulator with 8 heterogeneous CPU workers and modeled home/LAN bandwidth, async pairwise gossip reaches a loose target loss about 6.4x-7.2x faster than synchronous barrier averaging while maintaining lower model disagreement than local-only training.

## Why it stopped

Proxy simulation supports async gossip over barrier sync but early-falsifies the broader home-CPU distributed-training claim for simple convex objectives because local-only training was competitive or faster in home-link scenarios.

## Recommended next action

Stop this run as a no-paper mixed proxy result; next bounded test should use a real PyTorch non-IID task where online shared-model consensus is required and compare async gossip against local-only/post-hoc averaging and synchronous averaging.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch non-IID CPU training test for online gossip consensus
- Success threshold: Async gossip reaches the target validation loss at least 1.5x faster than synchronous averaging and at least 1.2x faster than local-only/post-hoc averaging, with final validation loss within 5% of the best baseline and final consensus gap less than half of local-only.
- Stop condition: Stop if local-only/post-hoc averaging matches or beats async gossip on time-to-target and final validation loss, or if gossip communication overhead prevents a 1.2x wall-clock advantage under the straggler setting.

## Evidence references

- Artifact root: `<local-path>/projects/async-gossip-averaging-for-home-cpu-distributed-training-14b03b98391b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
