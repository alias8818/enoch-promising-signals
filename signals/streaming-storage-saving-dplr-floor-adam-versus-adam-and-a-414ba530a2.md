# Streaming storage-saving DPLR/floor Adam versus Adam and Adafactor

Status: `useful_signal`
Project ID: `streaming-storage-saving-dplr-floor-adam-versus-adam-and-a-414ba530a2`
Run ID: `streaming-storage-saving-dplr-floor-adam-versus-adam-and-a-414ba530a2-20260516T071223379587+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Streaming storage-saving DPLR/floor Adam versus Adam and Adafactor: internal_generated:streaming-storage-saving-dplr-floor-adam-versus-adam-and-a-414ba530a2

## What looked useful

Factored Adam second-moment storage is a practical storage-saving signal versus AdamW on this task, but the floor mechanism is sensitive: floor_mult=0.1 hurts every seed while floor_mult=0.01 behaves like no-floor. Adafactor saves much more state but has much worse validation loss under the tested settings.

## Boundaries and scale limits

This is a bounded local character-LM benchmark, not GPT-2-small-class or full-scale LLM evidence. It does not test longer training, large vocabularies, mixed precision robustness, distributed training, fused optimizer throughput, or memory-pressure-limited batch/model scaling.

## Claim scope

On a 3-layer, 256-wide character Transformer trained for 500 steps on Tiny Shakespeare with seeds 0, 1, and 2, a factored-second-moment AdamW variant without an aggressive floor, or with floor_mult=0.01, matched AdamW validation loss while using about 50.3% of AdamW optimizer-state bytes. The tested floor_mult=0.1 variant was consistently worse than AdamW and the no-floor ablation.

## Why it stopped

No-paper closure: the local Tier 2 benchmark produced a useful mechanism signal but also showed the proposed floor is harmful when too large, and the evidence is not broad or long enough for publication.

## Recommended next action

Run a bounded deepen test on a tokenized GPT-2-small-class text setup with a floor grid, matched learning-rate sweeps, and a fixed memory-budget batch/context scaling test; stop if no factored variant matches AdamW within 1% validation loss while enabling a concrete memory-budget gain.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class memory-budget validation for factored Adam floor sweep
- Success threshold: At least one factored Adam variant matches AdamW final validation loss within 1% over three seeds, uses <=60% of AdamW optimizer-state bytes, beats Adafactor validation loss by >=10%, and demonstrates a concrete fixed-memory batch or context increase without worse validation loss.
- Stop condition: Stop if all factored variants are >1% worse than AdamW after matched tuning, if the memory savings do not translate to any fixed-budget scaling gain, or if floor variants remain no better than the no-floor ablation.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-storage-saving-dplr-floor-adam-versus-adam-and-a-414ba530a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
