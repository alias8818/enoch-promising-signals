# Low-rank KV cache compression on small LMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-cache-compression-on-small-lms-4bbdd38377f6`
Run ID: `low-rank-kv-cache-compression-on-small-lms-4bbdd38377f6-20260614T011401319988+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a89d19a40a

## What looked useful

Learned low-rank KV bases show exploitable structure on GPT-2: on WikiText-2, rank 16 uses 25% of the per-token hidden dimension and achieved mean attention-output rel-L2 0.0964 and mean cosine 0.9822, versus random-basis rel-L2 0.8852. However, max rel-L2 remained 0.5469 at rank 16, and value reconstruction error was much higher than key reconstruction error.

## Boundaries and scale limits

This run used attention-output reconstruction only, not an actual compressed generation cache. It used GPT-2 at sequence length 128 with 1,877 held-out non-pad WikiText-2 tokens; it did not measure perplexity, task accuracy, long-context latency, memory pressure, quantization, or larger LMs.

## Claim scope

On GPT-2 small with 48 WikiText-2 calibration rows and 24 held-out validation rows, fixed per-layer/per-head low-rank K/V bases preserve average causal attention outputs much better than random bases, but aggressive ranks still have high worst-case layer distortion.

## Why it stopped

The result is a bounded mechanism/proxy evaluation, not full validation; prior work already covers low-rank KV compression with stronger end-to-end evidence, and this run lacks direct perplexity/latency/memory measurements.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded compressed-generation implementation that reports WikiText-2 perplexity, generated-token latency, and measured KV memory against baseline cache and at least one published low-rank method.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct compressed-generation evaluation for GPT-2 low-rank KV bases
- Success threshold: At least 2x measured KV memory reduction with WikiText-2 perplexity degradation under 5%, generated-token latency regression under 10%, and no layer with sustained attention-output rel-L2 above 0.25 on the validation sample.
- Stop condition: Stop if the compressed-cache implementation cannot beat random-basis quality, exceeds 5% perplexity degradation at 2x memory reduction, or requires custom kernels/long runs outside this worker's bounded budget.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-cache-compression-on-small-lms-4bbdd38377f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
