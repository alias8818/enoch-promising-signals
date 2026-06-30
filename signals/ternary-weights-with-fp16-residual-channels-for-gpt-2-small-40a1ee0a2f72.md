# Ternary Weights with FP16 Residual Channels for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-fp16-residual-channels-for-gpt-2-small-40a1ee0a2f72`
Run ID: `ternary-weights-with-fp16-residual-channels-for-gpt-2-small-40a1ee0a2f72-20260523T025204622861+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

Targeted FP16 residual channels monotonically reduce ternary reconstruction error and perplexity damage, but quality remains far from dense: dense FP16 PPL 44.90; ternary-only PPL 30185.02; 6.25% residual PPL 7759.23; 12.5% residual PPL 5899.00; 25% residual PPL 2686.94; 50% residual PPL 846.93.

## Boundaries and scale limits

No quantization-aware fine-tuning or training-from-scratch was run; evaluation used one dataset slice and left embeddings, layer norms, positional embeddings, and the tied output head dense. Results do not rule out a trained ternary-plus-residual architecture.

## Claim scope

Post-training replacement of GPT-2-small transformer projection/MLP weights with per-output-channel ternary weights plus targeted FP16 residual output channels, evaluated on an 8192-token WikiText-2 raw test slice.

## Why it stopped

Proxy/early falsification for small-residual post-training ternarization: residual channels help, but even 50% FP16 residual channels remain 18.9x worse than dense perplexity on the direct GPT-2-small/WikiText-2 probe.

## Recommended next action

Stop this post-training path as no-paper evidence; the only bounded next test worth running is quantization-aware fine-tuning of the same residual-channel scheme against a dense and standard quantization baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware fine-tuning for GPT-2-small ternary weights with targeted FP16 residual channels
- Success threshold: At 12.5% or lower FP16 residual channels, validation perplexity is within 20% of dense FP16 and at least 2x better than quantization-aware ternary without residual channels under matched training budget.
- Stop condition: Stop if 12.5% residual quantization-aware fine-tuning remains more than 2x worse than dense perplexity after the planned budget or fails to beat the non-residual quantization-aware ternary baseline.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-fp16-residual-channels-for-gpt-2-small-40a1ee0a2f72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
