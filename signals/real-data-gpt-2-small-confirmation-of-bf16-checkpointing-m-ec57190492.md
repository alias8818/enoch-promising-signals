# Real-data GPT-2-small confirmation of bf16 checkpointing memory reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492`
Run ID: `real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492-20260607T211530589479+0000`

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

- Parent run decision: Gradient Checkpointing + Mixed Precision for 60% VRAM Reduction: enoch://control-plane/projects/gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a/runs/gradient-checkpointing-mixed-precision-for-60-vram-reduction-a3afc381745a-20260607T170532278631+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d23b46f8b45c

## What looked useful

A direct small GPT-2-small real-data test supports the expected bf16 activation-checkpointing memory reduction mechanism, with 37-40% lower peak allocated memory and 47-48% lower reserved memory across two batch sizes.

## Boundaries and scale limits

Single GPU, one dataset, one seed, two batch sizes, sequence length 1024, three optimizer steps per scenario; no sustained throughput, convergence, multi-seed, or multi-dataset validation.

## Claim scope

On a single NVIDIA GB10, pretrained GPT-2-small fine-tuning on real Wikitext-2 tokens for three optimizer steps showed bf16 activation checkpointing reduced peak CUDA allocated memory by 36.8% at batch 4 and 39.5% at batch 8 versus bf16 without checkpointing.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains too short and narrow for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded medium confirmation with more steps, multiple seeds, batch and sequence sweeps, and sustained throughput measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2-small bf16 checkpointing memory and throughput sweep
- Success threshold: At least 30% median peak allocated memory reduction for bf16 checkpointing versus bf16 no-checkpoint across the sweep, with no loss-path failure and documented throughput overhead.
- Stop condition: Stop if repeated direct GPT-2-small real-data runs show less than 15% median peak allocated reduction or inconsistent losses indicating an invalid checkpointed training path.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-gpt-2-small-confirmation-of-bf16-checkpointing-m-ec57190492`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
