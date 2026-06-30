# Self-Speculative Decoding Without Draft Model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-without-draft-model-vram-237d9a23222f`
Run ID: `self-speculative-decoding-without-draft-model-vram-237d9a23222f-20260609T164513217787+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e2a380800d3b

## What looked useful

Zero-extra-parameter self-drafting is mechanically viable, but acceptance is the gating metric: mean acceptance around 0.957 gave up to 2.783x optimistic verifier speedup, while material late-layer changes dropped mean acceptance to 0.348 and removed even modeled speedup.

## Boundaries and scale limits

Synthetic CPU-only model; no pretrained LLM, no CUDA/KV-cache memory measurement, no sampling-quality evaluation, and no production serving stack. Optimistic verifier speedup is a latency model, not measured GPU wall-clock.

## Claim scope

A NumPy residual-decoder probe shows that using a prefix of the same model layers as a drafter can eliminate separate draft-model parameter memory and preserve exact greedy output under verification, but useful speedup appears only when early-layer next-token agreement is very high.

## Why it stopped

Bounded proxy evidence supports the mechanism but also shows the practical speedup depends on real-model early-layer agreement; this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should measure early-layer/full-model next-token agreement and end-to-end self-speculative decoding on a real small pretrained decoder with KV-cache batching.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure self-speculative early-exit agreement on a small pretrained decoder
- Success threshold: At least 1.2x measured decode throughput on a real small pretrained model with exact greedy equivalence and no separate draft-model weights loaded.
- Stop condition: Stop if no early-exit depth reaches 0.8 next-token agreement on representative prompts or if measured throughput remains below baseline after KV-cache batching.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-without-draft-model-vram-237d9a23222f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
