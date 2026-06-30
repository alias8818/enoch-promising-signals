# Extreme INT4 Quantization with Principled Residual Channel Preservation for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-for-gb10-44575b9b73aa`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-for-gb10-44575b9b73aa-20260609T060635273611+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b4f39773704c

## What looked useful

Residual channel preservation is a real error-reduction mechanism in these bounded tests: synthetic 2% scored residual rows cut mean output MSE by about 56% while random rows cut about 2%; on Pythia-70M hidden layers, 2% activation-aware residual rows reduced logits MSE from 106.19 to 64.66 versus fp16. Selector novelty is mixed because activation-aware scoring did not beat simpler quant-error scoring on synthetic layers and was not consistently best on tiny-model loss.

## Boundaries and scale limits

No packed INT4 kernel, no standard corpus perplexity benchmark, no GPT-2-small-class full validation, no 1B+ model validation, and no production serving throughput or memory-pressure test. The Pythia probe used 8 calibration and 8 eval snippets with embeddings and lm_head left fp16.

## Claim scope

On synthetic transformer-like linear layers and a tiny cached Pythia-70M probe, preserving a small scored set of fp16 output rows while quantizing remaining hidden linear weights to per-row INT4 reduces output/logit reconstruction error versus all-INT4 and random residual rows at about 4.24-4.48 effective weight bits, excluding scale metadata.

## Why it stopped

This run produced a reproducible useful signal but not publication-grade evidence; the result is bounded by synthetic reconstruction tests, a tiny pretrained-model probe, and no packed GB10 INT4 throughput validation.

## Recommended next action

Run a bounded real-corpus Pythia-70M/160M or GPT-2-small-class evaluation against matched GPTQ/AWQ-style baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus residual INT4 channel preservation against matched quantization baselines
- Success threshold: At 2-4% residual rows, activation-aware preservation must reduce perplexity degradation by at least 10% relative to row quant-error preservation at the same effective bit budget and must not erase expected INT4 memory benefits.
- Stop condition: Stop if activation-aware selection is within noise of row quant-error selection on perplexity/logits MSE or if residual handling removes practical GB10 memory/latency advantages.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-for-gb10-44575b9b73aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
