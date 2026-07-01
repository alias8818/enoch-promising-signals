# Exact-anchor compressed context windows for gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-compressed-context-windows-for-gb10-6c58d8692ebc`
Run ID: `exact-anchor-compressed-context-windows-for-gb10-6c58d8692ebc-20260611T152837834844+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/17d687b72f1b

## What looked useful

Exact-anchor compression consistently improved point-retrieval accuracy over lossy prefix/reservoir baselines at matched approximate token budgets, with +3.6 to +14.5 percentage-point absolute gains and about 22% relative gain, but it missed the predeclared +20 percentage-point useful-signal threshold.

## Boundaries and scale limits

Synthetic facts only; no natural documents, no LLM summarization, no model-in-the-loop answering, no training, and no long-context GPU workload.

## Claim scope

Synthetic point-retrieval benchmark with 256 compressed windows, 2048 exact anchor facts, four token budgets, and seven deterministic trials per budget.

## Why it stopped

Proxy-only synthetic result supports a modest mechanism but does not meet the predeclared absolute-gain threshold and is not a full validation.

## Recommended next action

Stop this run as no-paper proxy evidence; a bounded follow-up should test exact-anchor windows with real LLM-generated summaries on natural long documents.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-document LLM summary control for exact-anchor windows
- Success threshold: Exact-anchor windows beat the best summary control by at least 20 absolute percentage points at two matched sequence-item budgets without materially increasing context tokens.
- Stop condition: Stop as negative if exact-anchor windows improve by less than 5 absolute percentage points at both budgets or if gains disappear after removing synthetic anchor formatting.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-context-windows-for-gb10-6c58d8692ebc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
