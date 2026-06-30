# Sparse KV Residuals for 128k CPU Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-kv-residuals-for-128k-cpu-context-5f57badf6096`
Run ID: `sparse-kv-residuals-for-128k-cpu-context-5f57badf6096-20260525T112526442507+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a884e882bba0

## What looked useful

At 4,608 compressed tokens for a 131,072-token trace (28.44x token compression), residual summaries reduced overall mean relative L2 versus matched sparse anchors by 29.7% on average and reduced topic-query relative L2 from 0.762 to 0.241, but needle-query relative L2 stayed about 1.0 despite full attention assigning 0.999997 mean mass to the target needle.

## Boundaries and scale limits

Synthetic KV only; 64-dimensional single-layer single-step attention; no real LLM KV traces, no language-model task accuracy, no inference-engine integration, no GPU/kernel benchmarking, and only three random seeds.

## Claim scope

On synthetic 128k-token CPU single-step attention traces, contiguous residual summary slots improve broad/topic attention-output reconstruction over equal-token fixed sparse retention, but they fail exact old-needle retrieval when the rare token is not explicitly retained.

## Why it stopped

No paper-ready result: the local evidence is a useful mixed synthetic signal, not direct real-model validation, and it exposes a retrieval failure mode for residual-only compression.

## Recommended next action

Run a bounded real-model deepen test combining residual summaries with an explicit rare-token selector; stop treating residual-only sparse KV as a complete 128k CPU-context solution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid residual summaries with rare-token retention on real 128k KV traces
- Success threshold: At equal KV memory, hybrid residual+rare retention improves broad reconstruction by at least 20% relative L2 versus matched sparse while keeping old-needle retrieval accuracy within 2 percentage points of full KV on a bounded real-model task.
- Stop condition: Stop if rare-token retention cannot recover needle accuracy at equal memory, or if residual build/decode overhead eliminates the CPU memory benefit on the bounded real-model workload.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-kv-residuals-for-128k-cpu-context-5f57badf6096`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
