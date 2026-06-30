# Forgetting-bound curriculum for tiny model data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `forgetting-bound-curriculum-for-tiny-model-data-selection-1e14f63106a4`
Run ID: `forgetting-bound-curriculum-for-tiny-model-data-selection-1e14f63106a4-20260605T123502841099+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2d4671d07106

## What looked useful

Forgetting-from-best alone is an insufficient selection signal when rare slices are underlearned rather than forgotten; the bound rarely triggers and preserves biased exposure. Future variants should combine forgetting bounds with explicit coverage or regret-to-target terms.

## Boundaries and scale limits

Synthetic data, tiny MLP rather than transformer, explicit domain feature, 8 seeds, 1200 updates, CPU-only local run. This does not validate natural-language pretraining, GPT-2-small-class models, or large-corpus data selection.

## Claim scope

A NumPy tiny-MLP next-token proxy with two synthetic regimes, easy/hard examples, 8 seeds, and 1200 online updates per policy shows that a simple validation-regime forgetting-bound selector can mildly improve mean loss versus an 80/20 skewed sampler but does not reduce worst forgetting versus that skewed control and is worse than balanced sampling.

## Why it stopped

Proxy early falsification rather than full validation: the tested forgetting-bound-only selector failed the direct control requirement because balanced sampling dominated it and it did not reduce worst forgetting versus skewed random sampling.

## Recommended next action

Stop this simple forgetting-bound-only variant as no-paper evidence; the next bounded test should add an explicit rare-slice coverage/regret term and require beating balanced sampling on mean loss, rare-domain loss, and worst forgetting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-aware forgetting-bound curriculum for tiny-model data selection
- Success threshold: Combined coverage-aware forgetting-bound policy beats balanced random on mean validation loss by at least 0.01 nats, is no worse than balanced by 0.02 nats on rare-domain loss, and has worst forgetting below 0.01 nats in at least 12 of 16 seeds.
- Stop condition: Stop if the combined policy loses to balanced random on rare-domain loss by more than 0.05 nats on average or has worst forgetting above 0.02 nats in more than 4 of 16 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/forgetting-bound-curriculum-for-tiny-model-data-selection-1e14f63106a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
