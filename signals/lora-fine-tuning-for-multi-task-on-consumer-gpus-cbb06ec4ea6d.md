# LoRA Fine-Tuning for Multi-Task on Consumer GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-fine-tuning-for-multi-task-on-consumer-gpus-cbb06ec4ea6d`
Run ID: `lora-fine-tuning-for-multi-task-on-consumer-gpus-cbb06ec4ea6d-20260628T144421950203+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/979f67b8f044

## What looked useful

LoRA was locally feasible and resource-efficient on consumer GPU hardware, improving aggregate toy accuracy from 0.511 to 0.711 while using 498.8 MB peak CUDA allocation versus 2483.0 MB for the stable full fine-tune control. Numeric parity and comparison accuracy remained modest, so this is not a broad multi-task success claim.

## Boundaries and scale limits

Synthetic deterministic tasks only; GPT-2 small only; one main seed; short 120-step runs; no real benchmark, no 7B-class model, no hyperparameter sweep, and no saved-adapter persistence test.

## Claim scope

On a GB10 host, a shared PEFT LoRA adapter for GPT-2 small adapted a synthetic three-task instruction probe with 0.648% trainable parameters, lower observed CUDA memory, and higher short-run throughput than a stable full fine-tune control; task quality remained weak for numeric tasks.

## Why it stopped

Closed as no-paper useful signal: the evidence is a small synthetic local probe that supports the resource mechanism but does not validate robust multi-task LoRA performance.

## Recommended next action

Run a bounded deepen experiment on real small multi-task benchmarks with saved LoRA adapters, 3 seeds, and matched hyperparameter budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Benchmark GPT-2 LoRA Multi-Task Adapter Probe
- Success threshold: Mean LoRA accuracy within 2 percentage points of full fine-tuning or better on at least two of three tasks, with at least 4x lower peak CUDA allocation and no adapter reload regression greater than 0.5 percentage points.
- Stop condition: Stop if LoRA underperforms the tuned full control by more than 5 percentage points mean accuracy or fails to preserve a 4x peak CUDA memory advantage after one bounded LR/rank sweep.

## Evidence references

- Artifact root: `<local-path>/projects/lora-fine-tuning-for-multi-task-on-consumer-gpus-cbb06ec4ea6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
