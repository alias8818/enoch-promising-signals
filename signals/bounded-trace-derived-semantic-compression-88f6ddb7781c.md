# Bounded Trace-Derived Semantic Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-trace-derived-semantic-compression-88f6ddb7781c`
Run ID: `bounded-trace-derived-semantic-compression-88f6ddb7781c-20260620T064653412635+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/86bb76839617

## What looked useful

Semantic selection can outperform raw compression and equal-budget truncation when traces contain task-irrelevant high-entropy diagnostic noise, but the signal is bounded to a controlled grammar and should not be treated as publication-grade validation.

## Boundaries and scale limits

Synthetic traces only; hand-written extractor matched to the generator; no production logs, learned extractor, schema drift, adversarial traces, LLM summaries, or downstream model-context benchmark were tested.

## Claim scope

On deterministic synthetic workflow traces with a known grammar and eight fixed query fields, hand-written semantic fact extraction preserved all measured target answers while reducing mean compressed size to 17.98% of raw zlib size in the 500-case main run.

## Why it stopped

No-paper closure: the result is a synthetic controlled-grammar useful signal, not a direct validation on real traces or downstream model behavior.

## Recommended next action

Run a bounded held-out trace benchmark using real or public workflow logs with schema drift and the same fixed query-fidelity/byte-size metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out real-trace semantic compression benchmark
- Success threshold: Mean query accuracy >= 0.95 and semantic compressed size <= 0.35x raw zlib size on held-out traces, with no individual critical field below 0.90 accuracy.
- Stop condition: Stop as negative if held-out query accuracy is below 0.90, if semantic size exceeds 0.50x raw zlib at comparable accuracy, or if failures cluster around schema drift that the bounded extractor cannot handle.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-trace-derived-semantic-compression-88f6ddb7781c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
