# Real-corpus quality filtering for a tiny transformer under equal-token CPU pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-quality-filtering-for-a-tiny-transformer-under-e9df7dc4d2`
Run ID: `real-corpus-quality-filtering-for-a-tiny-transformer-under-e9df7dc4d2-20260530T050813691569+0000`

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

- Parent run decision: Quality-filtered tiny pretraining on CPU: enoch://control-plane/projects/quality-filtered-tiny-pretraining-on-cpu-638ab37768c9/runs/quality-filtered-tiny-pretraining-on-cpu-638ab37768c9-20260530T010847274843+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Quality-filtered training won 4/4 seeds with mean validation-loss delta unfiltered-minus-quality of 0.017006 nats and mean relative validation-loss reduction of 0.7227%, under equal parameter count and equal training-token consumption.

## Boundaries and scale limits

Only three books, one held-out validation source, character-level tokenization, hand-built quality heuristic, 116k-parameter model, 245760 consumed training tokens per seed, and four seeds. This does not establish broad web-corpus or production-scale pretraining behavior.

## Claim scope

In a Tier 1 CPU-only direct test on three Project Gutenberg books, a 116705-parameter character-level causal Transformer trained for 245760 equal consumed tokens had lower held-out validation loss with a deterministic quality-top paragraph filter than with an unfiltered training stream across seeds 11-14.

## Why it stopped

No-paper closure: bounded direct evidence supports the mechanism direction, but the effect is small and the setting is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen test on 20-50 mixed-domain public-domain or web-cleaned documents with a subword tokenizer, equal consumed token budget, and at least three held-out validation domains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-domain subword quality filtering under equal-token tiny-transformer pretraining
- Success threshold: Quality-filtered condition wins at least 4/5 seeds and reduces mean held-out validation loss by at least 0.5% relative to unfiltered across held-out domains.
- Stop condition: Stop if quality filtering fails to beat unfiltered mean validation loss by 0.5% or if wins are fewer than 4/5 seeds under matched tokens and parameters.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-quality-filtering-for-a-tiny-transformer-under-e9df7dc4d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
