# Crash-safe concurrent compact ledger in a GPU worker harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-safe-concurrent-compact-ledger-in-a-gpu-worker-harne-df47f9de08`
Run ID: `crash-safe-concurrent-compact-ledger-in-a-gpu-worker-harne-df47f9de08-20260602T140546088410+0000`

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

- Parent run decision: Compact Hash-Chain Evidence Ledger for GPU Worker Outputs: enoch://control-plane/projects/compact-hash-chain-evidence-ledger-for-gpu-worker-outputs-bc7c942e9d22/runs/compact-hash-chain-evidence-ledger-for-gpu-worker-outputs-bc7c942e9d22-20260601T102101381502+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/268e803ebadc

## What looked useful

Ordered durable commit markers recovered a contiguous valid prefix after 30 total killed ordered trials across final and replicate campaigns, with zero committed-after-invalid violations; a forced unsafe unordered control produced violations in 5/5 trials.

## Boundaries and scale limits

Small ledgers only; process SIGKILL rather than power loss; one filesystem/host; one appender process; CUDA used for record generation, not sustained GPU pressure; no multi-process, dm-flakey, or hardware flush validation.

## Claim scope

Bounded Tier-1 direct test of a single-process CUDA-record GPU worker harness using concurrent host append threads and an ordered two-phase compact ledger on one Linux GB10 host.

## Why it stopped

Tier-1 direct mechanism support was obtained, but evidence is bounded local no-paper evidence rather than publication-grade crash-safety validation.

## Recommended next action

Run a medium deepen test with randomized kill timings, larger ledgers, multi-process appenders, and filesystem/device fault injection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium randomized crash and filesystem-fault validation for ordered compact GPU-worker ledger
- Success threshold: Zero prefix violations across the randomized and fault-injected campaigns, with recovered-prefix progress in at least 95% of kill trials and documented throughput overhead.
- Stop condition: Stop if any ordered-ledger run shows a committed record after the first invalid slot, checksum/index corruption within the accepted prefix, or unacceptable durability overhead relative to a serialized baseline.

## Evidence references

- Artifact root: `<local-path>/projects/crash-safe-concurrent-compact-ledger-in-a-gpu-worker-harne-df47f9de08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
