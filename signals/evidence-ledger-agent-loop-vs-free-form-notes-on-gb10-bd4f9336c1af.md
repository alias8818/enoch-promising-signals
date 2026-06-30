# Evidence-Ledger Agent Loop vs Free-Form Notes on gb10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-agent-loop-vs-free-form-notes-on-gb10-bd4f9336c1af`
Run ID: `evidence-ledger-agent-loop-vs-free-form-notes-on-gb10-bd4f9336c1af-20260620T054403286048+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/09b091fae8ea

## What looked useful

The ledger loop achieved 18/24 exact answers versus 24/24 for free-form notes, with paired accuracy discordance of 0 ledger-only wins and 6 free-form-only wins. Citation coverage was 8/24 for ledger versus 5/24 for free-form, a small non-conclusive gain. Ledger used 4277 generated tokens versus 1650 for free-form.

## Boundaries and scale limits

Single local model, one cleaned seed/task set, synthetic short-context QA, greedy decoding, prompt-only ledger without constrained decoding or parser repair; not evidence about larger models, real research workflows, long-horizon agents, or optimized ledger implementations.

## Claim scope

On 24 deterministic synthetic multi-evidence QA tasks using Qwen/Qwen2.5-1.5B-Instruct on GB10, a naive prompt-only evidence-ledger two-step loop reduced exact-answer accuracy versus a free-form notes two-step loop while only modestly improving required citation coverage.

## Why it stopped

Proxy/local experiment found an accuracy regression for the naive evidence-ledger loop, so the original improvement hypothesis is unsupported in the tested scope rather than ready for paper-positive validation.

## Recommended next action

Stop this run as a bounded no-paper useful negative signal; a follow-up should test schema-constrained ledger generation with parser validation across at least three seeds and two local model sizes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Schema-Constrained Evidence Ledger Agent Loop
- Success threshold: Ledger exact accuracy must be no worse than free-form by more than one task per seed and required citation coverage must improve by at least 15 percentage points on average.
- Stop condition: Stop if validated ledger generation still produces lower exact accuracy than free-form on two of three seeds or if citation coverage gain remains below 15 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-vs-free-form-notes-on-gb10-bd4f9336c1af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
