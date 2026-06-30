# Cross-Node Ledger Consensus for Quantized Home Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-node-ledger-consensus-for-quantized-home-agents-bd9dd34d5aca`
Run ID: `cross-node-ledger-consensus-for-quantized-home-agents-bd9dd34d5aca-20260524T210342985185+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Bucketed quantization improved commit availability versus exact matching, but ledger equality required a certified shared vote set. In the representative 5-node/1-Byzantine/noise case with 5% packet loss, certified buckets reached 0.818 commit rate and 1.000 final ledger match, while naive bucket quorum reached 0.678 commit rate but 0.000 final ledger match with 62.4 divergent rounds.

## Boundaries and scale limits

No real home-agent workload, model inference, durable storage, signatures, process isolation, view changes, recovery, or physical network was tested. The certified mode approximates a shared quorum certificate rather than implementing full reliable broadcast.

## Claim scope

Synthetic scalar-signal simulation of 3-7 nodes shows that deterministic coarse quantization plus a shared quorum certificate can keep honest hash-chain ledgers identical under bounded Byzantine faults, sensor noise, and 0-5% packet loss; naive per-receiver quorum and no-ledger controls diverge.

## Why it stopped

Synthetic evidence supports the bucket-plus-certificate mechanism but falsifies naive ledger quorum under equivocation; this is not full validation of cross-node consensus for deployed home agents.

## Recommended next action

Stop this run as no-paper useful signal; next build a small multi-process signed quorum-certificate prototype with durable replay and measure safety/liveness on real quantized agent outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable Signed Quorum Certificates for Quantized Home-Agent Ledgers
- Success threshold: On a 5-node/1-Byzantine setup with 5% induced message loss, honest nodes maintain identical ledger hashes across restart/replay with at least 80% commit rate and less than 1% false bucket commits across three traces.
- Stop condition: Stop if honest ledger hashes diverge after a committed certificate, replay cannot reconstruct the committed ledger, or commit rate stays below 50% on two traces after protocol bugs are fixed.

## Evidence references

- Artifact root: `<local-path>/projects/cross-node-ledger-consensus-for-quantized-home-agents-bd9dd34d5aca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
