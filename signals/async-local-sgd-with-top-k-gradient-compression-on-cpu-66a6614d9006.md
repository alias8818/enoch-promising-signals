# Async Local SGD with Top-K Gradient Compression on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-local-sgd-with-top-k-gradient-compression-on-cpu-66a6614d9006`
Run ID: `async-local-sgd-with-top-k-gradient-compression-on-cpu-66a6614d9006-20260529T204913431563+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/03809f7c3eca

## What looked useful

Top-k compression itself appears viable for synchronous local SGD in this bounded CPU benchmark, but the async variant is sensitive: 5% async top-k cut payload 13.4x yet lagged async dense by 3.0 accuracy points at 1200 events and 1.2 points at 3000 events, with worse validation loss. A follow-up should focus on async-specific correction rather than generic top-k feasibility.

## Boundaries and scale limits

No real networking, no true concurrent multiprocessing, no measured inter-worker staleness distribution, no large neural model, no multi-host CPU cluster, and limited hyperparameter sweep. Wall-clock results are single-process CPU simulator timings, not distributed speedup evidence.

## Claim scope

Bounded CPU NumPy simulation on UCI Wine Quality Red binary classification with 1024 random nonlinear features, 4 mildly non-IID workers, local logistic-regression SGD, and serialized payload-byte accounting. Synchronous local SGD tolerated 5-10% top-k error-feedback compression with negligible accuracy loss and 6.7x-13.4x lower payload; naive async top-k reduced payload similarly but trailed async dense in validation accuracy/loss under tested settings.

## Why it stopped

No-paper closure: bounded simulator evidence is mixed and does not support the named async local-SGD top-k hypothesis strongly enough for publication or scale-up claims.

## Recommended next action

Run a bounded multiprocessing CPU follow-up that measures real staleness and tests staleness-aware or periodic-dense-correction async top-k against async dense.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Staleness-aware async top-k local SGD on real CPU worker processes
- Success threshold: Across at least 5 seeds, corrected async top-k validation accuracy is within 1 percentage point of async dense, validation loss is not worse by more than 0.02, serialized payload is reduced by at least 5x, and bandwidth-limited wall-clock is not slower than async dense.
- Stop condition: Stop if corrected async top-k still trails async dense by more than 2 accuracy points or more than 0.04 validation loss after a 5-seed bounded run, or if payload savings fall below 3x.

## Evidence references

- Artifact root: `<local-path>/projects/async-local-sgd-with-top-k-gradient-compression-on-cpu-66a6614d9006`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
