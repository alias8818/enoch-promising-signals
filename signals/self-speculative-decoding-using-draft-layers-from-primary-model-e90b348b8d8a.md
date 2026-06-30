# Self-speculative decoding using draft layers from primary model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-using-draft-layers-from-primary-model-e90b348b8d8a`
Run ID: `self-speculative-decoding-using-draft-layers-from-primary-model-e90b348b8d8a-20260608T201529549666+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/38c857bbbb9c

## What looked useful

Across distilgpt2 layers 2/3/4 and gpt2 layers 3/6/9, top-1 agreement ranged from 0.1059 to 0.3305 while draft/full cost ratios ranged from 0.4076 to 0.8580. Every modeled speculative configuration was slower than full greedy decoding; the best observed modeled speedup was 0.7857x for gpt2 layer 3/12.

## Boundaries and scale limits

Tested only distilgpt2 and gpt2, 20 short prompts, 236 scored next-token positions, CPU offline timing, and a modeled speculative throughput proxy rather than an optimized KV-cache serving implementation. Results do not cover learned early-exit heads, distributional sampling acceptance, GPU kernels, 1B+ models, or full end-to-end decoding latency.

## Claim scope

Raw intermediate layers from GPT-style primary models, projected through the model's own final layer norm and LM head, did not provide a useful greedy speculative draft signal on short real-text prompts for distilgpt2 or gpt2 under the measured CPU prefix/full forward cost model.

## Why it stopped

Proxy/direct-small-model evidence consistently showed modeled slowdown rather than speedup for raw primary-layer drafts; this is an early falsification of the raw mechanism, not a full-scale serving validation.

## Recommended next action

Stop the raw intermediate-LM-head drafting path as no-paper negative evidence; the only bounded salvage test worth running is a learned early-exit head or calibration head that must clear explicit break-even acceptance thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for self-speculative GPT-2 drafts
- Success threshold: At minimum, learned layer-3 agreement must exceed 0.41 or learned layer-6 agreement must exceed 0.58 on held-out prompts, and an end-to-end greedy decoder must show greater than 1.05x generated-token speedup with exact output equivalence.
- Stop condition: Stop if held-out learned-head agreement remains below the measured draft/full cost ratio for all tested layers or if end-to-end exact greedy decoding fails to exceed 1.0x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-using-draft-layers-from-primary-model-e90b348b8d8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
