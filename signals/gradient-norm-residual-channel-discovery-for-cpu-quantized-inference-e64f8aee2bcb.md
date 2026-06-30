# Gradient-Norm Residual Channel Discovery for CPU Quantized Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-residual-channel-discovery-for-cpu-quantized-inference-e64f8aee2bcb`
Run ID: `gradient-norm-residual-channel-discovery-for-cpu-quantized-inference-e64f8aee2bcb-20260602T113043713153+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03d2b34b4c60

## What looked useful

Gradient-norm channel scores carry usable correction signal, averaging 21.3% logit-MSE reduction versus 14.4% for random, but weight-norm averaged 22.9% and won 16 of 45 groups versus 4 for gradient-norm; the novelty claim is therefore not supported in this bounded test.

## Boundaries and scale limits

Five seeds, synthetic classification data, one-hidden-layer MLPs, simulated 3/4/8-bit dequantized arithmetic, and no production CPU kernel or transformer residual-stream validation.

## Claim scope

In a NumPy synthetic-teacher MLP proxy for CPU quantized inference, gradient-norm residual channel selection improves mixed-precision residual correction over random and activation-norm selection but does not beat a simple output-weight-norm baseline.

## Why it stopped

Bounded proxy early falsification of the stronger practical-superiority claim: gradient-norm selection worked better than weak baselines but underperformed the cheap weight-norm baseline, so this is not publication-grade positive evidence.

## Recommended next action

Stop as no-paper useful-signal evidence; only reopen with a bounded transformer residual-stream test that includes weight-norm and quant-error baselines at matched retained-channel budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer residual-stream gradient channels versus weight-norm baseline
- Success threshold: Gradient-based selection must improve validation loss or perplexity by at least 10% relative to weight-norm's quantization degradation recovery at two retained-channel budgets without worse CPU latency overhead.
- Stop condition: Stop if weight-norm matches or beats gradient-based selection on the primary validation metric for two budgets or if residual correction overhead dominates the quantized inference path.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-residual-channel-discovery-for-cpu-quantized-inference-e64f8aee2bcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
