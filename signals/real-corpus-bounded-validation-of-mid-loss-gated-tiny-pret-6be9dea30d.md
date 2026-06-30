# Real-corpus bounded validation of mid-loss gated tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-corpus-bounded-validation-of-mid-loss-gated-tiny-pret-6be9dea30d`
Run ID: `real-corpus-bounded-validation-of-mid-loss-gated-tiny-pret-6be9dea30d-20260612T234529310614+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Loss-gated data selection for tiny local pretraining: enoch://control-plane/projects/loss-gated-data-selection-for-tiny-local-pretraining-b1c339bf73f2/runs/loss-gated-data-selection-for-tiny-local-pretraining-b1c339bf73f2-20260612T231907373846+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5ed6553a91ed

## What looked useful

Strict q25-q75 mid-loss gating used 37.25% of updates but regressed validation loss by 8.30%; broader q10-q75 gating used 56.0% of updates but regressed validation loss by 5.55%. Both missed the <=2% validation-loss threshold despite meeting the <=70% update target.

## Boundaries and scale limits

Character-level tokenization, tiny 4-layer/128-hidden Transformer, WikiText-2 only, 600 steps, two seeds, and two rolling-quantile gate bands. This does not rule out token-level GPT-2-small-class, larger corpus, longer horizon, or differently scheduled gates.

## Claim scope

On WikiText-2 character-level tiny Transformer pretraining for 600 sampled-batch steps and two seeds, tested mid-loss gates reduced optimizer updates but did not preserve validation loss within the predeclared 2% tolerance.

## Why it stopped

Controlled small direct test failed the success threshold: both mid-loss gates met update reduction but exceeded the allowed validation-loss regression.

## Recommended next action

Stop this follow-up as an early direct real-corpus falsification of the bounded threshold; only revisit with a predeclared token-level GPT-2-small-class schedule and longer multi-seed run.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-bounded-validation-of-mid-loss-gated-tiny-pret-6be9dea30d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
