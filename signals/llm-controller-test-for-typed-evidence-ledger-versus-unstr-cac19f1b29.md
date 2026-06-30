# LLM controller test for typed evidence ledger versus unstructured notes under hidden drift

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-controller-test-for-typed-evidence-ledger-versus-unstr-cac19f1b29`
Run ID: `llm-controller-test-for-typed-evidence-ledger-versus-unstr-cac19f1b29-20260621T052854456901+0000`

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

- Parent run decision: Typed Evidence-Ledger Agent vs Unstructured Notes on Repeated Tool Tasks: enoch://control-plane/projects/typed-evidence-ledger-agent-vs-unstructured-notes-on-repeated-tool-tasks-0de05f28b57d/runs/typed-evidence-ledger-agent-vs-unstructured-notes-on-repeated-tool-tasks-0de05f28b57d-20260621T050402134045+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db62ea746c91

## What looked useful

Typed evidence gating achieved 1.000 accuracy and 0.000 stale false-accept rate; the unstructured notes first-match baseline achieved 0.500 accuracy and 1.000 stale false-accept rate on drifted stale claims.

## Boundaries and scale limits

120 generated cases, deterministic controller variants, no live LLM prompting, no realistic workload distribution, no adversarial prompt variation beyond retained stale note text.

## Claim scope

In a deterministic Tier 1 synthetic hidden-drift harness, a typed evidence ledger with active/superseded evidence checks prevented stale claim acceptance, while a recency-blind unstructured notes controller failed on stale drift cases.

## Why it stopped

Closed as no-paper useful signal: controlled synthetic mechanism support is not publication-grade evidence.

## Recommended next action

Run a bounded live-LLM deepen test with the same hidden-drift cases, matched prompts and budgets, and a success threshold focused on stale false-accept reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM hidden-drift controller test for typed ledgers versus unstructured notes
- Success threshold: Typed-ledger stale false-accept rate at least 50% lower than unstructured notes, typed current false-reject rate no worse by more than 10 percentage points, and at least 95% artifact completeness.
- Stop condition: Stop if typed-ledger stale false-accept reduction is below 20% or if artifact completeness falls below 95% after one fixed-seed run.

## Evidence references

- Artifact root: `<local-path>/projects/llm-controller-test-for-typed-evidence-ledger-versus-unstr-cac19f1b29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
