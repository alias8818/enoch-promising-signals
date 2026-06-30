# Natural-language tool-task operator memory vs retrieval under equal budget

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `natural-language-tool-task-operator-memory-vs-retrieval-un-181478056c`
Run ID: `natural-language-tool-task-operator-memory-vs-retrieval-un-181478056c-20260613T035341973738+0000`

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

- Parent run decision: Operator-model agent memory vs retrieval-only: enoch://control-plane/projects/operator-model-agent-memory-vs-retrieval-only-846e10dba6d6/runs/operator-model-agent-memory-vs-retrieval-only-846e10dba6d6-20260613T033322916669+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfdae30b842d

## What looked useful

Retrieval did not beat memory under equal budget. Main k=3 run: memory 87.5%, retrieval 68.75%, delta -18.75 pp, bootstrap 95% CI [-31.25, -6.25]. k=5 sensitivity: memory 87.5%, retrieval 75.0%, delta -12.5 pp, CI [-25.0, 0.0]. Retrieval recall was high but imperfect, and many retrieval errors occurred even when the gold operator was retrieved.

## Boundaries and scale limits

Small synthetic Tier 1 test only: 48 tasks, one final model, lexical retrieval, fixed-choice operator scoring, no multi-step execution, no real production task traces, and no large operator catalog where memory context exceeds budget.

## Claim scope

In a 12-operator synthetic natural-language tool-task selection benchmark with Qwen2.5-1.5B-Instruct and equal prompt-character budget, prompt memory outperformed lexical retrieval at k=3 and k=5.

## Why it stopped

Tier 1 direct controlled evidence did not support retrieval outperforming prompt memory under equal budget; this is a no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded medium confirmation with a larger operator catalog, embedding retrieval, and at least two instruction models before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium operator-catalog memory-vs-retrieval confirmation with embedding retrieval
- Success threshold: Embedding retrieval improves exact-match operator accuracy by at least 8 percentage points over the best equal-budget memory condition, with bootstrap 95% CI lower bound above 0 on the paired delta.
- Stop condition: Stop as unsupported if embedding retrieval is not above memory by at least 3 percentage points or if gains disappear when gold operator recall is controlled.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-tool-task-operator-memory-vs-retrieval-un-181478056c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
