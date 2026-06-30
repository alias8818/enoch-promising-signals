# Ring-Reduce Gradient Ledger for 2-Node Homes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769`
Run ID: `ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769-20260528T191204224153+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9ad70054129c

## What looked useful

For a 256 MiB two-node gradient exchange, modeled clean-link ledger overhead was 0.077% to 1.208% depending on chunk size. Under 64 KiB chunks with transfer failure probability 0.0005, stateless retry used 10.808x the median bytes and 42.034x the p95 estimated time versus the ledger. At 256 KiB and failure probability 0.001, stateless retry used 2.440x median bytes and 8.236x p95 estimated time. Ledger trials completed with the chunk-delivery checksum invariant satisfied.

## Boundaries and scale limits

Proxy-only simulation: no real distributed training, no PyTorch/NCCL integration, no real NIC or filesystem fsync measurement, no burst-loss network trace, and no model convergence evidence.

## Claim scope

In a deterministic two-node protocol simulation, a per-chunk append-only gradient ledger can resume interrupted gradient exchanges and reduce retransmitted bytes/tail synchronization time versus stateless whole-step retry when chunk-transfer failures occur.

## Why it stopped

Closed as no-paper useful signal because the evidence is a controlled protocol simulation, not direct real-network or training evidence.

## Recommended next action

Deepen with a bounded real two-process TCP or PyTorch distributed prototype that injects mid-step failures and measures wall-clock recovery time, bytes sent, clean-link overhead, and gradient equality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fault-Injected Two-Process Gradient Ledger Prototype
- Success threshold: Across at least 100 injected-failure synchronization steps, ledger recovery shows >=2x lower median bytes and >=2x lower median wall-clock time than stateless retry, exact gradient equality after recovery, and <2% median clean-link overhead.
- Stop condition: Stop if the prototype cannot preserve exact gradient equality after interruption, or if clean-link overhead is >=2%, or if failure-case median byte/time savings are <2x.

## Evidence references

- Artifact root: `<local-path>/projects/ring-reduce-gradient-ledger-for-2-node-homes-f5d564a0f769`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
