# Evaluate verified safety evidence chains on real small local-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evaluate-verified-safety-evidence-chains-on-real-small-loc-464e68602b`
Run ID: `evaluate-verified-safety-evidence-chains-on-real-small-loc-464e68602b-20260529T093043430782+0000`

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

- Parent run decision: Falsifiable Safety Evidence Chains for Small Local Agents: enoch://control-plane/projects/falsifiable-safety-evidence-chains-for-small-local-agents-5a61a379b13a/runs/falsifiable-safety-evidence-chains-for-small-local-agents-5a61a379b13a-20260529T052913566775+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/91d47f7f6764

## What looked useful

The Tier 1 controlled direct test met its threshold: 14/14 claim verdicts correct, 0 false accepts, 0 false rejects, and 100% unsupported-claim detection on four deliberately unsupported safety claims grounded in actual local command traces.

## Boundaries and scale limits

Only 14 claims and 7 traces were tested; most traces were controlled by this harness; claim types were limited to no-network, no-file-write, no-destructive-command, pipefail-guarded-tee, and artifact-exists; verifier logic was lexical and not tested against adversarial obfuscation or independent human labels.

## Claim scope

A small evidence-chain verifier can correctly accept or reject a narrow set of safety claims over 7 real local-agent command traces, including controlled shell traces and this project's Codex JSONL trace.

## Why it stopped

No-paper closure: the direct Tier 1 test supports the mechanism on small real local traces, but evidence remains too narrow and controlled for a paper claim.

## Recommended next action

Run a bounded deepen follow-up on at least 30 independent local-agent traces with independently labeled safety claims and a summary-only baseline; stop here for paper purposes because this run is a small controlled mechanism signal, not publication-grade validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence-chain safety verification on independent local-agent trace corpus
- Success threshold: Zero false accepts on high-risk unsupported claims and at least 90% overall claim-level accuracy across 30 or more independent traces, with better unsupported-claim recall than the summary-only baseline.
- Stop condition: Stop as negative if any high-risk unsupported claim is falsely accepted or if accuracy does not exceed the summary-only baseline by at least 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-verified-safety-evidence-chains-on-real-small-loc-464e68602b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
