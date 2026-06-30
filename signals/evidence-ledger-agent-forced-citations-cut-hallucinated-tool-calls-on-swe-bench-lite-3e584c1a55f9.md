# Evidence-Ledger Agent: Forced Citations Cut Hallucinated Tool Calls on SWE-bench-Lite

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-forced-citations-cut-hallucinated-tool-calls-on-swe-bench-lite-3e584c1a55f9`
Run ID: `evidence-ledger-agent-forced-citations-cut-hallucinated-tool-calls-on-swe-bench-lite-3e584c1a55f9-20260613T022630876177+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

Forced citations can cut hallucinated file-tool calls, but only works well when the ledger already contains useful repository evidence; issue-only citation gating is too brittle for many repair tasks.

## Boundaries and scale limits

No LLM agent, no repository checkout, no patches applied, and no SWE-bench tests executed. The tree-proxy condition uses gold paths as a stand-in for observed repository evidence and is not a full validation.

## Claim scope

Deterministic path-level SWE-bench-Lite metadata probe: citation gating sharply reduced unsupported decoy file-tool calls, but issue-only evidence retained too few useful gold file calls; a repository-tree proxy restored useful retention.

## Why it stopped

Closed as no-paper useful signal because the evidence is a deterministic proxy, not a full SWE-bench-Lite agent validation, and issue-only useful retention failed the probe threshold.

## Recommended next action

Run a bounded direct-agent A/B test on 30 SWE-bench-Lite tasks with the same model, comparing baseline tool use against evidence-ledger gating plus mandatory repo tree/search evidence acquisition.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct SWE-bench-Lite agent A/B test for evidence-ledger citation gating
- Success threshold: On at least 30 SWE-bench-Lite tasks with the same model, reduce unsupported tool calls by >=70%, retain >=80% useful calls, and keep resolved rate within 5 percentage points of baseline.
- Stop condition: Stop if unsupported-call reduction is below 40%, useful-call retention is below 60%, or resolved rate drops by more than 10 percentage points after the first 15 completed tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-forced-citations-cut-hallucinated-tool-calls-on-swe-bench-lite-3e584c1a55f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
