# Real-corpus tiny transformer gradient coreset subset selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-transformer-gradient-coreset-subset-selec-9f90b0020d`
Run ID: `real-corpus-tiny-transformer-gradient-coreset-subset-selec-9f90b0020d-20260523T070906428737+0000`

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

- Parent run decision: Gradient coreset subset selection for tiny pretraining: enoch://control-plane/projects/gradient-coreset-subset-selection-for-tiny-pretraining-b095dc8f55de/runs/gradient-coreset-subset-selection-for-tiny-pretraining-b095dc8f55de-20260523T044554618644+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/796b6c3ba0ff

## What looked useful

OMP gradient coreset selection matched the full gradient sketch mean very closely but failed the 1% validation-loss improvement threshold; a gradient-diversity selector over the same sketches won all 5 confirmation seeds but only improved mean validation loss by 0.375%, below threshold.

## Boundaries and scale limits

Small single-corpus Tier 1 test only: Tiny Shakespeare, char-level tokenizer, tiny transformer, compact final-layer gradient sketches, up to 2048 candidate blocks, 512 selected blocks, 5 seeds, 500 training steps.

## Claim scope

On Tiny Shakespeare with a char-level tiny transformer, 25% subset selection using compact final-layer gradient mean matching did not achieve a meaningful validation-loss improvement over random under matched training budgets.

## Why it stopped

Direct Tier 1 real-corpus tests did not support the stated practical threshold for OMP gradient coreset subset selection; this is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Run one bounded deepen/branch test of gradient-diversity selection on two additional real corpora or tokenizer/model settings; stop if it remains below 1% mean validation-loss improvement versus random.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Real-corpus tiny transformer gradient-diversity subset selection
- Success threshold: Gradient-diversity selection improves mean final validation loss by at least 1% versus random and wins at least 4 of 5 seeds in each tested setting.
- Stop condition: Stop if the mean improvement remains below 1% in the first bounded additional real-corpus setting or if wins fall below 4 of 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-transformer-gradient-coreset-subset-selec-9f90b0020d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
