# Layered Memory With Noisy Extraction vs Temporal Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-with-noisy-extraction-vs-temporal-flat-retr-8137fdb8cd`
Run ID: `layered-memory-with-noisy-extraction-vs-temporal-flat-retr-8137fdb8cd-20260619T233931759567+0000`

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

- Parent run decision: Layered Agent Memory vs Flat Retrieval on Multi-Session Tasks: enoch://control-plane/projects/layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6/runs/layered-agent-memory-vs-flat-retrieval-on-multi-session-tasks-ebdcaffd13d6-20260619T231801631829+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fbfae992bbdc

## What looked useful

Layered memory beat temporal flat retrieval by +58.9 to +75.0 percentage points at 20% extraction noise across the three temporal windows, because temporal flat retrieval missed stale facts outside its context window. The same diagnostics show layered memory is worse for recent facts when extraction noise corrupts or drops values, so the mechanism favors stale retention rather than universally better retrieval.

## Boundaries and scale limits

Tested only generated event streams with exact keys, 30 seeds, 200 entities, 4000 events, window sizes 50/100/200, and synthetic extraction noise. Did not test semantic retrieval, paraphrase, learned extractors, neural model answering, real conversations, or large-scale training.

## Claim scope

In a controlled synthetic latest-fact QA task with exact entity-attribute grounding, fixed temporal flat retrieval windows, and independent extraction dropout/corruption, layered per-key memory preserved stale facts far better than newest-K temporal flat retrieval through 20% extraction noise.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal, but it is synthetic and not publication-grade evidence.

## Recommended next action

Run a bounded deepen test against semantic full-store flat retrieval with paraphrased queries and a realistic small-model or rule-plus-noise extractor; stop paper consideration until that baseline is tested.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Memory vs Semantic Flat Retrieval With Paraphrase and Realistic Extraction Errors
- Success threshold: Layered or hybrid memory beats semantic flat retrieval by at least 10 percentage points on stale facts at <=20% measured extraction error while losing no more than 3 points on within-window recent facts.
- Stop condition: Stop if semantic flat retrieval closes the stale-fact gap below 5 points or if realistic extraction errors cause more than a 10-point recent-fact regression that a hybrid policy cannot remove.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-with-noisy-extraction-vs-temporal-flat-retr-8137fdb8cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
