# Memory-Mapped Compressed Context Paging

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-compressed-context-paging-f2d521b56001`
Run ID: `memory-mapped-compressed-context-paging-f2d521b56001-20260607T184310088750+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e787b6d18d00

## What looked useful

Lossless fp16 page compression was not attractive: zstd only achieved about 1.08-1.15x size reduction while adding tens to hundreds of microseconds per refill, and lz4 was fast but effectively did not compress. q8+zstd achieved about 2.1-2.5x footprint reduction, but refill latency was about 61-69 us for 16 KiB pages, 262-264 us for 64 KiB pages, and about 0.98-1.08 ms for 256 KiB pages in the Python/CPU path. The viable branch is quantized compressed paging with small pages and overlapped compiled/GPU refill, not lossless compression of fp16 pages.

## Boundaries and scale limits

No real transformer KV tensors, no model-quality or perplexity measurement, no GPU-side decompression, no concurrent serving scheduler, and no cold NVMe page-cache eviction. Results are bounded to local cached mmap reads and synchronous CPU decompression/restoration.

## Claim scope

Synthetic CPU memory-system proxy for memory-mapped compressed context paging using fp16 KV-cache-like pages of 16 KiB, 64 KiB, and 256 KiB. Lossless zstd/lz4 and q8+zstd mmap refill were compared against raw mmap and RAM-byte baselines for compression ratio and page refill latency.

## Why it stopped

No-paper useful signal from a synthetic CPU proxy: lossless compressed mmap paging is early-falsified for fp16-like pages, while q8+zstd remains promising enough for a direct model-KV follow-up but is not validated here.

## Recommended next action

Run a bounded GPT-2-small-class replay/serving test with real KV tensors, q8 page restoration, perplexity or output-drift checks, and measured overlap between compressed page refill and attention compute.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV Quantized Compressed Paging Replay
- Success threshold: At least 2x cold-context footprint reduction with no more than 1% perplexity degradation or a predeclared small output-drift tolerance, and less than 10% end-to-end token latency overhead versus raw fp16 mmap for the tested context lengths.
- Stop condition: Stop if real KV q8 restoration exceeds the quality tolerance, or if non-overlapped refill overhead remains above 10% token latency after using 16-64 KiB pages.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-compressed-context-paging-f2d521b56001`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
