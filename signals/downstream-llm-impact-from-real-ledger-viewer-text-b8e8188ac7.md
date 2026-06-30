# Downstream LLM Impact From Real Ledger Viewer Text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `downstream-llm-impact-from-real-ledger-viewer-text-b8e8188ac7`
Run ID: `downstream-llm-impact-from-real-ledger-viewer-text-b8e8188ac7-20260527T060933238624+0000`

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

- Parent run decision: Real Ledger Parser and Viewer Injection Confirmation: enoch://control-plane/projects/real-ledger-parser-and-viewer-injection-confirmation-1dbc0c17f7/runs/real-ledger-parser-and-viewer-injection-confirmation-1dbc0c17f7-20260526T225831244308+0000
- Parent run decision: Adversarial Ledger Injection Stress Test: enoch://control-plane/projects/adversarial-ledger-injection-stress-test-c01ccd3cde03/runs/adversarial-ledger-injection-stress-test-c01ccd3cde03-20260525T024721117707+0000

## What looked useful

Real ledger-viewer text is useful downstream context for small LLM recovery of decision metadata, but it is not better than structured JSON and should be treated as a human-readable companion to machine-readable artifacts rather than a replacement.

## Boundaries and scale limits

The test is limited to local Enoch artifacts, one 1.5B local instruct model, deterministic field recovery, and 25 projects. It does not validate broader reasoning tasks, adversarial viewer pages, human-facing UI variants, API-scale models, or non-Enoch ledger domains.

## Claim scope

On 25 real completed Enoch project artifacts, real ledger-viewer text containing run notes plus rendered decision artifacts let Qwen2.5-1.5B-Instruct recover four decision labels with 0.92 all-fields exact accuracy and 0.98 mean per-field accuracy, strongly outperforming no-context, redacted, run-notes-only, and mismatched-viewer controls while roughly matching structured JSON.

## Why it stopped

Tier 2 evidence supports a scoped mechanism, but the task is still narrow label recovery and the structured JSON baseline remains slightly stronger, so publication-grade claims are not justified.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should ask models to answer nontrivial reasoning questions from real ledger-viewer pages rather than copy explicit decision labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reasoning QA From Real Ledger Viewer Text
- Success threshold: Full viewer text improves mean QA accuracy by at least 0.15 over run-notes-only and mismatched-viewer controls, stays within 0.05 of structured JSON, and wins paired comparisons on at least 70% of projects for two model sizes.
- Stop condition: Stop if viewer text fails to beat run-notes-only by 0.05 mean QA accuracy or mismatched-viewer errors show the model mostly follows irrelevant ledger text rather than target project context.

## Evidence references

- Artifact root: `<local-path>/projects/downstream-llm-impact-from-real-ledger-viewer-text-b8e8188ac7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
