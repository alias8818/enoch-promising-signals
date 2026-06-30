# Local Cascade Router: Difficulty-Based Model Selection on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-difficulty-based-model-selection-on-cpu-396db1bcc4f8`
Run ID: `local-cascade-router-difficulty-based-model-selection-on-cpu-396db1bcc4f8-20260611T134758940137+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4e7aaefaf4c

## What looked useful

Cheap-model confidence strongly ranked cheap-model errors (test AUC 0.91-0.99). On digits, low-confidence routing beat random routing by 1.28-2.06 accuracy points at matched fallback rates and achieved 1.90x-7.90x speedups versus all-strong. On datasets where the fallback was not more accurate or not slower, the cascade had little or negative practical value.

## Boundaries and scale limits

Classical CPU proxy only; no local LLM inference, no large datasets, no production serving stack, no domain-shift or calibration-persistence validation.

## Claim scope

On three small built-in scikit-learn CPU classification datasets, a cheap-model confidence router improved accuracy/cost tradeoffs when the fallback model was both more accurate and more expensive, most clearly on digits.

## Why it stopped

Proxy-scale useful signal only: the mechanism worked in the expected cost/asymmetry regime but the result is mixed across datasets and is not a full validation of local model cascade routing.

## Recommended next action

Run a bounded direct-evidence follow-up on local language-model or text-classification inference with all-small, all-large, random-routing, and confidence-routing controls; stop if confidence routing fails to beat random at matched fallback-call rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Text/LLM Cascade Router Validation
- Success threshold: Confidence routing beats random routing by at least 1 task-metric point at the same fallback-call rate on two held-out splits or domains, while achieving at least 1.5x latency speedup versus all-strong inference.
- Stop condition: Stop as negative if the fallback model is not materially better than the cheap model, if confidence-error AUC is below 0.65, or if confidence routing does not beat random routing at matched fallback-call rates.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-difficulty-based-model-selection-on-cpu-396db1bcc4f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
