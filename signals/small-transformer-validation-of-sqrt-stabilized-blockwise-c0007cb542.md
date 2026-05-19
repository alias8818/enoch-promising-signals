# Small-transformer validation of sqrt-stabilized blockwise int8 Adam v states

Status: `useful_signal`
Project ID: `small-transformer-validation-of-sqrt-stabilized-blockwise-c0007cb542`
Run ID: `small-transformer-validation-of-sqrt-stabilized-blockwise-c0007cb542-20260516T050422534967+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Small-transformer validation of sqrt-stabilized blockwise int8 Adam v states: internal_generated:small-transformer-validation-of-sqrt-stabilized-blockwise-c0007cb542

## What looked useful

Sqrt-domain quantization stabilizes blockwise int8 Adam second-moment state in direct transformer training controls: fp32 val loss 1.5572 vs sqrt-int8 1.5554 on 1.27M, and fp32 1.5886 vs sqrt-int8 1.5924 on 10.7M, while direct int8-v produced validation losses in the hundreds. Total optimizer-state memory fell about 37.3%, with estimated v-state-only reduction about 74.6%.

## Boundaries and scale limits

Local GB10 runs only; character-level Tiny Shakespeare corpus; custom Python/PyTorch optimizer; no GPT-2-small-class tokenized benchmark, no fused CUDA optimizer, no distributed or large-LLM validation, and no production throughput claim.

## Claim scope

On Tiny Shakespeare character-level small-transformer training at 1.27M and 10.7M parameters, blockwise int8 storage of sqrt(Adam v) matched fp32 AdamW validation loss within 0.24% mean degradation across three fixed seeds while direct int8-v quantization diverged.

## Why it stopped

Tier 2 local evidence supports the mechanism but remains too narrow for publication-grade optimizer validation because it uses character-level Tiny Shakespeare and a research optimizer rather than GPT-2-small-class tokenized training or a fused production implementation.

## Recommended next action

Do not write a paper from this run; deepen with a GPT-2-small-class tokenized corpus validation using fp32 AdamW, direct int8-v, and sqrt-int8-v controls, with a <=1% validation-loss degradation threshold and measured optimizer memory/throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class tokenized validation of sqrt-int8 Adam v states
- Success threshold: sqrt-int8-v final validation loss no more than 1% worse than fp32 AdamW mean across three seeds, no divergent seeds, direct int8-v clearly worse or mechanistically explained, and estimated v-state memory reduced by at least 70%.
- Stop condition: Stop if sqrt-int8-v exceeds 1% validation-loss degradation versus fp32 on two or more seeds, diverges, or the next run cannot fit a GPT-2-small-class/tokenized benchmark locally within the available budget.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-sqrt-stabilized-blockwise-c0007cb542`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
