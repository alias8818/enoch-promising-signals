# mmap-based optimizer state offload for CPU GPT-2-small training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mmap-based-optimizer-state-offload-for-cpu-gpt-2-small-training-87ac5b18aaff`
Run ID: `mmap-based-optimizer-state-offload-for-cpu-gpt-2-small-training-87ac5b18aaff-20260628T083443766266+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3118b0c19190

## What looked useful

Mmap optimizer state is viable as a Linux memory-class/persistence mechanism: 25M params reduced final Anonymous by 195,288 kB with unchanged RSS, and 100M params reduced final Anonymous by 781,256 kB with unchanged RSS. Per-step flush made the 25M run 1.49x slower; no-flush mmap was not slower in these short vectorized probes, but timing is not robust enough to claim speedup.

## Boundaries and scale limits

Not a full GPT-2-small Transformer training run, no PyTorch autograd stack, no dataset convergence evidence, no memory-pressure/eviction stress test, and only two 100M-parameter optimizer steps. The 100M parameter-count probe is close to GPT-2-small scale for optimizer state but remains a proxy for full training.

## Claim scope

In deterministic CPU NumPy AdamW parameter-vector probes up to 100M float32 parameters, mmap-backed first/second moments moved optimizer state from anonymous memory into file-backed mappings roughly equal to the Adam state size, but did not reduce total RSS for actively touched state and was slower when flushing every step.

## Why it stopped

Proxy evidence supports the memory-class mechanism but does not provide direct full GPT-2-small training, convergence, or pressure-stall evidence required for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the same mmap optimizer inside PyTorch or a minimal autograd Transformer block and test under explicit memory pressure with validation loss parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch mmap AdamW under memory pressure for small GPT training
- Success threshold: At equal model/data/seed, mmap AdamW reaches within 1% validation loss of standard AdamW, reduces Anonymous memory approximately by the fp32 m/v state size, avoids OOM or improves MemAvailable under constrained RAM, and keeps median step-time overhead below 20% with checkpoint-aligned flushing.
- Stop condition: Stop if mmap AdamW diverges from standard updates/loss, fails to reduce anonymous memory by at least 80% of the expected m/v state size, or requires per-step flushing that adds more than 50% median step-time overhead.

## Evidence references

- Artifact root: `<local-path>/projects/mmap-based-optimizer-state-offload-for-cpu-gpt-2-small-training-87ac5b18aaff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
