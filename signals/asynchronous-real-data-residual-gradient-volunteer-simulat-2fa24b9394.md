# Asynchronous real-data residual-gradient volunteer simulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `asynchronous-real-data-residual-gradient-volunteer-simulat-2fa24b9394`
Run ID: `asynchronous-real-data-residual-gradient-volunteer-simulat-2fa24b9394-20260608T231028277471+0000`

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

- Parent run decision: Distributed Volunteer Training with Quantized Residual Gradients: enoch://control-plane/projects/distributed-volunteer-training-with-quantized-residual-gradients-e5a2ee82a6e9/runs/distributed-volunteer-training-with-quantized-residual-gradients-e5a2ee82a6e9-20260608T203245896230+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

Residual/error-feedback appears useful for asynchronous volunteer training specifically under severe gradient sparsification. The effect was below threshold at 10% top-k, near threshold at 5% top-k, and above threshold at 2% top-k, suggesting the mechanism is compression-regime dependent.

## Boundaries and scale limits

Small MLP and small digit dataset only; volunteer devices, networks, and availability were simulated; no measured volunteer traces, large model, language task, or long-run robustness validation was performed.

## Claim scope

In a small real-data UCI handwritten-digit simulation with 8 heterogeneous non-IID asynchronous volunteer workers, per-worker residual/error-feedback buffers recovered severe 2% top-k gradient compression loss, improving final test accuracy by 2.48 percentage points over compressed async without residuals across 5 seeds and nearly matching uncompressed async accuracy.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not publication-grade evidence; finalizing no-paper rather than scaling claims from a small simulated volunteer run.

## Recommended next action

Run a bounded deepen follow-up using a larger real dataset and replayed or measured volunteer latency/bandwidth traces, with compression and residual ablations, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-replayed residual async gradients on a larger real dataset
- Success threshold: Residual compressed async improves final test accuracy by at least 2.0 percentage points over non-residual compressed async under severe bandwidth constraints and remains within 0.02 final loss of uncompressed async.
- Stop condition: Stop if residual compressed async fails to beat non-residual compressed async by 1.0 percentage point in accuracy or fails to reduce loss in the primary severe-compression setting across at least 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/asynchronous-real-data-residual-gradient-volunteer-simulat-2fa24b9394`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
