# State-Anchored Memory-Mapped KV for CPU Proxmox Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `state-anchored-memory-mapped-kv-for-cpu-proxmox-long-context-6bc3a9286a73`
Run ID: `state-anchored-memory-mapped-kv-for-cpu-proxmox-long-context-6bc3a9286a73-20260531T232110892121+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5726c9c194d7

## What looked useful

Persistence passed across reopen. Hot mmap throughput was 745 MiB/s sequential, 595 MiB/s local-window, and 418 MiB/s random versus RAM-copy retrieval at 970, 894, and 821 MiB/s. Cold-ish mmap fell to 145 MiB/s sequential and about 36-39 MiB/s random/local-window with hundreds of major faults. RAM baseline required loading a private copy, measured as roughly 1024 MiB RSS delta while the mmap path used file-backed resident pages.

## Boundaries and scale limits

Synthetic 512 MiB KV store, 4 KiB records, 30000 retrievals per pattern, single-process Python/NumPy copy loop. No real transformer KV tensors, no decoder integration, no quality or end-to-end tokens/s measurement, and cold-cache behavior is only approximated with POSIX_FADV_DONTNEED.

## Claim scope

On a CPU Proxmox-like worker, a fixed-record mmap file can persist state-anchored KV blocks and retrieve hot/cache-resident 4 KiB blocks at hundreds of MiB/s without a mandatory private RAM copy, but cold random/local-window retrieval is dominated by page faults and is much slower than RAM.

## Why it stopped

The mechanism works in a synthetic storage benchmark, but the result is not paper-ready because it lacks real model integration and shows severe cold random-access penalties.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next concrete step is a bounded integration with a CPU inference loop measuring tokens/s and quality with mmap-backed anchored KV versus standard resident KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU Inference Probe for mmap-backed State-Anchored KV
- Success threshold: Hot/local anchor reuse achieves at least 75 percent of resident-KV tokens/s while reducing private anonymous KV memory by at least 30 percent and preserving output equivalence or bounded perplexity delta on the tested harness.
- Stop condition: Stop if mmap-backed inference loses more than 50 percent tokens/s in hot/local reuse, fails output/persistence correctness, or does not reduce private anonymous memory on the bounded model.

## Evidence references

- Artifact root: `<local-path>/projects/state-anchored-memory-mapped-kv-for-cpu-proxmox-long-context-6bc3a9286a73`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
