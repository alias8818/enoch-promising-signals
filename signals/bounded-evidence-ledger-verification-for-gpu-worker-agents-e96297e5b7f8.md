# Bounded Evidence Ledger Verification for GPU Worker Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-evidence-ledger-verification-for-gpu-worker-agents-e96297e5b7f8`
Run ID: `bounded-evidence-ledger-verification-for-gpu-worker-agents-e96297e5b7f8-20260611T023457832914+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb27cdc59ebe

## What looked useful

Full verification caught 100% of tested artifact, ledger, and checkpoint mutations. Bounded verification was about 3.4x faster on this tiny run, caught checkpoint mutation 100%, and caught artifact/index record mutation at 5.5%, matching the 32/512 sampling design rather than providing complete detection.

## Boundaries and scale limits

Synthetic CUDA matmul artifacts only; 512 records; tiny 256-byte artifacts; single local GB10 worker; no signed remote attestation, no concurrent appenders, no production agent traces, and no million-record scaling.

## Claim scope

Local synthetic CUDA-worker evidence ledger with 512 records, 8 Merkle checkpoints, full verification, and bounded sampled verification over 32 sampled records.

## Why it stopped

Proxy-scale local evidence produced a useful mechanism signal and a clear limitation: bounded sampling verifies checkpoints cheaply but only catches per-record artifact/index tampering when sampled and misses ordinary ledger JSONL edits when the compact index is the verifier input.

## Recommended next action

Run the bounded deepen follow-up with authenticated compact indexes and a detection-overhead curve; do not write a paper from this proxy-scale result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Authenticated bounded evidence ledger detection-overhead curve for GPU worker traces
- Success threshold: Show bounded verification has a documented detection probability model matching empirical tamper trials within 95% confidence intervals while reducing verifier work by at least 5x versus full verification on realistic traces.
- Stop condition: Stop if authenticated bounded verification still misses non-sampled tampering without a quantifiable policy advantage over full or manifest verification.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-verification-for-gpu-worker-agents-e96297e5b7f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
