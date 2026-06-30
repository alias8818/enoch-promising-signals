# Operator-Model Updates from Trace Distillation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-model-updates-from-trace-distillation-d4f4bb339643`
Run ID: `operator-model-updates-from-trace-distillation-d4f4bb339643-20260613T055519660197+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/07558e2c34a4

## What looked useful

Layered operator-model updates reached 192/192 accuracy versus 157/192 for flat distilled retrieval, 122/192 for transcript-window lookup, and 70/192 for no-memory under 25.8% observed metadata noise.

## Boundaries and scale limits

Synthetic structured traces only; 128 trace events and 192 query tasks; no real operator data, no language-model fine-tuning, no downstream task execution, no long-horizon persistence validation, and no GPT-2-small-class baseline.

## Claim scope

On a deterministic synthetic replay benchmark with explicit operator preference updates, a layered operator-model state representation answered current-preference queries more accurately than no-memory, transcript-window, and flat distilled-retrieval controls.

## Why it stopped

Synthetic proxy evidence supports the state-update mechanism but is not direct/full validation of operator-model updates from trace distillation.

## Recommended next action

Stop this run as no-paper proxy evidence; run a bounded medium replay benchmark with human-authored traces and downstream task outcomes before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored replay benchmark for distilled operator-model updates
- Success threshold: Layered operator-model state improves downstream adherence by >=15 percentage points over both transcript-window and flat-retrieval controls with bootstrap 95% confidence interval excluding zero.
- Stop condition: Stop if layered state fails to beat either main control by at least 5 percentage points on the first 100 audited tasks or if human-authored traces cannot be produced without private/sensitive data leakage.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-updates-from-trace-distillation-d4f4bb339643`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
