# LoRA Adapter Fine-tuning for CPU Memory-constrained Domain Adaptation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9`
Run ID: `lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9-20260610T204248272481+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

Across three seeds, LoRA reduced target validation loss from 3.4493 frozen-baseline mean to 2.8155 and improved target accuracy from 0.4726 to 0.5149, with an estimated 20.6x Adam-style trainable-state memory reduction versus dense fine-tuning.

## Boundaries and scale limits

Small synthetic Markov-domain benchmark only; not a real pretrained transformer, not a real domain corpus, no enforced CPU memory cgroup, no dense hyperparameter sweep, and no publication-grade robustness study.

## Claim scope

Synthetic NumPy one-step token-prediction domain shift: rank-4 LoRA adapters on a frozen source-trained model improved target validation loss and accuracy while training 4.85% as many parameters as dense fine-tuning.

## Why it stopped

This run produced a useful bounded proxy signal, but the evidence is synthetic and not sufficient for a paper-positive conclusion or broad LLM memory-constrained adaptation claim.

## Recommended next action

Run a bounded deepen follow-up on a small real pretrained transformer and real domain corpus under an explicit CPU memory cap, comparing tuned dense, LoRA, and frozen baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU-capped LoRA adaptation on a small real transformer corpus
- Success threshold: LoRA achieves at least 80% of dense target-loss improvement over frozen baseline while reducing measured optimizer-state memory by at least 5x and staying within the CPU memory cap.
- Stop condition: Stop if LoRA fails to improve target validation loss over the frozen baseline in two consecutive seeds, or if framework overhead prevents all methods from running within the same CPU memory cap.

## Evidence references

- Artifact root: `<local-path>/projects/lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
