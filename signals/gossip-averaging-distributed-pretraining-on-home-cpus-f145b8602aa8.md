# Gossip-Averaging Distributed Pretraining on Home CPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-distributed-pretraining-on-home-cpus-f145b8602aa8`
Run ID: `gossip-averaging-distributed-pretraining-on-home-cpus-f145b8602aa8-20260528T213002651937+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/323a2ef4999d

## What looked useful

Gossip averaging is a plausible communication-reduction mechanism for local-SGD language-model training: it strongly outperformed local-only training and nearly matched all-reduce in the bounded proxy, but degradation appeared when communication was made too infrequent.

## Boundaries and scale limits

Synthetic Markov character data, 96x96 softmax model, four simulated workers, no real sockets, no residential network latency/churn/stragglers, no transformer or GPT-2-small-class model, and runs under seconds rather than long pretraining.

## Claim scope

In a single-process CPU simulation of four non-IID workers training a small next-token softmax language model, periodic ring gossip every 10 local steps matched all-reduce within about 0.08% validation loss on two seeds while using 50% less simulated parameter traffic.

## Why it stopped

No-paper closure: this run produced a useful proxy/mechanism signal but not direct publication-grade evidence for distributed pretraining on real home CPUs.

## Recommended next action

Run a bounded deepen follow-up with real multi-process TCP workers on separate CPU hosts or containers, injecting residential-like latency and stragglers, before considering transformer-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-socket gossip averaging under home-network delay and stragglers
- Success threshold: Gossip remains within 1% validation loss of all-reduce while reducing transferred bytes or synchronization wait time by at least 30% in at least two of three seeds.
- Stop condition: Stop if gossip is more than 3% worse than all-reduce validation loss at matched compute in two seeds, or if real communication overhead makes wall-clock tokens/sec worse than all-reduce by more than 20% without a byte/wait-time advantage.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-distributed-pretraining-on-home-cpus-f145b8602aa8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
