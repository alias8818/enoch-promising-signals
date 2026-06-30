# Activation-Compressed Gradient Checkpointing for Sub-4GB Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-compressed-gradient-checkpointing-for-sub-4gb-training-e28433b4a19d`
Run ID: `activation-compressed-gradient-checkpointing-for-sub-4gb-training-e28433b4a19d-20260524T010255622873+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d71a8a620cd6

## What looked useful

Checkpointing alone reduced batch-24 peak allocated memory from 4.31GiB to 1.98GiB and fit batch 56 at 3.91GiB. Checkpoint plus int8 saved-tensor hooks used more memory and lower throughput: 2.29GiB vs 1.98GiB at batch 24, 3.97GiB vs 3.43GiB at batch 48, and 4.53GiB vs 3.91GiB at batch 56. Int8-only compression fit batch 24 under 4GiB but was slower and less memory-efficient than checkpointing.

## Boundaries and scale limits

Synthetic data only; 2-6 measured optimizer steps per run; measured peak allocation on a high-memory GB10 rather than enforced 4GiB physical VRAM; no real corpus convergence, GPT-2-small full baseline, or multi-hour stability test.

## Claim scope

On a 12-layer 512-hidden synthetic GPT-style CUDA training benchmark, standard block checkpointing achieved sub-4GiB peak allocated memory more efficiently than naive int8 saved-tensor activation compression, and checkpoint_int8 did not extend the sub-4GiB batch-size frontier.

## Why it stopped

Bounded local evidence is a useful proxy/early falsification of the naive activation-compressed checkpointing path, not a full validation: the compressed checkpoint variant was slower and used more peak allocated memory than checkpointing alone.

## Recommended next action

Stop the broad saved-tensor int8 hook approach; if continuing locally, run one bounded selective boundary-only compression test against checkpointing alone with an enforced 4GiB CUDA/process memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective Boundary-Only Compression for Checkpointed Transformer Blocks
- Success threshold: At batch size 48 or larger, selective compression must reduce peak allocated memory by at least 10% versus checkpointing alone while keeping throughput within 10% and matching short-run loss within 1%.
- Stop condition: Stop if selective boundary-only compression still has equal-or-higher peak allocated memory than checkpointing alone or more than 10% throughput loss at the same batch size.

## Evidence references

- Artifact root: `<local-path>/projects/activation-compressed-gradient-checkpointing-for-sub-4gb-training-e28433b4a19d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
