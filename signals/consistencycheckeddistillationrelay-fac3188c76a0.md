# ConsistencyCheckedDistillationRelay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `consistencycheckeddistillationrelay-fac3188c76a0`
Run ID: `consistencycheckeddistillationrelay-fac3188c76a0-20260619T161302144161+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

Consistency gates were useful for the exact failure mode targeted by this run: baselines either reused stale facts, accepted noisy later overrides, or answered unresolved conflicts, while the relay reached 12/12 accuracy with correct abstention on both unsupported-conflict tasks.

## Boundaries and scale limits

Synthetic JSONL traces only; no LLM extraction, embedding retrieval, real operator traces, long-context persistence, or production agent integration was tested.

## Claim scope

On a 12-task synthetic repeated-agent memory contradiction probe, a deterministic consistency-checked distillation relay outperformed no-memory, first-transcript, last-retrieval, and confidence-layered baselines by preserving supported corrections and abstaining on unresolved low-confidence conflicts.

## Why it stopped

Proxy-only useful signal is not paper-grade direct evidence; closing this worker run as no-paper evidence with artifacts and a bounded follow-up recommendation.

## Recommended next action

Run one bounded deepen follow-up on real or LLM-generated repeated-agent traces with blind labels and extraction noise; stop if relay accuracy is not at least 10 percentage points above the strongest baseline or if abstention precision falls below 0.8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blind Replay Trace Validation for Consistency-Checked Memory Relay
- Success threshold: Relay overall accuracy at least 10 percentage points above the strongest baseline, contradiction accuracy at least 0.85, and abstention precision at least 0.8 on unsupported conflicts.
- Stop condition: Stop as negative if the relay does not beat the strongest baseline by 10 percentage points, if abstention precision is below 0.8, or if benefits disappear when extraction noise is introduced.

## Evidence references

- Artifact root: `<local-path>/projects/consistencycheckeddistillationrelay-fac3188c76a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
