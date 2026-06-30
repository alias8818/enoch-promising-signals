# Activation and Perplexity Validation for Norm-Ranked 2-bit Residual Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-and-perplexity-validation-for-norm-ranked-2-bit-0efdb6b2fd`
Run ID: `activation-and-perplexity-validation-for-norm-ranked-2-bit-0efdb6b2fd-20260527T163141419109+0000`

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

- Parent run decision: Norm-Based Channel Ranking for Calibration-Free 2-bit Residual Quantization: enoch://control-plane/projects/norm-based-channel-ranking-for-calibration-free-2-bit-residual-quantization-2a27d8efe630/runs/norm-based-channel-ranking-for-calibration-free-2-bit-residual-quantization-2a27d8efe630-20260527T112643255818+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cb48439439d2

## What looked useful

Weight-norm ranking supported the activation-reconstruction mechanism but failed the direct perplexity criterion; activation MSE improvement alone was not predictive of language-model loss, and the bottom-norm control had the best quantized NLL.

## Boundaries and scale limits

Single small GPT-2 model, one WikiText-2 validation slice, one residual fraction, no training-time test, no larger-model replication, no storage-accounted residual encoding, and no production quantization kernel.

## Claim scope

On cached GPT-2 FP16 evaluated over the first 16,384 WikiText-2 validation tokens, simulated restoration of the top 5% output channels by weight norm after symmetric 2-bit projection quantization greatly reduced activation reconstruction error but worsened next-token NLL versus uniform 2-bit and matched random residual controls.

## Why it stopped

Tier 1 direct GPT-2/WikiText-2 test falsified the joint activation-plus-perplexity threshold for simple top-weight-norm residual selection: activation error improved, but NLL was worse than uniform and random controls.

## Recommended next action

Stop this norm-top residual rule as no-paper evidence; next bounded test should evaluate activation-aware or loss-aware residual ranking against the same random, bottom-norm, and uniform controls.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Activation-aware residual ranking for 2-bit GPT projection quantization
- Success threshold: Activation-aware or loss-aware 5% residual selection must reduce NLL by at least 10% relative to uniform 2-bit and beat the mean of three random residual controls while keeping mean activation relative MSE below the random-control mean.
- Stop condition: Stop if activation-aware or loss-aware ranking fails to beat either uniform 2-bit or random-control mean NLL on the same 16,384-token GPT-2/WikiText-2 validation harness.

## Evidence references

- Artifact root: `<local-path>/projects/activation-and-perplexity-validation-for-norm-ranked-2-bit-0efdb6b2fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
