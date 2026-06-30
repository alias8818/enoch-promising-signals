# PRNG-Masked Gradient Reproducibility Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prng-masked-gradient-reproducibility-test-00f3230693a8`
Run ID: `prng-masked-gradient-reproducibility-test-00f3230693a8-20260628T215444300437+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c26e074009b

## What looked useful

Fixed-seed stateless masked-gradient runs produced identical loss and model-state hashes across 3 repeats; changing only the mask seed changed the final state; an interrupted stateless run exactly matched the uninterrupted run without saving mask RNG state, while a stateful PRNG mask diverged under the same resume condition.

## Boundaries and scale limits

Tiny MLP, synthetic regression data, one device, one PyTorch/CUDA stack, 220 optimization steps, 3 repeats per case. This does not validate large-model training, distributed training, mixed precision, dataloader nondeterminism, or cross-hardware reproducibility.

## Claim scope

On a local NVIDIA GB10/PyTorch 2.12 CUDA synthetic regression task, stateless step-and-parameter-keyed PRNG gradient masks were bitwise reproducible across fixed-seed repeats and across an interrupted/resumed run that did not restore mask RNG state.

## Why it stopped

Bounded local evidence supports the mechanism but is not broad or direct enough for publication-grade validation.

## Recommended next action

Stop this worker run as no-paper useful evidence; next run should test the same stateless mask protocol on a real small vision or language training task with checkpoint/resume and mixed-precision controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpoint-resume PRNG-masked gradients on a real small training task
- Success threshold: Stateless masked checkpoint/resume final model hashes match exactly for at least 3 fixed-seed repeats, changed mask seeds produce distinct states, and validation metric degradation is less than 5 percent relative to the unmasked baseline on the bounded task.
- Stop condition: Stop if stateless masked checkpoint/resume hashes diverge under deterministic settings or validation degradation exceeds 5 percent in two independent repeats.

## Evidence references

- Artifact root: `<local-path>/projects/prng-masked-gradient-reproducibility-test-00f3230693a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
