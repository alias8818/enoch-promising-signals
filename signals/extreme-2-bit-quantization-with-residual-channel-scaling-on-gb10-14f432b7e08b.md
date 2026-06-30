# Extreme 2-bit quantization with residual channel scaling on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-2-bit-quantization-with-residual-channel-scaling-on-gb10-14f432b7e08b`
Run ID: `extreme-2-bit-quantization-with-residual-channel-scaling-on-gb10-14f432b7e08b-20260611T160629683632+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f0ba224577ac

## What looked useful

RCS beta 1.0 reduced loss from 26.0233 to 24.1350 versus naive 2-bit quantization and reduced PPL ratio to 0.1513 of the naive 2-bit baseline, but fp16 loss was 4.5872/PPL 98.2 while RCS PPL remained 3.03e10. Layer-local diagnostics were weak: fixed beta 0.5 improved only 1/24 modules and oracle beta improved 4/24 modules.

## Boundaries and scale limits

Only distilgpt2, 4096 eval tokens, no packed 2-bit kernels, no training-aware quantization, no GPT-2-small/full-corpus validation, and no publication-grade perplexity run.

## Claim scope

On a bounded distilgpt2/Wikitext-2 proxy, calibration-derived residual channel scaling can reduce loss relative to naive 2-bit affine post-training quantization, but it does not preserve useful language-model quality.

## Why it stopped

Proxy early falsification: the method gives a measurable relative improvement over a collapsed 2-bit baseline but remains far from fp16 quality and lacks stable layer-local support.

## Recommended next action

Stop this simple fixed residual-channel-scaling variant as a paper claim; only pursue a bounded follow-up if scales are learned or selected per layer against calibration output error without eval leakage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned per-layer residual channel scales for 2-bit GPT-2 proxy quantization
- Success threshold: On the same bounded proxy, learned/per-layer RCS must achieve PPL <= 982 while improving at least two thirds of quantized modules relative to naive 2-bit.
- Stop condition: Stop if learned/per-layer scaling still leaves PPL above 10x fp16 or improves fewer than 16 of 24 modules.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-2-bit-quantization-with-residual-channel-scaling-on-gb10-14f432b7e08b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
