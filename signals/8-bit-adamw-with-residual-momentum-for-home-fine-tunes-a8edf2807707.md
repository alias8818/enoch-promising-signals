# 8-bit AdamW with residual momentum for home fine-tunes

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `8-bit-adamw-with-residual-momentum-for-home-fine-tunes-a8edf2807707`
Run ID: `8-bit-adamw-with-residual-momentum-for-home-fine-tunes-a8edf2807707-20260630T103234718089+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c56e9ba79ba4

## What looked useful

Residual first-moment error feedback, as implemented here with an fp16 residual buffer, was not justified: it doubled memory versus naive 8-bit AdamW without improving eval loss in two bounded benchmarks. Naive 8-bit AdamW itself remained a useful memory-saving baseline on this proxy.

## Boundaries and scale limits

Synthetic small-model proxy only; no pretrained LLM, LoRA/QLoRA, real text/code dataset, fused optimizer kernel, long run, or home fine-tune workload was validated. Python optimizer throughput is not a production performance claim.

## Claim scope

A simple CUDA PyTorch proxy compared fp32 AdamW, whole-tensor 8-bit AdamW, and 8-bit AdamW with fp16 first-moment residual error feedback on a tiny causal Transformer synthetic sequence task. Naive 8-bit AdamW matched fp32 convergence while using about 25% of fp32 optimizer-state memory; the residual-momentum variant did not improve eval loss versus naive 8-bit and used about 50% of fp32 optimizer-state memory.

## Why it stopped

Bounded proxy evidence did not support the residual-momentum addition; this is an early mechanism-level falsification, not a full validation of home fine-tuning.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is a bounded GPT-2-small LoRA fine-tune comparing naive 8-bit AdamW against a compressed-residual variant at equal or near-equal optimizer-state memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-memory residual 8-bit AdamW on a local GPT-2-small LoRA fine-tune
- Success threshold: Residual 8-bit AdamW improves mean validation loss versus naive 8-bit AdamW by at least 0.02 nats or a predeclared task metric by at least 1% relative, without exceeding 30% of fp32 AdamW optimizer-state memory.
- Stop condition: Stop if the residual variant exceeds the memory budget, fails to beat naive 8-bit AdamW across three seeds, or requires more than a local single-GPU bounded run to show an effect.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-residual-momentum-for-home-fine-tunes-a8edf2807707`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
