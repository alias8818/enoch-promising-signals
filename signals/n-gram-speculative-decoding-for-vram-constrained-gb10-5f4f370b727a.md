# N-gram Speculative Decoding for VRAM-Constrained GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-decoding-for-vram-constrained-gb10-5f4f370b727a`
Run ID: `n-gram-speculative-decoding-for-vram-constrained-gb10-5f4f370b727a-20260605T185805232688+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5599534680ce

## What looked useful

Exact-output n-gram speculative decoding showed 2.35x-3.23x mean speedup on distilgpt2 across draft lengths 8-16 and 3.11x mean speedup on gpt2 at draft length 16, with target forwards falling from 768 to 363 for distilgpt2 draft16 and from 768 to 231 for gpt2 draft16. A correctness bug in partial-mismatch cache handling was found and fixed by conservative cache recomputation.

## Boundaries and scale limits

Small GPT-2-class models only; no 7B-class model, no near-capacity UMA/VRAM pressure, no production serving runtime, no batching, no quantized long-context workload, and only six prompts.

## Claim scope

On this GB10 worker, a Python/Hugging Face prompt-lookup n-gram speculative decoder preserved exact greedy outputs and reduced target forward calls for distilgpt2 and gpt2 over six WikiText-2 validation prompts with 128 generated tokens per prompt.

## Why it stopped

This run produced useful bounded mechanism evidence but not direct VRAM-constrained large-model serving evidence, so it is no-paper local evidence rather than a final positive result.

## Recommended next action

Run a bounded deepen test on a quantized 1B-3B or 7B-class model with long prompts and explicit UMA memory pressure, using the same exact-output check plus non-repetitive prompt controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram speculative decoding under long-context UMA pressure
- Success threshold: Median speedup >= 1.25x with exact_match_all true, no prompt below 0.90x baseline throughput, and MemAvailable remaining above an explicitly documented safety floor.
- Stop condition: Stop if exact equivalence fails, if median speedup is below 1.10x after correctness fixes, or if memory pressure cannot be produced safely on the worker.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-vram-constrained-gb10-5f4f370b727a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
