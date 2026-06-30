# Bounded Long-Context Training with VRAM Constraints

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-long-context-training-with-vram-constraints-f88a94bb7c19`
Run ID: `bounded-long-context-training-with-vram-constraints-f88a94bb7c19-20260611T031631546660+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a1a3c6f35e71

## What looked useful

Detached chunk memory gave a clear memory-scaling advantage: full attention used 18.727 GiB at 8192 tokens, while bounded attention used 1.274 GiB at 8192 and 4.976 GiB at 32768. However, exact associative-recall validation accuracy remained 0.000 for both full and bounded short training runs, and the bounded stop-gradient memory design cuts credit assignment to earlier chunks.

## Boundaries and scale limits

Toy model only: 2-3 layers, 96-192 hidden width, synthetic key/value retrieval, maximum bounded memory probe 32768 tokens, short training runs of 40 and 300 steps. No real corpus, GPT-2-small-class baseline, FlashAttention baseline, multi-seed robustness, or full-scale language-modeling validation.

## Claim scope

On a GB10 CUDA worker, a toy chunked transformer with detached recurrent memory substantially reduced peak CUDA allocation versus explicit full causal attention on synthetic long-context associative-recall probes, but did not demonstrate non-chance exact retrieval accuracy in short bounded training runs.

## Why it stopped

No paper-positive result: this was a toy/proxy early falsification of naive detached-memory long-context training quality, not a full validation of bounded long-context training.

## Recommended next action

Run a bounded deepen test that adds an explicit memory-writer credit-assignment mechanism, such as auxiliary per-chunk retrieval/reconstruction losses or replay, and require non-chance validation retrieval while preserving the memory advantage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Credit-assigned bounded memory for exact long-context retrieval
- Success threshold: Bounded method reaches at least 25% validation retrieval accuracy at 2048 tokens and at least 10% at 8192 tokens, beats detached-memory-only by at least 5 percentage points, and retains at least 4x lower peak CUDA allocation than explicit full attention at the same sequence length.
- Stop condition: Stop if auxiliary credit assignment fails to exceed 5% validation retrieval accuracy at 2048 tokens after 3 seeds or if the memory advantage falls below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-long-context-training-with-vram-constraints-f88a94bb7c19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
