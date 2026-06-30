# Evidence-ledger gating in real tool-using LLM tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-gating-in-real-tool-using-llm-tasks-44771debd9`
Run ID: `evidence-ledger-gating-in-real-tool-using-llm-tasks-44771debd9-20260612T005348935987+0000`

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

- Parent run decision: Evidence-Ledger Agents: Forcing Falsifiable Claims Before Actions: enoch://control-plane/projects/evidence-ledger-agents-forcing-falsifiable-claims-before-actions-8fbc17cb8d30/runs/evidence-ledger-agents-forcing-falsifiable-claims-before-actions-8fbc17cb8d30-20260612T003201893539+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f44ce5341be3

## What looked useful

Strict post-hoc evidence gating can enforce provenance, but in this direct small test it mainly converted potential errors or malformed outputs into no-final outcomes and did not improve accuracy over a strong tool-using baseline.

## Boundaries and scale limits

Small controlled benchmark, deterministic lookup/calculator tools, one cached 1.5B local model, stale-hint adversary only; no open-ended web tools, no multi-step production agent traces, no larger frontier model comparison.

## Claim scope

In a 12-task controlled local tool-use benchmark with Qwen/Qwen2.5-1.5B-Instruct, strict evidence-ledger gating prevented unsupported final emissions but reduced completed correct answers from 11/12 to 4/12 because the model often failed to emit compliant cited final JSON after evidence was available.

## Why it stopped

Tier 1 direct test completed; result is a useful no-paper signal because the strict gate hurt finalization and did not improve baseline accuracy.

## Recommended next action

Run a bounded follow-up that adds a deterministic finalization adapter or constrained JSON decoder after ledger evidence is collected, then require gated accuracy to match baseline while maintaining zero unsupported final emissions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-aware finalization adapter for evidence-gated tool agents
- Success threshold: Adapter-assisted gate has 0 unsupported final emissions and accuracy no more than 5 percentage points below the ungated baseline, with final emission rate at least 90%.
- Stop condition: Stop if adapter-assisted gating still emits finals on less than 80% of tasks or drops accuracy by more than 10 percentage points versus baseline after prompt and parser fixes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-in-real-tool-using-llm-tasks-44771debd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
