# Quantized long-context training for home GPU memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-long-context-training-for-home-gpu-memory-73919379c4f3`
Run ID: `quantized-long-context-training-for-home-gpu-memory-73919379c4f3-20260611T154501366729+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/17d687b72f1b

## What looked useful

Quantized optimizer state saved 0.067 GB on a 33.6M parameter model and 0.352 GB on a 176.2M parameter model, but peak memory at long sequence was unchanged at 2048-8192 tokens for the smaller model and 4096-8192 tokens for the larger model. Activation checkpointing gave a larger peak-memory reduction at 8192 tokens.

## Boundaries and scale limits

Synthetic one-step runs only; no convergence test, no real corpus, no production fused 8-bit optimizer, no enforced 16-24 GB device cap, no 7B-class model, and no multi-hour stability validation.

## Claim scope

On one-step synthetic BF16 causal-transformer training on GB10, int8 persistent Adam moments halve optimizer-state storage but do not reduce long-sequence peak memory at 4096-8192 tokens for the tested 33.6M and 176.2M parameter models.

## Why it stopped

Proxy/local mechanism test completed; evidence is useful but insufficient for a paper or broad validation because it does not test real training convergence or production optimizer kernels.

## Recommended next action

Run a bounded follow-up with a production fused or blockwise 8-bit optimizer under an enforced 24 GB memory cap and compare max reachable sequence length against activation-checkpointed AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 24 GB capped max-sequence test with production-style 8-bit optimizer states
- Success threshold: 8-bit optimizer increases max reachable sequence length by at least 25% over the strongest AdamW baseline at similar loss behavior, not just persistent memory bytes.
- Stop condition: Stop if checkpointed AdamW matches or exceeds the 8-bit optimizer max sequence length, or if 8-bit optimizer instability prevents comparable loss over the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-long-context-training-for-home-gpu-memory-73919379c4f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
