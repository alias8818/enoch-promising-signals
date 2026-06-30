# CPU-RAM Subspace Gradient Projection for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-ram-subspace-gradient-projection-for-gpt-2-27058fe6e855`
Run ID: `cpu-ram-subspace-gradient-projection-for-gpt-2-27058fe6e855-20260601T070810834488+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a71d140b24df

## What looked useful

Projected updates can carry optimization signal at rank 1024/14848, reaching eval loss 4.2358 versus dense SGD 4.1803, but rank 64 and 256 lag badly and retained gradient energy tracks rank fraction. Explicit dense CPU-RAM bases scale as parameters times rank, implying about 29.6 GiB, 118.3 GiB, and 473.0 GiB for GPT-2-small at ranks 64, 256, and 1024 respectively.

## Boundaries and scale limits

No GPT-2-small training or GPU offload path was run. GPT-2-small memory numbers are extrapolated from explicit basis scaling, not measured on a 124M-parameter model.

## Claim scope

On a 14,848-parameter causal next-token model, explicit CPU-RAM random-subspace gradient projection trains only when rank is a material fraction of parameter count; low ranks retain little gradient energy and lag dense SGD.

## Why it stopped

Bounded local evidence supports the optimization mechanism at moderate rank but early-falsifies practical explicit CPU-RAM dense-basis use for GPT-2 because competitive ranks imply excessive host-memory storage and slower updates; this is proxy/small-model evidence, not full GPT-2 validation.

## Recommended next action

Stop this explicit dense-basis CPU-RAM projection idea as no-paper useful signal; only pursue a new bounded branch if replacing the explicit basis with an implicit structured projection such as Hadamard or CountSketch.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Implicit Structured Subspace Projection for GPT-Style Training
- Success threshold: Match or improve explicit rank-1024 eval loss within 0.03 while using less than 2x dense-SGD runtime and extrapolated GPT-2-small projection storage below 16 GiB.
- Stop condition: Stop if implicit projection eval loss remains worse than 4.30 on the local benchmark or runtime exceeds dense SGD by more than 3x without a memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-ram-subspace-gradient-projection-for-gpt-2-27058fe6e855`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
