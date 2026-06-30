# Evidence-ledger correction on real small-agent tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-correction-on-real-small-agent-tool-traces-4ae6b44b24`
Run ID: `evidence-ledger-correction-on-real-small-agent-tool-traces-4ae6b44b24-20260525T094348568390+0000`

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

- Parent run decision: Evidence-Ledger Self-Correction for Small CPU Agents: enoch://control-plane/projects/evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e/runs/evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e-20260525T091321098709+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/be15fec6b4ab

## What looked useful

On real small-agent command traces, ledger-backed correction fixed 900/900 injected structured factual errors and preserved 900/900 true claims; no-correction baseline overall accuracy was 0.500 and ledger-corrected overall accuracy was 1.000.

## Boundaries and scale limits

Tested on 30 local JSONL logs, 300 command evidence items, and 1800 templated claim cases with injected corruptions. It does not test free-form claim extraction, naturally occurring agent mistakes, semantic entailment, or human-adjudicated correction quality.

## Claim scope

A deterministic evidence ledger can correct templated structured factual claims about command exit code, output line count, and output SHA-256 prefix when those claims reference evidence items parsed from real Codex/Enoch small-agent tool traces.

## Why it stopped

Tier 1 controlled direct test succeeded on real trace evidence, but the result is still templated/injected-error mechanism evidence rather than publication-grade free-form agent reliability evidence.

## Recommended next action

Run a bounded deepen follow-up using natural small-model agent summaries over real traces, automatic claim extraction, and blind or deterministic labels for unsupported and corrected claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural summary claim extraction for real agent evidence-ledger correction
- Success threshold: At least 50 real traces and 300 extracted factual claims, unsupported-claim rate reduced by >=50% versus no correction, supported-claim preservation >=90%, and correction precision >=85%.
- Stop condition: Stop if claim extraction maps fewer than 100 factual claims to evidence items or if correction precision is below 70% on the first labeled batch.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-correction-on-real-small-agent-tool-traces-4ae6b44b24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
