# Real-Trace Ground-Truth Completeness Check for Local-Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-trace-ground-truth-completeness-check-for-local-agent-92a8e741b7`
Run ID: `real-trace-ground-truth-completeness-check-for-local-agent-92a8e741b7-20260527T042413963954+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Independent Ground-Truth Completeness Check for Local-Agent Evidence Ledgers: enoch://control-plane/projects/independent-ground-truth-completeness-check-for-local-agen-75f49ee193/runs/independent-ground-truth-completeness-check-for-local-agen-75f49ee193-20260526T214721195812+0000
- Parent run decision: Intercepted Evidence Ledger on Real Local-Agent Tool Calls: enoch://control-plane/projects/intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b/runs/intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b-20260526T150041318082+0000

## What looked useful

Artifact-aware ledgers materially improved real-trace completeness recall over command-history (+0.6020) and transcript (+0.7960) baselines. Hash ablation lost all output-tamper detection, and support-link ablation lost all final-claim support recall.

## Boundaries and scale limits

Ground truth is extracted from platform JSONL logs, not from an independent OS/process/filesystem sidecar. Final-claim support is structural rather than semantic. The result does not validate production key custody, concurrent writers, filesystem read/write completeness, network provenance, or human-reviewed claim necessity.

## Claim scope

On 1,976 real Codex/Enoch local-agent JSONL traces with 42,790 completed command events, a structured artifact ledger checked against the platform trace manifest achieved complete command/output/status/support coverage and detected injected command deletions and output-hash tampering, outperforming transcript-only and command-history baselines.

## Why it stopped

No-paper useful signal: the Tier-3 bounded real-trace run supports the mechanism relative to platform JSONL ground truth, but independent sidecar ground truth and semantic claim-support review are still missing.

## Recommended next action

Run a depth-4 bounded sidecar-instrumented validation on live local-agent tasks with OS/process/filesystem manifests and manually reviewed final-claim support links; stop if it fails to preserve at least 95% completeness and tamper detection with a 0.4 completeness advantage over command history.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sidecar-instrumented real local-agent evidence-ledger completeness validation
- Success threshold: Artifact ledger completeness recall >= 0.95, tamper/omission detection >= 0.95, final-claim support recall >= 0.90, and completeness advantage over command-history baseline >= 0.40 across at least 50 live tasks.
- Stop condition: Stop as no-paper negative if sidecar-manifest completeness falls below 0.90, tamper detection falls below 0.90, or the advantage over command history is below 0.25 after the full fixed task set.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-ground-truth-completeness-check-for-local-agent-92a8e741b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
