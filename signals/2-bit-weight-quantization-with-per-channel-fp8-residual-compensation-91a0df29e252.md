# 2-bit Weight Quantization with Per-Channel FP8 Residual Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-per-channel-fp8-residual-compensation-91a0df29e252`
Run ID: `2-bit-weight-quantization-with-per-channel-fp8-residual-compensation-91a0df29e252-20260609T100250809397+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58d8e0541c11

## What looked useful

Dense residual compensation works mechanically at about 10 bits/weight, but sparse FP8 residual compensation at about 4.27 bits/weight had 0.5249 mean output relative MSE versus 0.0642 for int4 at about 4.02 bits/weight; even 25% residual density at about 6.52 bits/weight remained worse than int4.

## Boundaries and scale limits

No real pretrained language-model weights, perplexity evaluation, packed kernel throughput, NF4 baseline, or fine-tuning recovery were tested. Medium run covered 512x512 to 2048x2048 synthetic matrices across normal, Laplace, and outlier distributions with three seeds.

## Claim scope

Synthetic CUDA/PyTorch linear-layer probes show that dense per-channel FP8 residuals can nearly reconstruct 2-bit-quantized weights, but storage-aware sparse FP8 residual compensation is much less accurate than int4 at comparable effective bits per weight.

## Why it stopped

Synthetic storage-aware probe falsified the practical version of the hypothesis: sparse per-channel FP8 residual compensation did not beat int4 at comparable or even higher effective storage, while dense residual compensation removed the 2-bit compression advantage.

## Recommended next action

Stop this run as an early no-paper useful signal; only continue via a bounded real-weight follow-up comparing storage-matched FP8 residual compensation against int4/NF4 on GPT-2-small layer weights.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-matched FP8 residual compensation on real GPT-2-small weights
- Success threshold: At matched effective bits near 4 bits/weight, FP8 residual compensation must reduce mean layer output relative MSE by at least 20% versus int4/NF4 on real pretrained layers without relying on dense residual storage.
- Stop condition: Stop if storage-matched FP8 residual compensation is worse than int4/NF4 on mean layer output relative MSE across GPT-2-small attention and MLP projections, or if index/kernel overhead pushes the method above the matched bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-per-channel-fp8-residual-compensation-91a0df29e252`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
