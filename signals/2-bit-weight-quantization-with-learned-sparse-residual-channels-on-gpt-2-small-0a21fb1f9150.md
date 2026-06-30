# 2-bit weight quantization with learned sparse residual channels on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-learned-sparse-residual-channels-on-gpt-2-small-0a21fb1f9150`
Run ID: `2-bit-weight-quantization-with-learned-sparse-residual-channels-on-gpt-2-small-0a21fb1f9150-20260611T201613193055+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/083e54a74394

## What looked useful

Sparse learned residual channels are effective at reconstructing selected high-error channels, with 80.7% mean selected-channel MSE reduction in the all-layer expanded run, but model loss stayed high: original 3.8156, uniform 2-bit 35.9409, residual 19.3201.

## Boundaries and scale limits

Evaluated on short 128-token blocks and small streamed WikiText-2 samples; residuals were fitted from 4096 activation rows per module; quantizer was simple uniform min/max rather than activation-aware GPTQ/AWQ-style optimization; no full benchmark perplexity or downstream evaluation.

## Claim scope

On GPT-2-small with short WikiText-2 held-out blocks, uniform per-output-channel 2-bit quantization of all Conv1D weights plus learned low-rank sparse residual channels recovers selected activation-space quantization error and about half of the language-loss gap, but remains far from original model loss.

## Why it stopped

Bounded direct GPT-2-small evidence shows mechanism-level recovery but not practical model quality; this is an early negative result for simple uniform 2-bit quantization plus sparse residual channels, not a full validation or full rejection of stronger quantizers.

## Recommended next action

Stop this simple uniform-2bit formulation as no-paper evidence; a bounded follow-up should test the same sparse residual budget with an activation-aware 2-bit quantizer and an equal-parameter dense low-rank residual control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware 2-bit quantization with sparse residual-channel controls on GPT-2-small
- Success threshold: 2-bit plus sparse residual channels recover at least 80% of the activation-aware quantization loss gap and beat the equal-parameter dense low-rank residual control by at least 10% of the remaining loss gap on held-out validation.
- Stop condition: Stop if activation-aware 2-bit plus sparse residual remains more than 25% worse than original validation loss or does not outperform the equal-parameter dense residual control.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-learned-sparse-residual-channels-on-gpt-2-small-0a21fb1f9150`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
