# FP8 vs INT4 Post-Training Quantization Pareto on a Home-Trained 60M LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp8-vs-int4-post-training-quantization-pareto-on-a-home-trained-60m-lm-846c78e07086`
Run ID: `fp8-vs-int4-post-training-quantization-pareto-on-a-home-trained-60m-lm-846c78e07086-20260609T154918166369+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca73369961ca

## What looked useful

Embedding/output-head treatment dominates the practical Pareto point for this small GPT-style LM. Block-only FP8 had +0.0141 loss delta versus +0.3515 for INT4, but all-weight FP8 had +1.2028 and all-weight INT4 had +7.0445 loss delta.

## Boundaries and scale limits

Not a home-trained 60M checkpoint; public 70M proxy only. Evaluation used a small validation slice and simulated quantize/dequantize storage, not real FP8/INT4 inference kernels or latency/memory-residency measurements.

## Claim scope

Bounded proxy evidence on EleutherAI/pythia-70m-deduped over 32,768 Wikitext-2 validation tokens: scaled FP8 e4m3 transformer-block-only PTQ preserved loss much better than groupwise INT4, while naive all-weight PTQ including embeddings/output head was not viable.

## Why it stopped

Proxy-only early result: it directly tested a 70M public GPT-style LM and simulated PTQ, not the requested home-trained 60M LM with production low-bit kernels.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use an actual home-trained approximately 60M checkpoint and compare embedding-aware FP8/INT4 policies on its held-out validation set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding-aware PTQ Pareto on an actual home-trained 60M LM
- Success threshold: FP8 embedding-aware or block-only PTQ has loss delta <= 0.05 while reducing non-embedding weight storage by about 4x, and INT4 either reaches loss delta <= 0.20 with at least 6x quantized-weight compression or is clearly documented as lower-quality/higher-compression.
- Stop condition: Stop if all embedding-aware FP8 variants exceed +0.10 loss delta or if INT4 remains above +0.50 loss delta after one reasonable group-size/calibration ablation.

## Evidence references

- Artifact root: `<local-path>/projects/fp8-vs-int4-post-training-quantization-pareto-on-a-home-trained-60m-lm-846c78e07086`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
