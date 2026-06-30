# Gossip Evidence Ledger on CPU Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-evidence-ledger-on-cpu-nodes-b4ba531f4652`
Run ID: `gossip-evidence-ledger-on-cpu-nodes-b4ba531f4652-20260603T180430837711+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

Low-fanout gossip converged in every 64-node trial and all honest nodes detected injected equivocation, but naive entry-push anti-entropy has high bandwidth cost; fanout 1 used about 0.35 GB ledger bytes versus about 10.0 GB for all-peer broadcast, while fanout 6 reduced median convergence only from round 92 to 81 at about 6.1x the fanout-1 bytes.

## Boundaries and scale limits

No real network, disk-backed persistence, signature verification, node churn, adversarial scheduler, or multi-host CPU contention was tested. Results should not be read as production or paper-grade validation.

## Claim scope

Synthetic single-process simulations of a hash-addressed append-only evidence ledger on 64 CPU-modeled nodes with lossy low-fanout gossip, malicious fork injection, and an all-peer broadcast control.

## Why it stopped

No-paper closure: this run produced useful synthetic protocol evidence, but it is not direct real-node validation and exposes bandwidth limitations in the naive entry-push design.

## Recommended next action

Build a compact digest/set-reconciliation variant and rerun the same bounded simulation plus a small real-VM CPU cluster test before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Digest-Reconciled Gossip Evidence Ledger
- Success threshold: At 64 synthetic nodes and in a small real CPU cluster, maintain full honest conflict detection and final completeness while reducing bytes per entry per node by at least 5x versus fanout-1 entry-push gossip.
- Stop condition: Stop if digest reconciliation fails to converge within the same settle window, misses any injected conflict at honest nodes, or reduces bandwidth by less than 2x versus fanout-1 entry-push gossip.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-evidence-ledger-on-cpu-nodes-b4ba531f4652`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
