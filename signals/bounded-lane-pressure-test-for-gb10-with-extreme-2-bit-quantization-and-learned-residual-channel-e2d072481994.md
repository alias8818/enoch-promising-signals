# Bounded lane-pressure test for gb10 with extreme 2-bit quantization and learned residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-lane-pressure-test-for-gb10-with-extreme-2-bit-quantization-and-learned-residual-channel-e2d072481994`
Run ID: `bounded-lane-pressure-test-for-gb10-with-extreme-2-bit-quantization-and-learned-residual-channel-e2d072481994-20260628T024632243172+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a959f9b7cbe6

## What looked useful

Rank 64 residual channels added a 6.25% residual parameter/FLOP ratio and raised theoretical storage to 3.0 bits/parameter, but reduced 2-bit output RMSE by only 5.79%, leaving relative RMSE 0.4754. Rank 512 reduced RMSE by 38.61%, but required 50% residual parameter/FLOP ratio and 10.0 theoretical bits/parameter.

## Boundaries and scale limits

This is a bounded proxy: it does not test packed INT2 kernels, real pretrained transformer weights, activation-aware residual training, or end-to-end language-model perplexity. Runtime uses PyTorch FP16 matmuls and measures residual-path overhead rather than fused 2-bit deployment speed.

## Claim scope

On synthetic 2048x2048 transformer-like linear projections on GB10, groupwise 2-bit dequantized weights plus best-rank SVD residual channels improve output reconstruction monotonically, but small residual budgets do not recover enough error to support practical low-lane-pressure viability.

## Why it stopped

Proxy evidence only: direct synthetic linear reconstruction on GB10 shows small learned residual channels help too little at near-2-bit budgets, so this is not a full validation and not paper-ready.

## Recommended next action

Stop this run as a proxy early falsification; the one useful next test is a direct pretrained GPT-2-small layer study with activation-aware learned residual channels and a measured GB10 latency/control baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 layer residual-channel test for near-2-bit quantization
- Success threshold: At rank <=64 and <=3.0 theoretical bits/parameter, reduce 2-bit-only output RMSE or loss degradation by at least 25% while keeping measured residual-path latency overhead <=20% versus the quantized/control path.
- Stop condition: Stop if rank 64 improves RMSE by less than 15% on two representative pretrained layers or if latency overhead exceeds 35% before reaching the error threshold.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-lane-pressure-test-for-gb10-with-extreme-2-bit-quantization-and-learned-residual-channel`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
