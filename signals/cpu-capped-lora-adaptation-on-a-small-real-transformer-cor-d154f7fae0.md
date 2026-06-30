# CPU-capped LoRA adaptation on a small real transformer corpus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-capped-lora-adaptation-on-a-small-real-transformer-cor-d154f7fae0`
Run ID: `cpu-capped-lora-adaptation-on-a-small-real-transformer-cor-d154f7fae0-20260610T210347545311+0000`

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

- Parent run decision: LoRA Adapter Fine-tuning for CPU Memory-constrained Domain Adaptation: enoch://control-plane/projects/lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9/runs/lora-adapter-fine-tuning-for-cpu-memory-constrained-domain-adaptation-559390b33bb9-20260610T204248272481+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

CPU-capped LoRA produced consistent small-run adaptation: mean validation-loss improvement 0.3106 nats over frozen GPT-2, minimum 0.2789 nats across three seeds, with 811,008 trainable parameters, about 0.6475% of total parameters, about 97 seconds per run, and under 1.83 GiB RSS.

## Boundaries and scale limits

Only GPT-2-small and Wikitext-2 were tested; validation covered 128 short blocks per seed; no dense fine-tuning, full fine-tuning, longer convergence, larger corpus, downstream task, or larger-model controls were run.

## Claim scope

In a bounded CPU-worker Tier 1 test, GPT-2-small LoRA rank-8 adaptation on Wikitext-2 with 4 CPU threads, 40 steps, 256 train blocks, and 128 validation blocks improved held-out validation loss over the frozen GPT-2 baseline in 3/3 seeds.

## Why it stopped

Tier 1 direct threshold was met, but the evidence is a narrow useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test adding a same-budget dense/full fine-tuning control and a larger validation window to check whether LoRA's CPU-capped gain remains distinct from ordinary small-budget adaptation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU-capped LoRA versus dense controls on GPT-2 Wikitext-2
- Success threshold: LoRA achieves at least 80% of the full fine-tune validation-loss improvement over frozen GPT-2 while training under 1% of parameters and all LoRA seeds improve validation loss by at least 0.05 nats on the larger validation window.
- Stop condition: Stop if LoRA fails to improve over frozen GPT-2 by 0.05 nats in two or more seeds, or if same-budget full fine-tuning clearly dominates LoRA without a parameter-efficiency tradeoff worth reporting.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-capped-lora-adaptation-on-a-small-real-transformer-cor-d154f7fae0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
