# CPU Volunteer Gradient Quantization Proof-of-Concept

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-volunteer-gradient-quantization-proof-of-concept-7b7b9d478a03`
Run ID: `cpu-volunteer-gradient-quantization-proof-of-concept-7b7b9d478a03-20260605T055104205376+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e8e619eb5e79

## What looked useful

The bounded proxy supports testing 4-bit and 8-bit gradient uploads as plausible communication savers for CPU volunteer training. Results below 4 bits were mixed: 2-bit degraded, and the implemented error-feedback residuals hurt rather than helped at 1-2 bits.

## Boundaries and scale limits

Synthetic linear classification only; no real volunteer network, no deep model, no adversarial/Byzantine behavior, no privacy layer, no internet latency, no straggler scheduling, and no 7B-scale gradient or optimizer-state validation.

## Claim scope

In a local NumPy synthetic non-IID federated softmax-regression proxy with 16 clients, 8 active clients per round, 5 seeds, and 120 rounds, stochastic 4-bit and 8-bit client gradient uploads preserved final accuracy within about 1 percentage point of FP32 while reducing uploaded gradient bytes by 87.3% and 74.8% respectively.

## Why it stopped

No-paper useful signal: this run provides moderate synthetic proxy evidence, not direct/full validation of volunteer CPU training or large-model gradient quantization.

## Recommended next action

Run a bounded deepen test on a real small dataset and neural model, with non-IID client partitions and an explicit success threshold of 4-bit upload accuracy/loss within 1 percentage point or comparable validation loss of FP32.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset CPU federated 4-bit gradient upload confirmation
- Success threshold: 4-bit upload final validation accuracy within 1 percentage point of FP32 or validation loss not worse by more than 3%, with at least 80% upload-byte reduction across at least 5 seeds.
- Stop condition: Stop if 4-bit loses more than 3 percentage points or validation loss worsens by more than 10% against FP32 in two independent non-IID settings after learning-rate/clipping tuning.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-volunteer-gradient-quantization-proof-of-concept-7b7b9d478a03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
