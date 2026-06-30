# Honest Local-First Toy for Volunteer Gradient Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `honest-local-first-toy-for-volunteer-gradient-compression-877c5a538ba2`
Run ID: `honest-local-first-toy-for-volunteer-gradient-compression-877c5a538ba2-20260620T212407093509+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

Hard benchmark over 5 seeds: dense mean accuracy 0.901367 with 50,903,040 bytes; top-k 1% with error feedback mean accuracy 0.902344 with 1,013,760 bytes (98.0% fewer bytes); sign mean accuracy 0.905273 with 1,599,360 bytes (96.9% fewer bytes); random-k 1% mean accuracy 0.550342 at the same 1,013,760-byte budget.

## Boundaries and scale limits

Synthetic data, tiny MLP, synchronous aggregation, simulated churn, no real volunteer devices or network traces, no privacy/adversarial validation, and no large-model or real-dataset training.

## Claim scope

On a synthetic local-first federated toy benchmark with non-IID clients and simulated 25% volunteer participation, structured gradient compression can match dense-gradient accuracy while cutting transmitted bytes by about 97-98%; random-k at the same byte budget fails on the harder task.

## Why it stopped

No-paper closure: evidence is a useful toy/proxy mechanism result, not direct real-world or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on one real federated or federated-like dataset with replayed client availability/network traces and matched-byte dense/top-k-error-feedback/sign/random-k controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Data Local-First Gradient Compression With Matched Byte Budgets
- Success threshold: Top-k with error feedback reaches within 1 percentage point of dense final accuracy while reducing bytes by at least 90%, and random-k at the same byte budget is at least 5 percentage points worse than dense or top-k error feedback.
- Stop condition: Stop as negative if top-k error feedback is more than 3 percentage points below dense on two independent seeds or if byte accounting shows less than 80% reduction after including indices/metadata.

## Evidence references

- Artifact root: `<local-path>/projects/honest-local-first-toy-for-volunteer-gradient-compression-877c5a538ba2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
