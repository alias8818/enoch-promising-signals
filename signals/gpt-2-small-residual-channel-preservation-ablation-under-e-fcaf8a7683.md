# GPT-2-small residual-channel preservation ablation under extreme activation quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-residual-channel-preservation-ablation-under-e-fcaf8a7683`
Run ID: `gpt-2-small-residual-channel-preservation-ablation-under-e-fcaf8a7683-20260601T080900771361+0000`

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

- Parent run decision: Residual-Channel Preserving Extreme Quantization: enoch://control-plane/projects/residual-channel-preserving-extreme-quantization-049f27ff4ef0/runs/residual-channel-preserving-extreme-quantization-049f27ff4ef0-20260601T025441178977+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4ec8f6b79033

## What looked useful

Global residual-channel preservation by calibration RMS is not a robust Tier 1 win under extreme 2-bit activation quantization. Small k=32 and k=128 benefits beat random controls but remain far below the stated 5% threshold, and k=64 fails outright.

## Boundaries and scale limits

Small direct inference-only ablation; no retraining or fine-tuning; Wikitext-2 validation subset only; fake quantization rather than real integer kernels; global channel selection only; no per-layer/per-head/channel-routing selection; no large-corpus or long-context validation.

## Claim scope

On pretrained GPT-2-small evaluated on 32,768 Wikitext-2 validation tokens, preserving global top-RMS residual-stream channels during 2-bit fake activation quantization of transformer block outputs did not reach a 5% NLL reduction over uniform 2-bit quantization; k=32 and k=128 gave only about 1% relative NLL reductions, while k=64 was worse than uniform.

## Why it stopped

Controlled small direct test failed the predefined Tier 1 threshold; this is an early direct falsification of the global top-RMS preservation variant, not a full validation of all possible residual-channel preservation designs.

## Recommended next action

Stop this branch as no-paper useful signal; if continuing, run a bounded per-layer channel-preservation ablation with the same GPT-2-small/Wikitext-2 setup and require >=5% NLL reduction over uniform 2-bit plus random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-layer residual-channel preservation under 2-bit GPT-2-small activation quantization
- Success threshold: Per-layer top-k preservation must reduce mean NLL by at least 5% relative to uniform 2-bit quantization and outperform the mean random per-layer control on the same evaluated tokens.
- Stop condition: Stop if per-layer preservation remains below 5% relative NLL reduction, fails to beat random controls, or shows gains only by preserving a large fraction of channels that weakens the compression premise.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-residual-channel-preservation-ablation-under-e-fcaf8a7683`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
