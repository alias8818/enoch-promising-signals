# All-layer GPT-2 INT4 residual-channel preservation with perplexity validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c`
Run ID: `all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c-20260605T203225281143+0000`

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

- Parent run decision: Extreme INT4 Quantization with Principled Residual Channel Preservation in Feed-Forward Layers: enoch://control-plane/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742/runs/extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742-20260605T175255143897+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4ac61a90de1

## What looked useful

Naive all-layer INT4 raised GPT-2 small WikiText-2 PPL from 47.76 to 543,998. RCP at 2% residual channels reduced PPL to 853.00, and RCP at 4% reduced PPL to 70.54. Same-fraction random-channel controls remained catastrophic at roughly 538k-687k PPL, supporting the calibrated residual-channel mechanism.

## Boundaries and scale limits

Single model scale, one validation slice of 16,256 predicted tokens, one calibration seed/slice, fake dequantized INT4 weights rather than packed INT4 kernels, no latency or memory-throughput validation, no larger-model or multi-dataset robustness.

## Claim scope

GPT-2 small, WikiText-2 validation slice, fake symmetric weight-only INT4 applied to all Conv1D/Linear modules including the LM head; preserving calibrated high-activation residual-stream channels at 2-4% of residual dimensions sharply reduces perplexity damage versus naive all-layer INT4 and same-budget random-channel controls.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not publication-grade robustness or hardware-realistic INT4 evidence.

## Recommended next action

Run a bounded deepen validation across multiple calibration seeds and a larger validation token budget, adding GPT-2 medium if it fits, before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Seed-robust GPT-2 residual-channel INT4 preservation validation
- Success threshold: Median RCP 2-4% recovery >=90% of naive INT4 PPL delta, every RCP 4% run beats its random 4% control by at least 50% delta recovery, and FP-to-RCP PPL gap remains below 2x FP baseline on GPT-2 small.
- Stop condition: Stop as unsupported if RCP 4% fails to beat random 4% in two or more seeds, or if median RCP 4% PPL remains above 2x FP baseline despite recovering naive INT4 degradation.

## Evidence references

- Artifact root: `<local-path>/projects/all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
