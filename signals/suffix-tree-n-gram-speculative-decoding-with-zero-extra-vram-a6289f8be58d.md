# Suffix-tree n-gram speculative decoding with zero extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-n-gram-speculative-decoding-with-zero-extra-vram-a6289f8be58d`
Run ID: `suffix-tree-n-gram-speculative-decoding-with-zero-extra-vram-a6289f8be58d-20260620T205902869963+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fffce6da15c8

## What looked useful

The mechanism is promising for locally repetitive greedy continuations: draft length 16 gave the best estimated target-call reduction, while shorter drafts had higher acceptance rates. The proposer stayed CPU-only with no measured CUDA allocation after target traces.

## Boundaries and scale limits

No optimized online speculative decoder was implemented; wall-clock speedup, latency, KV-cache handling, CPU overhead under serving load, sampling behavior, larger models, larger corpora, and real workload robustness remain unvalidated.

## Claim scope

On GPT-2 greedy trace replay over six repetitive/mixed prompts and six non-repetitive prompts, a CPU-only suffix/n-gram proposer built from prompt plus generated history reduced estimated target verifier calls by 68.49% to 79.04% with 0.0 MiB measured CUDA allocation during the proposer phase.

## Why it stopped

No-paper useful signal: this run produced direct acceptance and VRAM evidence, but only proxy target-call estimates rather than production end-to-end speed measurements.

## Recommended next action

Build a cache-aware online prototype that verifies suffix/n-gram drafts with the target model KV cache and measure real tokens/sec, latency, CPU cost, and VRAM against greedy decoding on a realistic text/code prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware online suffix n-gram speculative decoding benchmark
- Success threshold: At least 20% end-to-end tokens/sec improvement over greedy decoding on repetitive workloads with no additional CUDA allocation beyond target-model variance and no more than 5% slowdown on low-repetition prompts.
- Stop condition: Stop if cache-correct verification cannot preserve greedy outputs, CPU proposer overhead erases call-reduction gains, or measured CUDA allocation exceeds the target-only baseline by more than normal allocator noise.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-decoding-with-zero-extra-vram-a6289f8be58d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
