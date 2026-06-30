# Blockwise 8-bit AdamW CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adamw-cpu-training-a380e8ca719b`
Run ID: `blockwise-8-bit-adamw-cpu-training-a380e8ca719b-20260529T123420492119+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c79b9e0aa0fd

## What looked useful

Persistent optimizer state fell to about 25% of fp32 AdamW state, but CPU steps were 1.6-2.7x slower and the quantized optimizer diverged at lr=3e-3 where AdamW32 converged; lower learning rates tracked AdamW32 but remained slower.

## Boundaries and scale limits

Not tested on neural networks, language models, production fused CPU kernels, or memory-capacity-limited large models; temporary dequantized arrays mean RSS does not capture an optimized implementation's possible peak-memory behavior.

## Claim scope

Bounded CPU/NumPy evidence for a naive blockwise 8-bit AdamW-style optimizer on optimizer-only vectors up to 4M parameters and synthetic linear regression with 393,216 parameters.

## Why it stopped

Proxy/local CPU evidence shows useful memory compression but early falsifies the drop-in practical-training claim for this naive blockwise 8-bit AdamW: slower CPU updates and divergence at an AdamW32-stable learning rate.

## Recommended next action

Stop this naive design as no-paper evidence; a bounded follow-up should test a stabilized second-moment quantizer or fused CPU update before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized blockwise 8-bit AdamW second-moment quantization on CPU
- Success threshold: At lr=3e-3, final linear-regression loss within 10% of AdamW32 after 120 steps, no divergence across three seeds, and persistent state <=35% of AdamW32; throughput penalty <=25% unless a memory-capacity win is directly demonstrated.
- Stop condition: Stop if the stabilized quantizer still diverges at lr=3e-3, needs lr reduction relative to AdamW32, or remains more than 50% slower without a direct memory-capacity benefit.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adamw-cpu-training-a380e8ca719b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
