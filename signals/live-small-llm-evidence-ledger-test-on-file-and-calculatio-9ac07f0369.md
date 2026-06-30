# Live small-LLM evidence-ledger test on file and calculation tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-small-llm-evidence-ledger-test-on-file-and-calculatio-9ac07f0369`
Run ID: `live-small-llm-evidence-ledger-test-on-file-and-calculatio-9ac07f0369-20260608T132522806479+0000`

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

- Parent run decision: Evidence ledger for small CPU agent reliability: enoch://control-plane/projects/evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a/runs/evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a-20260608T003135348502+0000
- Parent run decision: Evidence ledger on real small-agent file and calculation tasks: enoch://control-plane/projects/evidence-ledger-on-real-small-agent-file-and-calculation-t-e72f014853/runs/evidence-ledger-on-real-small-agent-file-and-calculation-t-e72f014853-20260608T062141407320+0000

## What looked useful

Evidence acquisition alone was insufficient: the no-gate ledger ablation acquired correct evidence but still produced unsupported/non-final behavior. The final-answer gate was the reliability mechanism, but it caused 25% overall abstention and 50% file-task abstention.

## Boundaries and scale limits

One 0.5B model, synthetic local tasks, 12 tasks per condition, deterministic programmatic auditor, simulated file contents, no public benchmark or independent labels.

## Claim scope

On a 36-episode fixed-seed Qwen/Qwen2.5-0.5B-Instruct local harness with hidden file_read and calculator tools, evidence-ledger final-answer gating eliminated unsupported final answers and improved calculation accuracy, but failed the preset abstention threshold on file tasks.

## Why it stopped

Medium direct test failed the stated threshold because ledger_gate abstention was 25%, above the 20% limit, despite eliminating unsupported finals.

## Recommended next action

Stop this run as a no-paper mixed result; next bounded test should modify the file-task finalization protocol and require abstention below 20% with unsupported final rate near zero on the same fixed seeds before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: File-task finalization protocol for small-LLM evidence ledgers
- Success threshold: Unsupported final rate <= 0.05, overall abstention <= 0.20, file-task abstention <= 0.20, and exact accuracy no worse than 5 absolute points below baseline on the same fixed seeds.
- Stop condition: Stop if file-task abstention remains above 20% or unsupported final rate rises above 5% under the modified finalization protocol.

## Evidence references

- Artifact root: `<local-path>/projects/live-small-llm-evidence-ledger-test-on-file-and-calculatio-9ac07f0369`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
