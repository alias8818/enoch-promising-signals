# Signed Observation Recorder for Real Agent Evidence Ledgers

Status: `useful_signal`
Project ID: `signed-observation-recorder-for-real-agent-evidence-ledger-873e746277`
Run ID: `signed-observation-recorder-for-real-agent-evidence-ledger-873e746277-20260518T115904697910+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a648939756d

## What looked useful

The core signed-observation mechanism worked in a controlled direct test: valid ledgers verified with zero failures, all 4/4 mutation attacks were rejected, and isolated signing/hash-chain overhead was about 22 microseconds over unsigned append-only JSONL.

## Boundaries and scale limits

Tested only on one local machine with 300 real subprocess observations, 5,000 append-only observations, and four synthetic post-recording mutation attacks. Not tested for multi-agent operation, production Enoch integration, hostile host compromise, key exfiltration, distributed ordering, crash recovery, or long-running high-throughput workloads.

## Claim scope

Local Tier 1 evidence shows a Python Ed25519 plus hash-chain recorder can sign real subprocess observations, verify a valid JSONL evidence ledger, detect payload tampering, deletion, reordering, and wrong-signer append attacks, and add about 0.024 ms per append-only signed observation in this environment.

## Why it stopped

No-paper closure: Tier 1 direct mechanism evidence is useful but too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up that integrates the recorder into a real multi-step agent/tool trace and validates restart persistence plus a larger adversarial mutation suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Recorder on Real Multi-Step Agent Tool Traces
- Success threshold: At least 95% mutation detection over the expanded suite, zero verification failures on the unmodified ledger, append p95 below 1 ms per event, and successful verification after restart/resume.
- Stop condition: Stop as negative if any unmodified ledger fails verification, any basic tamper/delete/reorder/wrong-key attack passes verification, or append p95 exceeds 1 ms per event on the local workload.

## Evidence references

- Artifact root: `<local-path>/projects/signed-observation-recorder-for-real-agent-evidence-ledger-873e746277`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
