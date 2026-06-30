# Memory-capped GPT-2-small-class blockwise uint8 AdamW offload fine-tune

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `memory-capped-gpt-2-small-class-blockwise-uint8-adamw-offl-c6a63b0bcc`
Run ID: `memory-capped-gpt-2-small-class-blockwise-uint8-adamw-offl-c6a63b0bcc-20260608T092115346648+0000`

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

- Parent run decision: 8-bit AdamW with uint8 optimizer state offloading for sub-4GB VRAM fine-tuning: enoch://control-plane/projects/8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0/runs/8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0-20260608T005050641046+0000
- Parent run decision: Hard-4GB mini causal-LM fine-tuning with blockwise uint8 AdamW offload: enoch://control-plane/projects/hard-4gb-mini-causal-lm-fine-tuning-with-blockwise-uint8-a-0bca380744/runs/hard-4gb-mini-causal-lm-fine-tuning-with-blockwise-uint8-a-0bca380744-20260608T051412680520+0000

## What looked useful

The memory-saving mechanism works in storage terms, but the tested drop-in blockwise uint8 AdamW offload path is not viable: all uint8 runs became non-finite while AdamW controls remained finite, and uint8 throughput was only about 24% of AdamW.

## Boundaries and scale limits

Synthetic token stream, 60-step runs, single GB10 host, and one symmetric per-block uint8 design for both Adam moments. This does not evaluate natural-language fine-tuning quality, longer stable training, fused kernels, fp32 second-moment variants, percentile scaling, or error-feedback quantization.

## Claim scope

On a deterministic GPT-2-small-class causal language-model training workload with 91.4M parameters, CPU-offloaded blockwise uint8 AdamW moment storage reduced optimizer-state bytes to about 25% of standard AdamW but reproducibly diverged to non-finite loss across fixed seeds and block-size/lower-LR controls.

## Why it stopped

Tier 2 local validation produced direct early falsification for this optimizer design: memory state shrank, but the uint8 offload optimizer diverged to non-finite loss in every tested seed while real AdamW baselines remained finite.

## Recommended next action

Stop this variant as a no-paper useful negative; only revisit with a bounded mechanism diagnostic that isolates first-moment versus second-moment quantization and must stay finite for the same 3-seed 60-step GPT-2-small-class matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Isolate Adam moment quantization failure in GPT-2-small-class uint8 offload
- Success threshold: At least one moment-isolation variant remains finite for all 3 seeds through 60 steps, preserves at least 35% optimizer-state memory reduction versus AdamW, and achieves at least 20% of AdamW throughput.
- Stop condition: Stop if all moment-isolation variants diverge before 60 steps on two or more seeds, or if the only stable variant preserves less than 35% optimizer-state memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/memory-capped-gpt-2-small-class-blockwise-uint8-adamw-offl-c6a63b0bcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
