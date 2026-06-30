# 4-bit gradient compression for volunteer training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-gradient-compression-for-volunteer-training-714787c8e376`
Run ID: `4-bit-gradient-compression-for-volunteer-training-714787c8e376-20260610T092731836762+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/486752b231db

## What looked useful

Across 3 medium-run seeds, q4_ef matched fp32 accuracy at 0.970988 mean accuracy with 0.125038x fp32 bytes and about 8x modeled upload speedup. In a harsher 16-worker non-IID stress run, naive q4 lost 13.26 accuracy points while q4_ef stayed within 0.012 percentage points of fp32, indicating error feedback is necessary for stable 4-bit volunteer-style gradient compression.

## Boundaries and scale limits

Small MLP, synthetic data, one local GB10 GPU, simulated workers, modeled 10 Mbps upload only, no real WAN links, no churn/stragglers, no real volunteer hosts, no privacy/security layer, and no large model or real benchmark dataset.

## Claim scope

In a local CUDA simulation of synchronous volunteer-style data-parallel training with synthetic non-IID classification shards, 4-bit uniform gradient compression with error feedback preserved fp32 convergence while reducing modeled upload bytes to about 12.5% of fp32.

## Why it stopped

Bounded local simulation supports the mechanism but does not directly validate real volunteer training or provide publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement q4 error-feedback compression in a real federated/distributed trainer on a real dataset with measured network/churn effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real federated q4 error-feedback compression under churn
- Success threshold: q4_ef achieves at least 98% of fp32 final accuracy or within 2 percentage points absolute, sends at most 15% of fp32 upload bytes, and improves measured communication-bound wall-clock by at least 2x under churn.
- Stop condition: Stop if q4_ef falls more than 2 accuracy points behind fp32 on two consecutive seeds or if measured overhead removes the communication-bound wall-clock advantage.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-gradient-compression-for-volunteer-training-714787c8e376`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
