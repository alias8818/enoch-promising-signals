# 4-bit Block-wise Optimizer States for Tiny-VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-block-wise-optimizer-states-for-tiny-vram-66199d1202c0`
Run ID: `4-bit-block-wise-optimizer-states-for-tiny-vram-66199d1202c0-20260628T051902227683+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/bd7acb8f5843

## What looked useful

The useful mechanism signal is that 4-bit block-wise persistent Adam states are not automatically hopeless, but denominator guarding is essential. Standard eps=1e-8 produced NaNs and near-random accuracy, while eps=1e-4 preserved accuracy on the bounded proxy with 7.39x lower persistent state storage.

## Boundaries and scale limits

Small synthetic 2D spiral task only; no transformer, language-model corpus, real tiny-VRAM memory pressure, fused CUDA/Triton kernel, distributed training, or long-run stability test. Python implementation was much slower than Adam.

## Claim scope

Bounded synthetic TinyMLP evidence: packed 4-bit block-wise Adam states with an epsilon guard matched full Adam held-out accuracy over 3 seeds and 500 steps while reducing persistent optimizer-state bytes by 7.39x; naive 4-bit Adam with standard eps diverged.

## Why it stopped

No-paper closure: evidence is a bounded proxy useful signal, not direct publication-grade validation for tiny-VRAM model training.

## Recommended next action

Run a bounded deepen test with a fused guarded 4-bit Adam implementation on a GPT-2-small-class or parameter-matched language-model proxy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded 4-bit Adam states on a GPT-2-small-class tiny-VRAM proxy
- Success threshold: No NaNs; final validation loss within 2% of Adam; at least 5x persistent optimizer-state memory reduction; peak memory reduction visible in GPU telemetry; throughput no worse than 2x Adam after kernel optimization.
- Stop condition: Stop if guarded 4-bit Adam diverges on any seed, exceeds 5% validation-loss degradation after matched training budget, or fails to show real peak-memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-block-wise-optimizer-states-for-tiny-vram-66199d1202c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
