# Home Fine-Tuning 2-bit Base + Full-Precision LoRA Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-fine-tuning-2-bit-base-full-precision-lora-residual-channel-2ed5bdc6e453`
Run ID: `home-fine-tuning-2-bit-base-full-precision-lora-residual-channel-2ed5bdc6e453-20260611T041859352464+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/513f70c2ab91

## What looked useful

Rank-8 calibrated run over three seeds reached final target loss 0.00741 and accuracy 1.0000 for q2_lora, matching fp_lora and far exceeding q2_no_adapter accuracy 0.1546. Rank-2/60-step stress kept q2_lora useful at accuracy 0.4639 versus q2_no_adapter 0.1553, but below fp_lora 0.5340.

## Boundaries and scale limits

Synthetic modular sequence data only; tiny approximately 0.18M parameter model; simulated per-row 2-bit dequantization rather than packed 2-bit kernels; no real pretrained LLM, real corpus, long run, optimizer robustness study, or home fine-tuning memory/throughput validation.

## Claim scope

On a tiny synthetic causal-Transformer adaptation task, a frozen per-row 2-bit base plus full-precision LoRA residual channel can recover target-task performance when adapter rank and training budget are sufficient; under rank-2 and short fine-tuning it still improves substantially over no adapter but lags full-precision-base LoRA.

## Why it stopped

The evidence is bounded synthetic mechanism evidence, not direct full-scale or real-corpus validation; it supports a follow-up but not a paper-ready claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should deepen with a GPT-2-small-class real-text benchmark and rank/step sweep before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class 2-bit frozen-base LoRA residual benchmark
- Success threshold: q2_lora reaches within 10 percent relative held-out perplexity of fp_lora at rank 8 or rank 16 while beating q2_no_adapter by at least 30 percent relative perplexity reduction.
- Stop condition: Stop if q2_lora fails to beat q2_no_adapter by 15 percent relative perplexity reduction after a smoke plus one calibrated rank/step setting, or if memory/runtime exceeds the local GB10 budget documented before the run.

## Evidence references

- Artifact root: `<local-path>/projects/home-fine-tuning-2-bit-base-full-precision-lora-residual-channel-2ed5bdc6e453`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
