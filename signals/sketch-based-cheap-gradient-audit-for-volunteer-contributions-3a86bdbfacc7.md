# Sketch-based cheap gradient audit for volunteer contributions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sketch-based-cheap-gradient-audit-for-volunteer-contributions-3a86bdbfacc7`
Run ID: `sketch-based-cheap-gradient-audit-for-volunteer-contributions-3a86bdbfacc7-20260628T141046964818+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6807a94e26b3

## What looked useful

Cheap random sketches are a plausible gradient-audit primitive: best cheap JL sketches reached mean AUC 1.0000 for sign-flip and scaled-flip faults, 0.9999 for high-heterogeneity sign flips, and 0.9688 for subtle directional bias while using 32x-128x compression. The subtle-bias case still had lower precision@bad-count than full gradients, and coordinate sampling was competitive.

## Boundaries and scale limits

No real volunteer traces, no federated training-loop validation, no secure aggregation constraints, no adaptive attackers, and no downstream model-quality measurement. CPU-only run completed locally in 41.84 seconds with 40 rounds and 256 clients per round.

## Claim scope

Synthetic 2048-dimensional volunteer-gradient submissions with 10-20% controlled faulty contributors; robust distance-to-consensus scoring over random sign sketches of 16-64 dimensions preserved anomaly-ranking AUC within 0.05 of full-gradient scoring across four simulated fault scenarios.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation of volunteer contribution auditing.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay the same sketch audit on real or realistic federated-learning gradient traces with non-IID benign clients and downstream training-quality measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based sketch audit for non-IID volunteer gradients
- Success threshold: A 64-256 dimensional sketch achieves AUC >= 0.90, false positive rate <= 5% on benign non-IID clients, and downstream validation accuracy within 1 percentage point of full-gradient audit filtering while reducing audited representation size by at least 8x.
- Stop condition: Stop if sketches fall below AUC 0.80, exceed 10% benign false positive rate, or degrade downstream validation accuracy by more than 3 percentage points in two independent trace settings.

## Evidence references

- Artifact root: `<local-path>/projects/sketch-based-cheap-gradient-audit-for-volunteer-contributions-3a86bdbfacc7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
