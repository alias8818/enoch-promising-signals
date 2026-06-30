# 1-bit Weight Quantization with Binary Residual Adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-bit-weight-quantization-with-binary-residual-adapters-63adb3dd6712`
Run ID: `1-bit-weight-quantization-with-binary-residual-adapters-63adb3dd6712-20260621T234458695374+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

Dense mean test accuracy was 0.9748, frozen 1-bit accuracy was 0.8980, and the best binary residual adapter reached 0.9793 mean test accuracy, slightly above the best float LoRA control at 0.9760.

## Boundaries and scale limits

Only a NumPy MLP on synthetic data was tested; no transformer, GPT-2-small, language modeling perplexity, packed kernels, real calibration data, or large-scale training was evaluated.

## Claim scope

On a synthetic two-moons MLP proxy, low-rank binary residual adapters trained on frozen 1-bit post-training quantized weights recovered the dense-vs-1-bit accuracy gap across three seeds.

## Why it stopped

Stopped after a proxy mechanism confirmation because the evidence is synthetic and insufficient for a paper or broad quantization claim.

## Recommended next action

Run a bounded GPT-2-small-class or tiny-transformer language-model follow-up comparing dense, frozen 1-bit, float LoRA, and binary residual adapters on validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer perplexity probe for 1-bit weights with binary residual adapters
- Success threshold: Binary residual adapters recover at least 50% of the frozen 1-bit perplexity degradation versus dense and are within 5% relative perplexity of the float LoRA control at a lower bit-storage budget.
- Stop condition: Stop if binary residual adapters recover less than 25% of the 1-bit perplexity degradation at all tested ranks or are consistently worse than float LoRA without a storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weight-quantization-with-binary-residual-adapters-63adb3dd6712`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
