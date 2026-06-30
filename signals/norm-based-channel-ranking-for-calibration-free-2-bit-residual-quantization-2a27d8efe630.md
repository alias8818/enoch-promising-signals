# Norm-Based Channel Ranking for Calibration-Free 2-bit Residual Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `norm-based-channel-ranking-for-calibration-free-2-bit-residual-quantization-2a27d8efe630`
Run ID: `norm-based-channel-ranking-for-calibration-free-2-bit-residual-quantization-2a27d8efe630-20260527T112643255818+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cb48439439d2

## What looked useful

At a 12.5% residual-channel budget, norm_top recovered 36.2% of all-channel residual gain on distilgpt2 and 33.9% on gpt2, versus 12.5% and 12.3% for random_mean. The policy remained below the residual-error oracle, which recovered 48.6% and 46.5%, so norm is useful but not optimal.

## Boundaries and scale limits

Evidence is limited to weight reconstruction on distilgpt2 and gpt2 matrices, plus synthetic smoke controls. It does not include activation MSE, perplexity, generation quality, packed 2-bit kernels, non-GPT architectures, or larger LLMs.

## Claim scope

For GPT-2-family public weight matrices under a simulated per-output-channel symmetric 2-bit residual quantizer, selecting the highest weight-norm output channels for a limited residual pass recovers substantially more weight-reconstruction gain than random or bottom-norm channel selection.

## Why it stopped

No-paper closure: this run produced bounded weight-reconstruction evidence only, not direct end-to-end model-quality validation.

## Recommended next action

Run a bounded direct-evidence follow-up measuring activation-output MSE and perplexity for full quantized GPT-2-family models while keeping channel ranking calibration-free.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation and Perplexity Validation for Norm-Ranked 2-bit Residual Quantization
- Success threshold: At 12.5% residual-channel budget, norm_top must improve activation-output MSE and perplexity versus random_mean on the same quantized model, and recover at least half of the oracle's activation-MSE gain.
- Stop condition: Stop as negative if norm_top fails to beat random_mean on activation-output MSE or perplexity at matched budget on the first public GPT-2-family model.

## Evidence references

- Artifact root: `<local-path>/projects/norm-based-channel-ranking-for-calibration-free-2-bit-residual-quantization-2a27d8efe630`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
