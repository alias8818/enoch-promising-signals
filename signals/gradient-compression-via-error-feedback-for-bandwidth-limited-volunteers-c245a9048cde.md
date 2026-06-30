# Gradient Compression via Error Feedback for Bandwidth-Limited Volunteers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-compression-via-error-feedback-for-bandwidth-limited-volunteers-c245a9048cde`
Run ID: `gradient-compression-via-error-feedback-for-bandwidth-limited-volunteers-c245a9048cde-20260605T165418495902+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e2c858ab2106

## What looked useful

At LR=0.10 over 5 seeds and 700 rounds, error feedback improved top-k 1.0% accuracy by 0.0062 and loss by 0.3395 at 46.9x lower uplink bytes versus dense; for top-k 0.5%, it improved accuracy by 0.0135 and loss by 0.1684 at 86.0x lower uplink bytes. At LR=0.55, sparse top-k error feedback reduced loss but hurt accuracy, so the mechanism is step-size sensitive.

## Boundaries and scale limits

Synthetic linear-classifier task only; no real volunteer networking, churn, stragglers, stale gradients, secure aggregation overhead, public dataset, or large neural-network training was tested.

## Claim scope

In a local synchronous 16-client non-IID synthetic classification simulation, per-client error feedback can improve final loss and modestly improve accuracy for severe top-k/sign gradient compression at the same uplink byte budget when the learning rate is tuned for the compressed optimizer.

## Why it stopped

No-paper closure: the current evidence is a bounded synthetic mechanism signal with mixed LR sensitivity, not direct volunteer-system or publication-grade validation.

## Recommended next action

Run a bounded real-dataset deepen test with a small neural network, volunteer-like client dropout/stragglers, and an LR/compression grid before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback gradient compression under volunteer churn on a small real dataset
- Success threshold: Compressed-EF must recover at least 95% of dense final accuracy and beat compressed-no-EF by at least 1 percentage point or reduce rounds-to-threshold by at least 20% at the same uplink byte budget.
- Stop condition: Stop if compressed-EF fails to beat compressed-no-EF on both accuracy and rounds-to-threshold across the tuned grid, or if its stability requires a learning rate that erases practical time-to-target gains.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-compression-via-error-feedback-for-bandwidth-limited-volunteers-c245a9048cde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
