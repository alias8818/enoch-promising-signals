# Noisy metadata extraction for repeated-agent memory baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `noisy-metadata-extraction-for-repeated-agent-memory-baseli-9ef84479b2`
Run ID: `noisy-metadata-extraction-for-repeated-agent-memory-baseli-9ef84479b2-20260612T085703667200+0000`

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

- Parent run decision: Natural-language repeated-agent memory benchmark with metadata-aware flat baselines: enoch://control-plane/projects/natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25/runs/natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25-20260612T085159531192+0000
- Parent run decision: Layered memory vs flat retrieval on repeated agent tasks: enoch://control-plane/projects/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d/runs/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d-20260611T163801785554+0000

## What looked useful

Hard-filtering repeated-agent memory retrieval on stored metadata is brittle under metadata corruption. When agent/topic metadata is still present in memory text, a lightweight extraction/fusion layer can recover oracle-like retrieval and avoid the high empty-filter rates of noisy stored metadata.

## Boundaries and scale limits

Synthetic corpus only; deterministic pattern extractor; 2,000 memories per condition; no real agent traces, embedding model baseline, LLM extractor, alias drift, missing in-text metadata, or adversarial natural-language distractors.

## Claim scope

In a controlled repeated-agent synthetic memory benchmark with labeled agent/topic mentions, corrupting stored metadata causes metadata-filter retrieval to degrade while extracting canonical metadata from memory text recovers clean-oracle retrieval across five fixed seeds and noise levels up to 0.6.

## Why it stopped

Tier 2 synthetic validation supports the mechanism but is not direct naturalistic evidence or paper-positive validation.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded realistic-trace follow-up with generated or real agent conversations, an embedding baseline, and a non-oracle metadata extractor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic repeated-agent memory retrieval with noisy metadata and non-oracle extraction
- Success threshold: Across at least five fixed seeds and three noise levels, extraction/fusion improves top-1 retrieval by at least 10 percentage points over the best non-oracle baseline at moderate/high metadata noise, with extractor pair F1 at least 0.85 and no regression larger than 2 points at zero noise.
- Stop condition: Stop if extraction pair F1 is below 0.70 or retrieval fails to beat the best non-oracle baseline by at least 3 points at moderate metadata noise.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-metadata-extraction-for-repeated-agent-memory-baseli-9ef84479b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
