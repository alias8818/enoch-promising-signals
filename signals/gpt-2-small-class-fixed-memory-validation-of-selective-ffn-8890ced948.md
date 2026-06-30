# GPT-2-small-class fixed-memory validation of selective FFN recomputation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-fixed-memory-validation-of-selective-ffn-8890ced948`
Run ID: `gpt-2-small-class-fixed-memory-validation-of-selective-ffn-8890ced948-20260526T181351195101+0000`

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

- Parent run decision: Selective Activation Recomputation for Tiny VRAM: enoch://control-plane/projects/selective-activation-recomputation-for-tiny-vram-1c300eb52568/runs/selective-activation-recomputation-for-tiny-vram-1c300eb52568-20260525T193251942323+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/830068e89f03

## What looked useful

Selective FFN recomputation has direct mechanism support on a GPT-2-small-class block stack, but this run does not validate the stronger fixed-memory capacity claim because total CUDA peak allocated memory was unchanged.

## Boundaries and scale limits

Synthetic tokens only, one forward/backward step, vocab reduced to 8192, no optimizer state, no convergence test, no hard CUDA memory cap search, and no total CUDA peak allocation reduction observed in this bounded matrix.

## Claim scope

Single-GPU GPT-2-small-class one-step CUDA training test shows selective FFN recomputation preserves exact loss and gradients while reducing saved-for-backward tensor bytes by 55.5-58.1% and forward-live allocation by 46.8-71.0% for the tested batch/sequence matrix.

## Why it stopped

Tier 1 direct test produced useful mechanism evidence but not paper-ready fixed-memory validation; CUDA peak allocated memory did not improve in the tested GPT-2-small-class matrix.

## Recommended next action

Run a bounded deepen test that searches max tokens per step under an explicit CUDA memory budget with optimizer state included, then stop unless selective FFN recompute improves max tokens per step by at least 25% with gradient agreement and no more than 25% runtime overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-budget max-token validation of selective FFN recomputation
- Success threshold: Selective FFN recompute achieves at least 25% more tokens per step than baseline under the same memory cap, with max gradient absolute difference at or below 1e-6 in fp32 or an explicitly justified mixed-precision tolerance, and runtime overhead no more than 25%.
- Stop condition: Stop if max tokens per step improves by less than 10%, if gradient agreement fails at the largest shared configuration, or if runtime overhead exceeds 35% across the feasible frontier.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-fixed-memory-validation-of-selective-ffn-8890ced948`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
