# Activation-Sparsity Data Selection for CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-sparsity-data-selection-for-cpu-pretraining-110d9af8b9dc`
Run ID: `activation-sparsity-data-selection-for-cpu-pretraining-110d9af8b9dc-20260607T060429497012+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4d064f2d90ca

## What looked useful

Naive low activation-density data selection did not reliably reduce final activation density or preserve validation loss. Across four seeds, sparse_low_density averaged +0.0085 nats loss versus random and only -0.00067 absolute activation-density change, with one large quality regression. The probe ranking signal was narrow and seed-sensitive, suggesting corpus quality/position confounding and weak persistence after training.

## Boundaries and scale limits

Does not test transformer pretraining, tokenizer-level corpora, production sparse CPU kernels, large datasets, or long training. Activation density is an estimated sparse FFN compute proxy, not measured sparse-kernel wall-clock speedup.

## Claim scope

Bounded CPU proxy on Tiny Shakespeare using a NumPy char-level ReLU MLP: activation-density-ranked chunk selection was compared with random and dense-selected subsets under equal selected-token budgets across four seeds.

## Why it stopped

No-paper useful signal: this local proxy is an early mixed/negative result for naive activation-sparsity data selection, not a full validation or full falsification of large-scale CPU pretraining.

## Recommended next action

Run a bounded stratified follow-up that matches chunks by probe loss, corpus position, and domain before considering any transformer or sparse-kernel scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stratified Activation-Sparsity Selection Controls for CPU Pretraining
- Success threshold: Mean final activation-density reduction >= 0.03 absolute versus matched random with validation-loss delta no worse than +0.02 nats and no seed showing >0.05 nats regression.
- Stop condition: Stop if matched low-density selection again has <0.01 absolute mean activation-density reduction or any repeated large validation-loss regression >0.05 nats.

## Evidence references

- Artifact root: `<local-path>/projects/activation-sparsity-data-selection-for-cpu-pretraining-110d9af8b9dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
