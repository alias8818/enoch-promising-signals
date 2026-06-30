# Selective activation recomputation vs uniform gradient checkpointing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `selective-activation-recomputation-vs-uniform-gradient-checkpointing-03e5ad1caeb4`
Run ID: `selective-activation-recomputation-vs-uniform-gradient-checkpointing-03e5ad1caeb4-20260621T183352348856+0000`

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

Broad selective checkpointing was 6-10% faster than uniform on larger cases but used roughly 99-138% more peak memory than uniform. A tighter linear-only selective policy was only 2-3% faster than uniform while using about 35-44% more memory. Attention bmm saves drive both speedup and memory regression.

## Boundaries and scale limits

Synthetic tokens only; one CUDA device; short 6-12 measured-step runs; no convergence study; no real GPT-2-small training corpus; no distributed, optimizer-state sharding, compiler, or production-kernel validation.

## Claim scope

On a local single-GB10 synthetic GPT-style bf16 benchmark with 12 layers, d_model 768, and sequence lengths up to 1024, selective activation recomputation can reduce uniform checkpointing step-time overhead, but the useful speed/memory Pareto gain is small unless expensive attention bmm outputs are saved, which substantially increases memory.

## Why it stopped

No-paper useful signal: the local proxy directly measured checkpoint memory/time tradeoffs but did not show a strong enough Pareto improvement over uniform checkpointing for publication-grade support.

## Recommended next action

Run a bounded GPT-2-small-class training benchmark comparing uniform checkpointing against linear-only selective checkpointing with matched tokens, real data, loss parity checks, and at least three seeds or repeated timing windows.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small linear-only selective checkpointing confirmation
- Success threshold: Linear-only selective checkpointing is at least 5% faster than uniform checkpointing with no more than 50% peak-memory overhead and no worse loss trajectory over the matched measured window.
- Stop condition: Stop if the speedup is below 5%, memory overhead exceeds 50%, or loss parity fails under matched settings.

## Evidence references

- Artifact root: `<local-path>/projects/selective-activation-recomputation-vs-uniform-gradient-checkpointing-03e5ad1caeb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
