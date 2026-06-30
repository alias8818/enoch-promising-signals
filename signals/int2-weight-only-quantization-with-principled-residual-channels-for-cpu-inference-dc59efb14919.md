# INT2 weight-only quantization with principled residual channels for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weight-only-quantization-with-principled-residual-channels-for-cpu-inference-dc59efb14919`
Run ID: `int2-weight-only-quantization-with-principled-residual-channels-for-cpu-inference-dc59efb14919-20260614T125552081899+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/dba0ebcc1722

## What looked useful

Sensitivity-selected residual channels, scored by calibration activation magnitude times weight-column RMS, reduced INT2 relative output MSE by 43.7% at 1%, 59.8% at 2%, 72.8% at 4%, and 74.3% at 8% residual channels across three layer shapes. At 4%, sensitivity residuals had about 0.295x the error of random residual channels and estimated storage was about 22.3% of fp16.

## Boundaries and scale limits

No real LM checkpoint, tokenizer, perplexity evaluation, downstream task, or packed INT2 CPU kernel was tested. Dense dequantized NumPy matmul timings are not evidence of production CPU inference speedup.

## Claim scope

In a bounded NumPy probe on three synthetic transformer-shaped linear layers with heavy-tailed channel structure, INT2 groupwise weight quantization plus 1-8% sensitivity-selected fp16 residual input channels reduces layer output error substantially versus pure INT2 and random residual-channel controls while preserving an estimated roughly 4.5x storage reduction at 4% residual channels.

## Why it stopped

Closed as no-paper useful signal because this run directly tested layer-level quantization error but only proxied real-model quality and did not validate packed CPU inference acceleration.

## Recommended next action

Run a bounded real-checkpoint follow-up on GPT-2-small-class weights using real text calibration activations, perplexity drift, random/INT4 controls, and at least a minimal packed INT2 CPU timing path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small INT2 residual-channel perplexity and packed CPU timing probe
- Success threshold: At 2-4% residual channels, sensitivity residual INT2 should cut pure INT2 perplexity or output-loss degradation by at least 50%, beat random residual controls by at least 25%, stay below 30% of fp16 weight storage, and show non-negative latency or bandwidth benefit in a packed CPU path.
- Stop condition: Stop if sensitivity residuals fail to beat random residual controls on real checkpoint loss/perplexity, if storage exceeds 30% of fp16 at the needed quality point, or if packed CPU timing cannot match dense baseline latency within the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-only-quantization-with-principled-residual-channels-for-cpu-inference-dc59efb14919`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
