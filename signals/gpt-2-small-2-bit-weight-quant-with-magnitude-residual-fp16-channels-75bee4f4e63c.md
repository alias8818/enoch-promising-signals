# GPT-2 small 2-bit weight quant with magnitude-residual FP16 channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-2-bit-weight-quant-with-magnitude-residual-fp16-channels-75bee4f4e63c`
Run ID: `gpt-2-small-2-bit-weight-quant-with-magnitude-residual-fp16-channels-75bee4f4e63c-20260613T082122926426+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9001c3f006c4

## What looked useful

Magnitude-selected FP16 residual channels improve over random residual channels at equal 10% residual budget, but the quality remains far from usable: signed int2 plus 10% magnitude residual gives PPL 5317 versus 44 for FP16, and even 50% residual channels still gives PPL 3286.

## Boundaries and scale limits

Does not test quantization-aware fine-tuning, GPTQ/AWQ-style calibrated quantization, packed int2 kernels, activation quantization, larger corpora, downstream tasks, or latency/memory wins. Evidence is a bounded local GPT-2 small validation probe, not full publication-grade validation.

## Claim scope

Post-training GPT-2 small transformer-block weight quantization to 2-bit signed or affine per-output-channel formats with magnitude-selected FP16 residual output channels, evaluated on 128 WikiText-2 validation windows of 256 tokens.

## Why it stopped

Bounded direct evidence is a proxy/early falsification of the simple post-training 2-bit magnitude-residual channel idea, not a full validation of all possible trained or calibrated variants.

## Recommended next action

Stop this no-paper run; only revisit with a calibrated GPTQ/AWQ or quantization-aware-training follow-up that must beat the signed int2 10% residual result by at least 10x PPL ratio while preserving meaningful compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated 2-bit GPT-2 residual-channel quantization
- Success threshold: At <=4 effective bits per tested transformer weight, magnitude residual channels should achieve PPL ratio <=2x FP16 and improve loss by at least 0.5 versus matched random residual-channel control.
- Stop condition: Stop if calibrated or QAT residual-channel variants still exceed 5x FP16 PPL at <=4 effective bits, or if recovery requires residual fractions that erase meaningful compression.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-2-bit-weight-quant-with-magnitude-residual-fp16-channels-75bee4f4e63c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
