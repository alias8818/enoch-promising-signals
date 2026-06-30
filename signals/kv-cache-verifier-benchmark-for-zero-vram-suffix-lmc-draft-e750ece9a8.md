# KV-cache verifier benchmark for zero-VRAM suffix-LMC drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-verifier-benchmark-for-zero-vram-suffix-lmc-draft-e750ece9a8`
Run ID: `kv-cache-verifier-benchmark-for-zero-vram-suffix-lmc-draft-e750ece9a8-20260611T090100148850+0000`

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

- Parent run decision: Suffix-LMC Speculative Decoding with Zero Draft VRAM on GB10: enoch://control-plane/projects/suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1/runs/suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1-20260611T053739748453+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46bcacdb967d

## What looked useful

The mechanism clears the local Tier 1 threshold: mean CPU lookup latency was 0.227-0.584 microseconds, p99 was 0.400-0.992 microseconds, resident draft KV peak would have been 64-512 MiB for the tested batch/suffix sizes, and zero-VRAM draft KV peak was 0 MiB by construction. This supports the bookkeeping and memory-saving mechanism but not a publication-grade systems claim.

## Boundaries and scale limits

Synthetic suffix table and acceptance model only; no real LMC drafter, no real verifier model, no GPU kernels, no end-to-end serving scheduler, and no measured model-quality acceptance trace.

## Claim scope

Controlled Tier 1 CPU bookkeeping and KV-memory accounting benchmark for zero-VRAM suffix-LMC draft verification. With 50k suffixes, 200k requests per scenario, suffix lengths 4/8/16/32, active batch 32, and 7B-class KV accounting, suffix lookup overhead stayed below 0.13% of a 50 microsecond/token verifier budget while eliminating resident draft-KV VRAM.

## Why it stopped

Tier 1 controlled direct mechanism test completed and produced useful no-paper evidence; paper readiness requires real-model end-to-end verifier evidence.

## Recommended next action

Run a bounded real-model speculative decoding test with a small suffix-LMC drafter and verifier, comparing end-to-end tokens/s, GPU memory, acceptance rate, and verifier stalls against a resident draft-KV baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model zero-VRAM suffix-LMC verifier microbenchmark
- Success threshold: Zero-VRAM variant is within 5% tokens/s of resident draft-KV baseline while reducing measured draft KV VRAM peak by at least 90% across suffix lengths 4, 8, 16, and 32.
- Stop condition: Stop if measured tokens/s drops by more than 10% in two independent prompt batches or if draft KV memory reduction is below 75%, because that would falsify the practical systems benefit at this tier.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-verifier-benchmark-for-zero-vram-suffix-lmc-draft-e750ece9a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
