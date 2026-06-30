# Predictive Operator-Model Updates from Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `predictive-operator-model-updates-from-agent-memory-3cb5b32d630b`
Run ID: `predictive-operator-model-updates-from-agent-memory-3cb5b32d630b-20260620T115522237902+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Layered doctrine memory reached 1.000 mean task accuracy versus 0.708 for the best baseline, an absolute lift of 0.292, by retaining explicit latest operator updates per dimension and ignoring noisy transcript content.

## Boundaries and scale limits

Synthetic hand-authored tasks only; deterministic symbolic strategies only; no real/private operator traces, LLM extraction, live agent runs, or downstream task-quality measurement.

## Claim scope

On a 12-task synthetic repeated-agent replay suite with noisy and obsolete memory events, a layered latest-update-wins operator-memory representation predicted current operator-model state more accurately than no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

No paper-ready validation: this run produced a useful synthetic mechanism signal, not direct real-operator or LLM-agent evidence.

## Recommended next action

Run a bounded direct follow-up using held-out naturalistic replay traces and LLM-based extraction/prediction to test whether the synthetic mechanism survives realistic ambiguity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic LLM Operator-Memory Update Prediction
- Success threshold: Layered memory improves mean operator-model prediction accuracy by at least 0.10 absolute over the best baseline and reduces stale-preference failures without increasing privacy or evidence-format errors.
- Stop condition: Stop as negative if layered memory fails to beat the best baseline by 0.05 absolute on held-out naturalistic traces or if gains disappear in downstream response-quality checks.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-model-updates-from-agent-memory-3cb5b32d630b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
