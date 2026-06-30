# INT4 weight quantization with low-rank residual correction on GPT-2-small (CPU)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-weight-quantization-with-low-rank-residual-correction-on-gpt-2-small-cpu-5d3384d9b2bd`
Run ID: `int4-weight-quantization-with-low-rank-residual-correction-on-gpt-2-small-cpu-5d3384d9b2bd-20260619T193642265557+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aca463b9eee0

## What looked useful

Rank-16 residual correction reduced INT4 loss by 1.116869 on the built-in corpus and 1.230988 on the WikiText-2 slice, but remained 1.315924 and 1.983808 loss above dense FP32 respectively.

## Boundaries and scale limits

Only 1,024 tokens per corpus were evaluated; execution used dequantized FP32 weights; residual-factor storage, packed INT4 latency, embeddings/lm head quantization, larger benchmark suites, and model-family robustness were not tested.

## Claim scope

On GPT-2-small non-embedding 2D weights, symmetric per-row INT4 dequantization plus rank-4/8/16 low-rank residual correction improves short-slice causal LM loss versus raw INT4 on a built-in corpus and a WikiText-2 validation slice, but does not recover dense FP32 quality.

## Why it stopped

Bounded direct GPT-2-small evidence supports the residual-correction mechanism but shows a large remaining dense-quality gap and lacks practical compression/serving evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should include residual-factor storage accounting and a larger WikiText/LAMBADA-style evaluation slice before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-aware GPT-2-small INT4 low-rank residual benchmark
- Success threshold: At a residual rank whose total storage is at least 2x smaller than FP16, recover at least 75% of the raw INT4 loss regression versus dense FP32 on the larger evaluation.
- Stop condition: Stop if storage-aware residual ranks either exceed the compression budget or fail to recover at least half of the raw INT4 loss regression on the larger slice.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-quantization-with-low-rank-residual-correction-on-gpt-2-small-cpu-5d3384d9b2bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
