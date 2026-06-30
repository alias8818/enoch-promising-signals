# Small-transformer residual-channel pruning before quantization on real text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-residual-channel-pruning-before-quantiza-bb2cf08a19`
Run ID: `small-transformer-residual-channel-pruning-before-quantiza-bb2cf08a19-20260607T033845460052+0000`

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

- Parent run decision: Residual Channel Pruning Before Quantization for Extreme Compression: enoch://control-plane/projects/residual-channel-pruning-before-quantization-for-extreme-compression-cd3077aadb56/runs/residual-channel-pruning-before-quantization-for-extreme-compression-cd3077aadb56-20260605T230425187795+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/98b36175dbbe

## What looked useful

Low-RMS residual channels appear genuinely lower utility than random channels, and pruning them can partially rescue a severely degraded 4-bit quantized model in this small direct test. The same intervention is not beneficial for dense FP32 or 8-bit quantized models, so the broad pruning-before-quantization hypothesis remains mixed and not paper-ready.

## Boundaries and scale limits

Single pretrained small model, one real-text validation slice, one activation-ranking seed, three random masks per sparsity, functional channel zeroing rather than structural pruning, and simulated dequantized weight quantization rather than production int kernels.

## Claim scope

On distilgpt2 evaluated on a 4064-token WikiText-2 validation slice, activation-low-RMS residual-channel pruning before simulated symmetric weight quantization consistently selected less damaging channels than random pruning; it improved severe 4-bit quantized loss versus dense 4-bit but worsened FP32 and 8-bit loss versus their dense baselines.

## Why it stopped

Tier 1 direct test produced a useful but mixed no-paper signal: 4-bit simulated quantization improved with activation-ranked pruning, while FP32 and 8-bit dense baselines were worsened by pruning.

## Recommended next action

Run a medium confirmation on GPT-2-small or two small pretrained LMs with at least 10x more held-out real-text tokens, production-like int4 quantization, and structural channel-removal checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of low-RMS residual pruning for int4 quantized small transformers
- Success threshold: At 10-30% residual-channel pruning, activation-ranked int4 pruning improves loss versus dense int4 by at least 0.20 on average and beats the random-pruned int4 mean by at least 0.20, while FP32 prune-only loss degradation remains clearly reported.
- Stop condition: Stop if activation-ranked int4 pruning fails to beat dense int4 or random-pruned int4 on the larger real-text evaluation, or if structural pruning does not reproduce hook-mask behavior within 0.05 loss.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-residual-channel-pruning-before-quantiza-bb2cf08a19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
