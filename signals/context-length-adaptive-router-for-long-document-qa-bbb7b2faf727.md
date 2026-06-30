# Context-Length Adaptive Router for Long-Document QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-length-adaptive-router-for-long-document-qa-bbb7b2faf727`
Run ID: `context-length-adaptive-router-for-long-document-qa-bbb7b2faf727-20260522T010245145307+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

Adaptive routing achieved 0.616 support coverage at 395.794 mean tokens versus fixed_8 at 0.616 support coverage and 614.707 mean tokens, a 35.6% token reduction with bootstrap cost-delta 95% CI [-239.980, -201.077] tokens and zero coverage delta on this test.

## Boundaries and scale limits

Synthetic data only; support coverage only; no public benchmark, no downstream QA model answer EM/F1, no dense retrieval, no production latency measurement, and no validation beyond k<=8 retrieved chunks.

## Claim scope

On a deterministic synthetic long-document QA support-coverage benchmark with lexical retrieval and 24 chunks per document, a threshold-calibrated context-length router matched fixed k=8 support coverage while reducing selected context tokens.

## Why it stopped

The result is a proxy mechanism validation, not a full long-document QA validation; it lacks real-data and downstream answer-generation evidence required for a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a public long-document QA benchmark and fixed answer model to measure answer EM/F1, support recall, token cost, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate Adaptive Context Routing on Public Long-Document QA
- Success threshold: Adaptive routing reduces mean selected tokens by at least 25% versus the strongest fixed_k baseline with answer EM/F1 no worse than 1 percentage point absolute and support recall no worse than 2 percentage points absolute on the held-out split.
- Stop condition: Stop if adaptive routing loses more than 3 percentage points answer EM/F1 against the comparable fixed-context baseline or saves less than 10% mean tokens after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/context-length-adaptive-router-for-long-document-qa-bbb7b2faf727`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
