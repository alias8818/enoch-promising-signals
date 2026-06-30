# Evidence Ledger Format Robustness on CPU Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89`
Run ID: `evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89-20260619T231252956198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

Machine-readable structure alone was insufficient: loose JSON had an 85.7% false-accept rate on invalid cases, while strict JSON with explicit invariants had 0.0% false accepts and 0.0% false rejects in the generated suite. Markdown was intermediate, missing polarity faults.

## Boundaries and scale limits

Synthetic local benchmark only; no real LLM/tool-agent transcripts, no independent human adjudication, no large perturbation corpus, and no downstream task-quality measurement.

## Claim scope

On 1,200 deterministic synthetic CPU-agent evidence-ledger cases, strict JSON validation with explicit cross-reference and polarity invariants accepted all clean cases and rejected all tested single-fault perturbations; loose shape-only JSON and simple markdown validators false-accepted semantic faults.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct/full validation of real agent evidence-ledger robustness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to replay the same validators on real or LLM-generated tool-agent transcripts with blinded fault injection and human labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transcript Evidence-Ledger Format Robustness
- Success threshold: Strict JSON validator false-accept rate at least 50% lower than both controls with false-reject rate no more than 5 percentage points higher on at least 200 labeled transcript-derived cases.
- Stop condition: Stop if strict validation has no false-accept advantage over both controls, or if false rejects exceed controls by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
