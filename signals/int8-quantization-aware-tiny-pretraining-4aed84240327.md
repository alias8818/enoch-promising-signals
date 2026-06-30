# INT8 Quantization-Aware Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-quantization-aware-tiny-pretraining-4aed84240327`
Run ID: `int8-quantization-aware-tiny-pretraining-4aed84240327-20260605T035514381529+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

INT8-QAT fake quant did not collapse tiny pretraining convergence: mean final validation loss was 4.631882 vs 4.631835 for FP32, with nearly identical loss improvement, but training throughput was only 0.7159x FP32.

## Boundaries and scale limits

Synthetic token process only; 4-layer tiny transformer only; 400 steps; no real text corpus; no GPT-2-small-class scale; fake quantization only; no converted INT8 inference engine or deployment kernel benchmark.

## Claim scope

On a 4-layer tiny causal LM trained for 400 GPU steps over a synthetic held-out pretraining process, symmetric INT8 fake-quantization-aware training of linear weights, biases, embeddings/activation boundaries, and the LM head matched FP32 validation loss movement across 3 seeds without instability.

## Why it stopped

The result is a bounded synthetic proxy showing mechanism viability, not direct or broad enough for a paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should repeat the matched QAT-vs-FP design on a real-token corpus with converted INT8 evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token tiny LM INT8-QAT with post-conversion evaluation
- Success threshold: INT8-QAT final validation perplexity within 1% of FP32, no seed diverges, and converted INT8 evaluation loss within 2% of fake-quant evaluation loss.
- Stop condition: Stop if INT8-QAT is worse than FP32 by more than 3% validation perplexity in at least 2 of 3 seeds or converted INT8 evaluation loses more than 5% perplexity versus fake quant.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-aware-tiny-pretraining-4aed84240327`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
