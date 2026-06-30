# GPT-2-small shard watermark survival under realistic fine-tuning and evasion controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-shard-watermark-survival-under-realistic-fine-9a0ba3c7db`
Run ID: `gpt-2-small-shard-watermark-survival-under-realistic-fine-9a0ba3c7db-20260620T005402747930+0000`

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

- Parent run decision: Embedded Shard Watermarks for Free-Rider Detection in Volunteer Training: enoch://control-plane/projects/embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89/runs/embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89-20260620T003112160616+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

The detector margin stayed essentially unchanged: implanted z=12.8000, after fine-tuning z=12.7992, after noise z=12.7998, after noise plus 8-bit quantization z=12.7946, while the unwatermarked fine-tuned control was z=-0.0006.

## Boundaries and scale limits

One model checkpoint, one seed, one shard, one implant strength, 12 CPU fine-tuning steps, small local text corpus, tiny eval set, and simple non-adaptive evasion controls only. No multi-epoch public downstream fine-tune, no multiple seeds, no adaptive removal, no pruning/merging attacks, no generated-text watermark test, and no publication-grade utility evaluation.

## Claim scope

In a single-seed Tier 1 direct test, a keyed additive watermark implanted into 65,536 entries of GPT-2-small tensor transformer.h.0.mlp.c_fc.weight at 0.05 tensor standard deviations remained detectable after 12 full-model next-token fine-tuning steps on a small local corpus, and after simple additive noise plus 8-bit quantize/dequantize controls; an unwatermarked fine-tuned control stayed near zero detector score.

## Why it stopped

Closed as no-paper useful signal: the mechanism survived the required small direct test, but the evidence is too narrow and short-run for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with multiple seeds, longer GPT-2-small fine-tuning on a public corpus such as Wikitext-2, held-out perplexity, varied shards/strengths, and stronger adaptive evasion controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed GPT-2-small shard watermark survival under longer public-corpus fine-tuning
- Success threshold: Across all seeds, watermarked models retain detector z-score > 5 after fine-tuning and controls, unwatermarked controls remain |z| < 5, and held-out loss degradation from implant remains below 1 percent relative to the unwatermarked run.
- Stop condition: Stop if any public-corpus fine-tuned watermarked seed falls below z-score 5 while matched controls and logs show the run completed correctly, or if implant utility cost exceeds the stated loss tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-shard-watermark-survival-under-realistic-fine-9a0ba3c7db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
