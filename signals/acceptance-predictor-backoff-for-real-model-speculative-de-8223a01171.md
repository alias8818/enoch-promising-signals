# Acceptance-predictor backoff for real-model speculative decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `acceptance-predictor-backoff-for-real-model-speculative-de-8223a01171`
Run ID: `acceptance-predictor-backoff-for-real-model-speculative-de-8223a01171-20260520T024657215997+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Calibrated high-gamma entropy backoff for speculative decoding: enoch://control-plane/projects/calibrated-high-gamma-entropy-backoff-for-speculative-deco-b83b49f20e/runs/calibrated-high-gamma-entropy-backoff-for-speculative-deco-b83b49f20e-20260520T023627339239+0000
- Parent run decision: Real-model entropy and acceptance controller probe for speculative decoding: enoch://control-plane/projects/real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc/runs/real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc-20260520T023107177553+0000

## What looked useful

The predictor filtered for higher acceptance-rate blocks, but the throughput cost of one draft probe on many backed-off steps dominated. With GPT-2/distilGPT-2 block size 4, always-speculate reached 207.30 tok/s versus target-only 203.80 tok/s, while the best nonzero predictor threshold reached only 136.69 tok/s. With block size 8, target-only was 201.66 tok/s, always-speculate 168.41 tok/s, and the best nonzero predictor threshold 146.43 tok/s. With GPT-2-medium/GPT-2, always-speculate was beneficial at 132.23 tok/s versus target-only 96.67 tok/s, but the best nonzero predictor threshold was 109.35 tok/s.

## Boundaries and scale limits

Evaluation used small GPT-2-class Hugging Face models, fixed prompts, greedy decoding, and a simple non-trained predictor. It did not test stochastic sampling, KV-cache-optimized serving kernels, trained hidden-state predictors, 7B-class models, or production inference servers.

## Claim scope

For deterministic greedy speculative decoding on GPT-2/distilGPT-2 and GPT-2-medium/GPT-2 pairs on this GB10 host, a first-draft-confidence plus rolling-acceptance backoff predictor did not improve throughput over target-only or always-speculate baselines.

## Why it stopped

Direct real-model validation produced a useful negative signal: the tested acceptance-predictor backoff design improved acceptance rate in some settings but reduced end-to-end throughput versus real baselines.

## Recommended next action

Stop this implementation path; only revisit backoff if a zero-probe or trained predictor can avoid per-token draft-probe overhead and beat always-speculate by at least 5% on the same direct metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Zero-probe acceptance backoff for speculative decoding
- Success threshold: At least 5% higher tokens/sec than always-speculate on GPT-2-medium/GPT-2 with zero output mismatches, and no worse than target-only on GPT-2/distilGPT-2 block-size stress cases.
- Stop condition: Stop if the predictor requires a per-token draft probe during backed-off spans or fails to beat always-speculate by 5% on the larger-target direct benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/acceptance-predictor-backoff-for-real-model-speculative-de-8223a01171`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
