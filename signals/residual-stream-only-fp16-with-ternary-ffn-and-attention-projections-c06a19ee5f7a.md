# Residual-Stream-Only FP16 with Ternary FFN and Attention Projections

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-stream-only-fp16-with-ternary-ffn-and-attention-projections-c06a19ee5f7a`
Run ID: `residual-stream-only-fp16-with-ternary-ffn-and-attention-projections-c06a19ee5f7a-20260530T024011015826+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bb72ed072c12

## What looked useful

At 120 steps both dense and ternary/FP16 variants stayed near the uniform baseline. At 600 steps, seed 0 dense reached 2.6511 validation loss while ternary/FP16 stayed near uniform at 2.8349; seed 1 saw neither variant learn clearly. This suggests the naive all-projection ternary recipe is not an immediate paper-positive path and needs ablation before scale-up.

## Boundaries and scale limits

Test used vocab 17, sequence length 12, d_model 24, d_ff 64, batch 32, two seeds, and at most 600 optimizer steps. It did not test real language data, multi-layer models, GPT-2-small scale, GPU kernels, true hardware FP16 throughput, or learned/groupwise ternary scaling.

## Claim scope

A CPU-only toy one-block causal transformer probe found that naive STE ternary attention/FFN projections with FP16-rounded residual activations can run and reduce loss initially, but did not robustly match a dense control once the control learned a delayed synthetic next-token rule.

## Why it stopped

Proxy/toy evidence is mixed and insufficient for a paper: the ternary/FP16 variant failed to learn in the only extended seed where the dense control learned, while the other seed did not provide a valid positive control.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should ablate ternary attention vs ternary FFN vs FP16 residual rounding on a more reliable small learning task before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ablate ternary attention, ternary FFN, and FP16 residual rounding on a reliable tiny transformer task
- Success threshold: Across at least 3 seeds, identify a ternary/FP16 ablation whose mean final validation loss is within 5% of the dense control's loss improvement over uniform, or identify a single component that reproducibly causes failure.
- Stop condition: Stop if the dense control fails to beat the uniform baseline in more than one seed, or if all ternary variants remain within 0.02 nats of the uniform baseline while the dense control improves by at least 0.15 nats.

## Evidence references

- Artifact root: `<local-path>/projects/residual-stream-only-fp16-with-ternary-ffn-and-attention-projections-c06a19ee5f7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
