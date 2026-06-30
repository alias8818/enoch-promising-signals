# Block-wise 8-bit Adam moments for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-8-bit-adam-moments-for-gpt-2-small-pretraining-30ba25f34373`
Run ID: `block-wise-8-bit-adam-moments-for-gpt-2-small-pretraining-30ba25f34373-20260621T182337644725+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd6dc1ca7d1c

## What looked useful

The mechanism is memory-useful but block-size sensitive: 256-value blocks used 252.8 MB optimizer state versus 995.5 MB for AdamW on GPT-2-small-shaped tensors, and 200-step small-GPT validation loss was 2.3293 versus 2.3286 for AdamW. Coarser 1024 and 2048 blocks diverged to validation losses 154.9 and 68.4.

## Boundaries and scale limits

No full GPT-2-small pretraining was run. Training evidence is a 3.23M-parameter GPT-style proxy for 200 updates on Tiny Shakespeare from one seed. GPT-2-small-scale evidence is optimizer-state/update only with synthetic gradients. Runtime evidence is for an unfused PyTorch implementation, not a production fused optimizer.

## Claim scope

On GB10 CUDA, a simple block-wise linear 8-bit AdamW moment implementation reduces optimizer-state memory by about 4x at GPT-2-small parameter shape and can match 200-step small-GPT Tiny Shakespeare validation loss when blocks are 256-512 values; 1024-2048 value blocks diverge in the same setup.

## Why it stopped

Closed as no-paper useful signal: the local evidence is enough to define a viability boundary and avoid coarse blocks, but it is proxy/short-run evidence rather than full GPT-2-small pretraining validation.

## Recommended next action

Run a bounded deepen study with 256-value block 8-bit moments for at least 1000-2000 small-GPT steps across three seeds, including checkpoint/resume persistence and a fused-kernel feasibility estimate; stop if validation loss exceeds AdamW by more than 1% after warmup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed longer small-GPT validation for 256-block 8-bit Adam moments
- Success threshold: Across three seeds, final validation loss is within 1% of AdamW and no run diverges; optimizer-state memory remains at least 3.7x smaller than AdamW.
- Stop condition: Stop early if any 256-block run diverges, if mean validation loss is more than 3% worse than AdamW after 500 updates, or if fused-kernel profiling shows unavoidable optimizer overhead large enough to erase the memory benefit for GPT-2-small-class training.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-8-bit-adam-moments-for-gpt-2-small-pretraining-30ba25f34373`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
