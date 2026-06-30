# Real LLM Tool-Agent Hidden-Drift Ledger Test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-llm-tool-agent-hidden-drift-ledger-test-938aafc871`
Run ID: `real-llm-tool-agent-hidden-drift-ledger-test-938aafc871-20260612T113025340328+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Mandatory Evidence-Ledger Agent on Local Multi-Step Tasks: enoch://control-plane/projects/mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153/runs/mandatory-evidence-ledger-agent-on-local-multi-step-tasks-ca4212a93153-20260611T110701531659+0000
- Parent run decision: LLM File-Agent Evidence Ledger on Hidden-Drift Local Tasks: enoch://control-plane/projects/llm-file-agent-evidence-ledger-on-hidden-drift-local-tasks-4b202643bc/runs/llm-file-agent-evidence-ledger-on-hidden-drift-local-tasks-4b202643bc-20260611T133203602410+0000

## What looked useful

The no-ledger baseline and ledger both reached 100% exact final answers with 0% stale-answer drift, so the ledger failed the predeclared improvement threshold. The ledger also mislabeled stale values as current facts in 15.56% of ledger outputs, weakening the mechanism claim.

## Boundaries and scale limits

Synthetic transcripts rather than live tools; one small instruction model; 405 total generations; prompt-level intervention only; no production agent memory or multi-model robustness.

## Claim scope

For Qwen/Qwen2.5-1.5B-Instruct on 45 seeded synthetic-but-tool-shaped hidden-drift transcripts with 3 LLM seeds, an explicit hidden-drift ledger prompt did not improve final-answer correctness over a no-ledger baseline.

## Why it stopped

Medium fixed-seed validation with a real baseline directly failed the ledger improvement threshold and exposed ledger audit-state errors.

## Recommended next action

Stop this follow-up as a useful negative/null Tier 2 result; do not write a paper from this evidence.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-tool-agent-hidden-drift-ledger-test-938aafc871`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
