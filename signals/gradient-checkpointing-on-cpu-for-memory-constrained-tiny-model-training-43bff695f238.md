# Gradient checkpointing on CPU for memory-constrained tiny model training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-checkpointing-on-cpu-for-memory-constrained-tiny-model-training-43bff695f238`
Run ID: `gradient-checkpointing-on-cpu-for-memory-constrained-tiny-model-training-43bff695f238-20260607T172139620248+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

Checkpointing saved 48 MiB/5.3% RSS at 6.9M params, 197 MiB/15.2% at 17.4M params, and 368 MiB/19.0% at 40.2M params across normal and reverse ordering. Timing was noisy, but the activation-heavy case stayed between 0.83x and 1.08x relative step time.

## Boundaries and scale limits

Synthetic random-token training only; 3-4 measured steps per case after warmup; one CPU worker; no real dataset convergence, cgroup memory-limit, OOM-boundary, GPT-2-small-class, or long-run validation.

## Claim scope

On a CPU-only PyTorch tiny-transformer benchmark, per-block activation checkpointing is not useful at the smallest 6.9M-parameter scale, is borderline around 17.4M parameters, and consistently reduces peak RSS by about 19% with near-parity step time on a 40.2M-parameter sequence-512 activation-heavy configuration.

## Why it stopped

Bounded local benchmark supports the mechanism only for activation-heavy tiny CPU training, but evidence is synthetic, short-run, and not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a medium confirmation with longer repeated runs, real memory caps, and GPT-2-small-class or parameter-matched baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of CPU checkpointing under real memory caps
- Success threshold: Checkpointing must increase the largest trainable batch/sequence product by at least 15% under fixed memory caps while keeping median step-time slowdown at or below 1.8x in at least two realistic tiny-model configurations.
- Stop condition: Stop if repeated capped-memory runs show less than 10% capacity improvement or median slowdown above 2.0x on realistic tiny-model baselines.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-on-cpu-for-memory-constrained-tiny-model-training-43bff695f238`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
