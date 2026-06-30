# Real-teacher answer-divergence instruction selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `57`
Project ID: `real-teacher-answer-divergence-instruction-selection-811b5fbbf8`
Run ID: `real-teacher-answer-divergence-instruction-selection-811b5fbbf8-20260629T082250542428+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `57`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Answer-divergence instruction data selection benchmark: enoch://control-plane/projects/adg-answer-divergence-data-selection-20260628/runs/adg-answer-divergence-data-selection-20260628-20260629T063237122388+0000
- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-208 frontier research issue: linear-ALI-208
- Answer-divergence instruction data selection benchmark: https://arxiv.org/abs/2604.10448v1
- Answer-divergence instruction data selection benchmark: https://github.com/WisdomShell/ADG

## What looked useful

Naive real-teacher answer-divergence selection consistently selected longer/harder responses and produced worse held-out overlap than random selection across three medium seeds: mean token-F1 0.2042 for high-divergence, 0.2511 for random, and 0.2723 for low-divergence.

## Boundaries and scale limits

Three seeds, 384 candidate examples and 96 held-out examples per seed, t5-small only, lexical overlap metrics only, public Dolly human responses as the real-teacher proxy. This does not rule out length-controlled divergence, stronger models, semantic metrics, or larger SFT budgets.

## Claim scope

In a small Dolly/t5-small proxy with 64 selected examples per arm, selecting instructions by maximum answer divergence between a pretrained t5-small answer and a human Dolly response underperforms random and low-divergence selection on held-out token-F1 and ROUGE-L.

## Why it stopped

Early direct proxy falsification: the naive high-divergence selector failed against random and low-divergence controls in actual small SFT runs, so the current idea is not paper-ready.

## Recommended next action

Stop this project as a no-paper useful negative; if continuing, run a bounded length-controlled divergence selector that compares high- and low-divergence examples within matched response-length buckets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-controlled real-teacher answer-divergence selection
- Success threshold: High-divergence matched selection improves mean held-out token-F1 or semantic similarity by at least 0.02 over matched random selection in at least two of three seeds without increasing final training loss.
- Stop condition: Stop if matched high-divergence selection is not better than matched random selection on mean held-out metrics across three seeds or if gains disappear after length/category diagnostics.

## Evidence references

- Artifact root: `<local-path>/projects/real-teacher-answer-divergence-instruction-selection-811b5fbbf8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
