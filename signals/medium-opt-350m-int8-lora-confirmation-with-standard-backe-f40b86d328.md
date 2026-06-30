# Medium OPT-350M INT8 LoRA confirmation with standard backend and downstream task

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-opt-350m-int8-lora-confirmation-with-standard-backe-f40b86d328`
Run ID: `medium-opt-350m-int8-lora-confirmation-with-standard-backe-f40b86d328-20260614T131430656278+0000`

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

- Parent run decision: QLoRA-mini: INT8 Quantization with Minimal Rank Adaptation for 350M Params: enoch://control-plane/projects/qlora-mini-int8-quantization-with-minimal-rank-adaptation-for-350m-params-180630d6c2d9/runs/qlora-mini-int8-quantization-with-minimal-rank-adaptation-for-350m-params-180630d6c2d9-20260614T125553625893+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9c36983d595

## What looked useful

Standard-backend OPT-350M INT8 LoRA is runnable on GB10 and gives a small downstream SST-2 signal under a bounded test. Across seeds 17, 29, and 43, LoRA after-training accuracy averaged 0.5807 versus 0.5326 for the dense FP16 head-only control, with paired accuracy differences of +0.1172, +0.0000, and +0.0273. LoRA validation loss was lower than the dense head-only control in all three seeds. The pure INT8 head-only control failed in all seeds with the expected Transformers error requiring adapters for quantized fine-tuning.

## Boundaries and scale limits

Only 512 SST-2 train examples, 256 validation examples, 60 optimizer steps, three seeds, one model family, one downstream classification task, and no convergence/robustness/hyperparameter sweep. Pure INT8 head-only fine-tuning could not be used as a control because the standard backend rejects fine-tuning purely quantized models without adapters.

## Claim scope

Tier 1 direct local confirmation that facebook/opt-350m can be loaded with the standard Transformers bitsandbytes INT8 backend, adapted with PEFT LoRA, and fine-tuned on GLUE SST-2 for 60 steps; INT8 LoRA improved mean validation accuracy from 0.4935 to 0.5807 over three seeds and beat or tied a dense FP16 frozen-head control after training.

## Why it stopped

No-paper useful signal: the direct Tier 1 downstream test supports standard-backend feasibility and a small LoRA effect, but the run is too short and variable for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up on full SST-2 or a larger fixed subset for enough steps to test whether INT8 LoRA exceeds the dense frozen-head control by at least 3 accuracy points mean over 3 to 5 seeds while preserving lower validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer OPT-350M INT8 LoRA SST-2 confirmation against dense frozen-head control
- Success threshold: INT8 LoRA mean validation accuracy is at least 0.03 higher than dense FP16 frozen-head control over 3 to 5 seeds, with no seed showing catastrophic regression and mean validation loss lower than control.
- Stop condition: Stop as negative/no-paper if INT8 LoRA fails to exceed the control by 0.03 mean accuracy, if validation loss is not lower on average, or if standard-backend quantized LoRA becomes unstable under the longer run.

## Evidence references

- Artifact root: `<local-path>/projects/medium-opt-350m-int8-lora-confirmation-with-standard-backe-f40b86d328`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
