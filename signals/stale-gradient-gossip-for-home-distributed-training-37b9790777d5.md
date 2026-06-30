# Stale-Gradient Gossip for Home Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stale-gradient-gossip-for-home-distributed-training-37b9790777d5`
Run ID: `stale-gradient-gossip-for-home-distributed-training-37b9790777d5-20260526T003732204125+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Stale-gradient gossip reached the fixed loss threshold in 20s median simulated time versus 60s for local periodic averaging and 120s for synchronous all-reduce in the 30-seed main sweep; high-delay and high-drop ablations preserved the advantage, but staleness attenuation itself was not a decisive mechanism.

## Boundaries and scale limits

Proxy-only CPU simulation; no real multi-host training, no transformer model, no measured network stack, no optimizer-state or checkpoint validation, and no datacenter-scale evidence.

## Claim scope

In a bounded synthetic non-IID logistic-regression discrete-event simulation of eight heterogeneous home workers, asynchronous stale-gradient gossip improved simulated wall-clock convergence versus synchronous all-reduce and periodic local averaging.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic/proxy-only and the attenuation mechanism was not isolated strongly enough for a paper claim.

## Recommended next action

Run a bounded real multi-process small language-model experiment with injected delay/drop to test whether the simulated no-barrier advantage survives actual optimizer, communication, and validation-perplexity dynamics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real multi-process small-LM stale-gradient gossip under injected home-network delay
- Success threshold: Asynchronous gossip reaches the same validation perplexity at least 1.5x faster wall-clock than the best baseline without worse final perplexity by more than 2% across repeated runs.
- Stop condition: Stop if asynchronous gossip is slower than periodic local SGD or has more than 2% worse final validation perplexity in two repeated bounded runs under the target delay/drop profile.

## Evidence references

- Artifact root: `<local-path>/projects/stale-gradient-gossip-for-home-distributed-training-37b9790777d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
