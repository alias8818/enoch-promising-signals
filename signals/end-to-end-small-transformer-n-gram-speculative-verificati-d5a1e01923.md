# End-to-end small-transformer n-gram speculative verification latency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-small-transformer-n-gram-speculative-verificati-d5a1e01923`
Run ID: `end-to-end-small-transformer-n-gram-speculative-verificati-d5a1e01923-20260612T112413342434+0000`

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

- Parent run decision: KV-cache latency benchmark for n-gram speculative verification: enoch://control-plane/projects/kv-cache-latency-benchmark-for-n-gram-speculative-verifica-37049afd34/runs/kv-cache-latency-benchmark-for-n-gram-speculative-verifica-37049afd34-20260612T111907221263+0000
- Parent run decision: N-gram Draft Verification for Speculative Decoding Without Extra VRAM: enoch://control-plane/projects/n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07/runs/n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07-20260611T133733900797+0000

## What looked useful

Repeated-context prompts showed exact greedy-equivalent n-gram draft8 speculation at 0.0754 s median versus 0.0857 s for KV greedy, a 1.136x speedup with 22 median verifier calls and 0.908 mean draft acceptance. Low-repetition prompts showed the best n-gram variant at only 0.644x of KV greedy speed, so the effect is conditional and not robust.

## Boundaries and scale limits

Single small transformer, one GB10 GPU, short 64-token greedy decodes, small hand-written prompt sets, full-prefix verifier recomputation rather than production KV-cache-preserving speculative verification, no batching or real traffic traces.

## Claim scope

On distilgpt2 with CUDA timing, exact n-gram prompt-lookup speculative verification can modestly reduce median end-to-end latency versus KV-cache greedy decoding on hand-written repeated-context prompts when draft length is aggressive; the same method is slower than KV-cache greedy on low-repetition prompts.

## Why it stopped

Tier 2 evidence found a narrow repeated-context latency win but a clear low-repetition slowdown versus the real KV-cache baseline, and the verifier implementation is not production-faithful enough for publication.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should implement KV-cache-preserving n-gram verification and test broader repeated versus non-repeated corpora before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-preserving n-gram speculative verification on broader prompt classes
- Success threshold: Exact greedy match for all runs; median speedup >=1.2x versus KV-cache greedy on repeated/natural repeated prompts; median speed no worse than 0.95x KV greedy on low-repetition prompts.
- Stop condition: Stop if KV-cache-preserving implementation cannot exceed 1.05x median speedup on repeated prompts or still falls below 0.8x on low-repetition prompts after draft-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-transformer-n-gram-speculative-verificati-d5a1e01923`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
