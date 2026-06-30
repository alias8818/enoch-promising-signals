# INT2 RAM Draft Model for Home-Hardware Spec Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-ram-draft-model-for-home-hardware-spec-decoding-f4bad96361d8`
Run ID: `int2-ram-draft-model-for-home-hardware-spec-decoding-f4bad96361d8-20260620T055451214290+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b56f6cbef347

## What looked useful

INT2 compression can preserve diffuse synthetic distribution overlap, but top-1 agreement was only about 12.2%. In a sharper stress case, INT2 overlap fell to about 0.48. Packed INT2 streaming cost about 30 ms/token on the local CPU process, making modeled speculative decoding slower than baseline for 20 ms and 100 ms targets in the sharper case; pre-dequantized INT2 looked faster but weakens the compressed active-weight premise.

## Boundaries and scale limits

No real LLM target or trained draft was evaluated. The benchmark used synthetic logits, a quantized copy of the target matrix, one local CPU process, and assumed target-model latencies rather than measured home-GPU verification.

## Claim scope

CPU-only synthetic proxy for INT2 RAM-resident draft speculative decoding: rowwise INT2 quantization fidelity, packed-stream draft latency, and simple speedup model for a 4096 x 768 synthetic logit matrix.

## Why it stopped

Proxy evidence is mixed and partly unfavorable for the original INT2 RAM draft claim; it is not full validation and should not be treated as paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a real-model follow-up that measures trained or calibrated INT2 draft acceptance and end-to-end tokens/s against a local target model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model INT2 draft acceptance and packed-latency validation
- Success threshold: At least 1.25x end-to-end speedup over baseline target decoding on real text while preserving output-quality checks, with packed INT2 draft latency below the modeled break-even for the measured target latency.
- Stop condition: Stop if real-text INT2 acceptance is below 0.55, top-token fidelity remains near the synthetic 12% level, or packed draft latency keeps modeled speedup at or below 1.0x for the measured target latency.

## Evidence references

- Artifact root: `<local-path>/projects/int2-ram-draft-model-for-home-hardware-spec-decoding-f4bad96361d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
