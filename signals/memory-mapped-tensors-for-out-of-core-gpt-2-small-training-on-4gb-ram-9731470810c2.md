# Memory-mapped tensors for out-of-core GPT-2-small training on 4GB RAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-tensors-for-out-of-core-gpt-2-small-training-on-4gb-ram-9731470810c2`
Run ID: `memory-mapped-tensors-for-out-of-core-gpt-2-small-training-on-4gb-ram-9731470810c2-20260523T211213706954+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9716dd2a98f5

## What looked useful

Shared memory-mapped Adam moments reduced anonymous RSS before state access, but after a complete Adam update over 124,439,808 GPT-2-small-sized parameters, total peak RSS was essentially identical to in-RAM moments at about 2125 MiB. mmap shifted roughly 0.95 GiB from anonymous RSS to file-backed RSS and was slower in early steps; both modes passed a 4GiB virtual-address-limit optimizer-only check.

## Boundaries and scale limits

Did not run full GPT-2-small forward/backward, real data, loss curves, or a true 4GiB no-swap cgroup. Tested fp32 optimizer-state memory behavior only.

## Claim scope

Bounded optimizer-state-only probe over GPT-2-small-sized fp32 parameter, gradient, and Adam moment tensors on a CPU PyTorch worker.

## Why it stopped

Proxy optimizer-state evidence does not support mmap tensors as sufficient for out-of-core GPT-2-small training on 4GB RAM; it lowers anonymous RSS but not the full touched working set after optimizer steps.

## Recommended next action

Stop this run as a proxy/early falsification of the broad 4GB training claim; the next bounded test should run an actual GPT-2-small forward/backward step under a real 4GiB no-swap cgroup and compare standard AdamW against the mmap Adam implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small training step under 4GiB no-swap cgroup with mmap Adam moments
- Success threshold: mmap Adam completes at least 3 repeated GPT-2-small training steps under 4GiB no-swap where standard AdamW OOMs, with no more than 2x step-time slowdown and matching finite loss/gradient behavior.
- Stop condition: Stop if both modes fit with similar memory, both OOM at the same sequence/batch setting, or mmap exceeds 2x slowdown without enabling a larger feasible batch/sequence configuration.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-tensors-for-out-of-core-gpt-2-small-training-on-4gb-ram-9731470810c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
