# QLoRA-mini: INT8 Quantization with Minimal Rank Adaptation for 350M Params

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `qlora-mini-int8-quantization-with-minimal-rank-adaptation-for-350m-params-180630d6c2d9`
Run ID: `qlora-mini-int8-quantization-with-minimal-rank-adaptation-for-350m-params-180630d6c2d9-20260614T125553625893+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9c36983d595

## What looked useful

INT8 did not measurably harm very-low-rank adaptation in this 350M-class probe: corrected seed-17 final losses were fp16/int8 rank1 3.5685/3.5611, rank2 3.5835/3.5741, rank4 3.5527/3.5475; seed-23 ranks 1 and 4 repeated the near-parity pattern.

## Boundaries and scale limits

Short 40-step run, small WikiText-2 slices, batch size 1, two seeds only for ranks 1 and 4, and a custom INT8 proxy rather than bitsandbytes/PEFT QLoRA. No downstream task accuracy, convergence run, instruction tuning, rank schedule, or larger-model validation.

## Claim scope

On a bounded OPT-350M WikiText-2 probe, frozen per-row INT8 linear weights with q/v LoRA ranks 1, 2, and 4 matched fp16 LoRA early adaptation loss after 40 adapter-only steps.

## Why it stopped

No-paper useful signal: the direct 350M probe supports the mechanism locally, but the evidence is too short, narrow, and proxy-implemented for publication-grade validation.

## Recommended next action

Run a medium confirmation with a standard quantized backend or faithful INT8 memory-saving kernel, 3-5 seeds, longer fixed-token training, and one downstream task before considering a bounded paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium OPT-350M INT8 LoRA confirmation with standard backend and downstream task
- Success threshold: INT8 LoRA rank 1-4 remains within 1% relative final validation loss or downstream accuracy of fp16 LoRA at the same rank while reducing frozen-base weight storage materially versus fp16.
- Stop condition: Stop if standard INT8 backend cannot run on GB10 after install/debug, if INT8 LoRA trails fp16 LoRA by more than 3% relative loss across two seeds, or if memory/throughput benefits disappear under a faithful implementation.

## Evidence references

- Artifact root: `<local-path>/projects/qlora-mini-int8-quantization-with-minimal-rank-adaptation-for-350m-params-180630d6c2d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
