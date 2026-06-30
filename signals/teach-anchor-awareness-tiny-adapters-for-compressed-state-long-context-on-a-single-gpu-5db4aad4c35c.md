# Teach Anchor Awareness: Tiny Adapters for Compressed-State Long Context on a Single GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `teach-anchor-awareness-tiny-adapters-for-compressed-state-long-context-on-a-single-gpu-5db4aad4c35c`
Run ID: `teach-anchor-awareness-tiny-adapters-for-compressed-state-long-context-on-a-single-gpu-5db4aad4c35c-20260630T063250201282+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/889938e71ba1

## What looked useful

The target task is solvable if the compressor preserves the post-anchor token, shown by oracle accuracy 1.0000, but the tiny learned adapter remained effectively uniform with target-token gate lift 1.0031x and accuracy only 0.0633 versus 0.0604 for uniform compression.

## Boundaries and scale limits

This is a toy synthetic probe, not a pretrained LLM or natural long-context benchmark. It tests one adapter form, one optimizer setting, one sparse-anchor data generator, and contexts up to 4096 tokens on a single GB10.

## Claim scope

On a synthetic compressed-state retrieval task with 4096-token contexts, 64-token chunks, a frozen random encoder, and a rank-4 learned token-gating adapter, the adapter did not learn anchor-local preservation from end-task gradients; an oracle anchor compressor solved the same task.

## Why it stopped

Proxy/early falsification of the naive tiny rank-4 end-task-trained adapter: it failed the predeclared +15 percentage point success signal by a wide margin, while the oracle positive control showed the synthetic task itself was learnable.

## Recommended next action

Stop this run as a bounded no-paper result; next test should add an explicit auxiliary anchor-gate objective or architectural locality bias and require non-uniform gate diagnostics before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Auxiliary-gated tiny adapters for sparse anchor preservation
- Success threshold: On 4096-token held-out synthetic sequences, achieve at least 0.25 accuracy, at least +0.15 absolute accuracy over uniform compression, and at least 8x target-token gate lift over uniform.
- Stop condition: Stop if gate lift remains below 2x after 1000 GPU training steps or if accuracy remains below 0.15 while the oracle compressor remains above 0.95.

## Evidence references

- Artifact root: `<local-path>/projects/teach-anchor-awareness-tiny-adapters-for-compressed-state-long-context-on-a-single-gpu-5db4aad4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
