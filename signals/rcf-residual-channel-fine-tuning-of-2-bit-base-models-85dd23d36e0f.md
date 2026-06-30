# RCF: Residual Channel Fine-tuning of 2-bit Base Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rcf-residual-channel-fine-tuning-of-2-bit-base-models-85dd23d36e0f`
Run ID: `rcf-residual-channel-fine-tuning-of-2-bit-base-models-85dd23d36e0f-20260621T193452128500+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/934896233762

## What looked useful

RCF improved target accuracy over the frozen 2-bit base by a mean +0.2048 across five seeds with 666 trainable parameters, outperforming bias/scale tuning. Rank-matched LoRA-style adapters reached higher target accuracy by a mean +0.0364 but used 3720 trainable parameters.

## Boundaries and scale limits

Evidence is limited to a toy MLP, synthetic teacher-generated classification data, five seeds, and a simple per-channel symmetric 2-bit quantizer. No transformer, language modeling corpus, real pretrained model, or production low-bit kernel was tested.

## Claim scope

On a controlled synthetic MLP task, a small RCF residual channel can recover substantial target accuracy from a frozen 2-bit quantized base, but it did not beat the LoRA-style control in this run.

## Why it stopped

Closed as no-paper useful signal: the local synthetic evidence supports the RCF mechanism but is not direct transformer evidence and does not outperform the strongest adapter control.

## Recommended next action

Run a bounded GPT-2-small-class language-modeling follow-up with strict trainable-parameter matching between RCF and LoRA before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched RCF vs LoRA on a small frozen 2-bit transformer
- Success threshold: RCF should match or beat LoRA validation loss within 1 percent at the same trainable parameter budget while improving frozen 2-bit validation loss by at least 10 percent relative.
- Stop condition: Stop if RCF fails to improve frozen 2-bit validation loss by 5 percent relative in a smoke run, or if parameter-matched LoRA beats RCF by more than 3 percent validation loss across three short seeds.

## Evidence references

- Artifact root: `<local-path>/projects/rcf-residual-channel-fine-tuning-of-2-bit-base-models-85dd23d36e0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
