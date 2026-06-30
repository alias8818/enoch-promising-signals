# Home Delta-Compressed Distributed

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-delta-compressed-distributed-2615551bb97b`
Run ID: `home-delta-compressed-distributed-2615551bb97b-20260522T110504893596+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e0acb91f60c2

## What looked useful

On the hard 5-seed profile, dense reached 0.97534 mean accuracy with 81.1 MB uploaded and 32.44 s modeled upload time. Top-k 1% reached 0.97427 mean accuracy with 1.62 MB uploaded and 0.648 s modeled upload time, a 50.04x byte reduction with about 0.00108 absolute accuracy loss. Top-k 0.1% reduced bytes by 501.91x but lost about 0.0173 absolute accuracy, marking a likely compression limit for this setup.

## Boundaries and scale limits

Evidence is synthetic and simulator-only. It does not test real home networking, packet overhead, latency, packet loss, NAT traversal, heterogeneous machines, stragglers, privacy/security constraints, or large-model/GPT-2-class training.

## Claim scope

In a local PyTorch simulator with 4 sequentially simulated non-IID workers training a 101386-parameter MLP, sparse top-k parameter-delta exchange with error feedback can preserve final accuracy close to dense delta exchange while sharply reducing modeled upload bytes over a 20 Mbps home-uplink model.

## Why it stopped

No-paper closure: the mechanism is supported by bounded simulator evidence, but the core home-distributed systems claim still needs direct network evidence before paper writing.

## Recommended next action

Run a bounded real-network or network-emulated multi-process follow-up that measures wall-clock round time, retry/failure behavior, and convergence under 20 Mbps uplink and realistic latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Network-Emulated Delta-Compressed Distributed Training
- Success threshold: Top-k 1% stays within 1.0 absolute percentage point of dense final accuracy and achieves at least 20x measured communication-time reduction across 5 seeds.
- Stop condition: Stop if top-k 1% loses more than 2.0 absolute percentage points versus dense, measured communication speedup is below 10x, or network overhead dominates enough that byte savings do not translate into wall-clock improvement.

## Evidence references

- Artifact root: `<local-path>/projects/home-delta-compressed-distributed-2615551bb97b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
