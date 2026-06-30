# INT8 Fake-Quantized Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-fake-quantized-tiny-pretraining-9c9002f1b922`
Run ID: `int8-fake-quantized-tiny-pretraining-9c9002f1b922-20260608T041710545549+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/51f62cf8b7b9

## What looked useful

Fake INT8 weight+activation pretraining was numerically stable and loss-matched a same-size full-precision control across three seeds, but the simulated quantization path was about 2.4% slower and used about 36.6 MB more CUDA allocation, so the useful claim is trainability rather than efficiency.

## Boundaries and scale limits

Synthetic corpus only; tiny model only; 500-step runs only; no GPT-2-small-class baseline; no natural-language data; no hardware INT8 training kernels; no long-run convergence or downstream evaluation.

## Claim scope

On a tiny 4-layer causal transformer trained for 500 steps on a reproducible synthetic Markov next-token task, symmetric fake INT8 quantization of linear weights and activations with straight-through rounding preserved final eval loss within 0.000104 of the full-precision control across three seeds.

## Why it stopped

Bounded local evidence supports the mechanism at tiny synthetic scale, but it is a proxy result and not a full validation of INT8 fake-quantized pretraining.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a real tokenized-corpus small-transformer comparison and quantization ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Small-Transformer Fake INT8 Pretraining Ablation
- Success threshold: Fake INT8 validation loss within 1% relative of full precision for at least two of three seeds, with no NaNs and no sustained gradient explosion.
- Stop condition: Stop early if fake INT8 shows NaNs, persistent gradient explosion, or more than 5% relative validation-loss degradation after the warmup/training budget where the full-precision control is learning.

## Evidence references

- Artifact root: `<local-path>/projects/int8-fake-quantized-tiny-pretraining-9c9002f1b922`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
