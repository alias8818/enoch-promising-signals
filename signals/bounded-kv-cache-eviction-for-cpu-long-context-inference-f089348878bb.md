# Bounded KV-Cache Eviction for CPU Long-Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-cache-eviction-for-cpu-long-context-inference-f089348878bb`
Run ID: `bounded-kv-cache-eviction-for-cpu-long-context-inference-f089348878bb-20260629T070301966926+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed5246c3b5cb

## What looked useful

Content-aware retention is the promising mechanism; bounded recent-only eviction is insufficient for arbitrary far-context recall. The next useful test should replace oracle landmarks with a real importance score in a small CPU transformer loop.

## Boundaries and scale limits

Synthetic vectors only; no real transformer inference, perplexity, task-quality, tokenizer effects, or non-oracle importance detector. CPU timing is NumPy dot-product microbenchmarking rather than integrated model-server latency.

## Claim scope

In a deterministic synthetic KV-cache probe up to 16384 tokens, a bounded content-aware landmark+recent policy preserved far-context needle recall while cutting final fp16 KV memory proxy by 96.5-98.8%; non-content-aware recent/reservoir baselines lost substantial far recall.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism is synthetic and oracle-assisted, not direct LLM inference evidence.

## Recommended next action

Implement a non-oracle importance detector in a small CPU transformer inference benchmark and require quality retention against full-cache/sliding baselines before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle bounded KV eviction in a small CPU transformer loop
- Success threshold: At least 95% of full-cache quality on the selected long-context task, at least 4x peak KV memory reduction, and no worse than 20% tokens/sec regression versus sliding at the same cap.
- Stop condition: Stop if the non-oracle importance policy fails to beat sliding-window quality at equal cache cap on two seeds or if CPU runtime exceeds the bounded local budget without producing checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-eviction-for-cpu-long-context-inference-f089348878bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
