# Equal-cost adaptive verifier test for sparse activation replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `equal-cost-adaptive-verifier-test-for-sparse-activation-re-abd908e4c4`
Run ID: `equal-cost-adaptive-verifier-test-for-sparse-activation-re-abd908e4c4-20260517T180804059833+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d019a3fa381

## What looked useful

Across five medium replicated seeds and 12 budget/noise conditions, adaptive verification had mean TPR lift +0.0588 and mean AUROC lift +0.0202 versus the stronger non-adaptive baseline; TPR wins were 49/60 seed-conditions and AUROC wins were 52/60.

## Boundaries and scale limits

Synthetic sparse windows only; no real transformer activations, no adversarial replay construction, no production verifier overhead, and no large-model or multi-layer validation.

## Claim scope

In a controlled sparse binary activation replay simulator with equal suspect-trace probe budgets, a two-stage adaptive verifier improves replay detection over uniform probing and a strong fixed archive-active verifier, especially at 64-128 probes.

## Why it stopped

Controlled Tier-1 direct synthetic test supports the mechanism but is not paper-positive evidence because the activation distribution and replay attack are simulated.

## Recommended next action

Run the same equal-budget verifier comparison on real small-transformer activation masks with archived-window replay and calibrated 5% FPR thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-cost adaptive verifier on real small-transformer activation replay
- Success threshold: Adaptive verifier beats the stronger non-adaptive baseline by at least +0.03 mean TPR at calibrated 5% FPR and non-negative AUROC lift across the tested real-activation budget/noise grid.
- Stop condition: Stop as unsupported if adaptive mean TPR lift is <= 0 or AUROC lift is negative versus the fixed active-coordinate baseline across the real-activation grid.

## Evidence references

- Artifact root: `<local-path>/projects/equal-cost-adaptive-verifier-test-for-sparse-activation-re-abd908e4c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
