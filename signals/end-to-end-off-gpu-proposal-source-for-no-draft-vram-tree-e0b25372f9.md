# End-to-end off-GPU proposal source for no-draft-VRAM tree verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-off-gpu-proposal-source-for-no-draft-vram-tree-e0b25372f9`
Run ID: `end-to-end-off-gpu-proposal-source-for-no-draft-vram-tree-e0b25372f9-20260610T165313876033+0000`

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

- Parent run decision: Real-model profiler test for no-draft-VRAM tree verification: enoch://control-plane/projects/real-model-profiler-test-for-no-draft-vram-tree-verificati-b94dd8f3e5/runs/real-model-profiler-test-for-no-draft-vram-tree-verificati-b94dd8f3e5-20260610T162758782613+0000
- Parent run decision: SpecDec Tree Verification with No Draft VRAM: enoch://control-plane/projects/specdec-tree-verification-with-no-draft-vram-c02df782e8d4/runs/specdec-tree-verification-with-no-draft-vram-c02df782e8d4-20260610T160127936192+0000

## What looked useful

The mechanism preserves exact greedy outputs and avoids a second CUDA model, but practical speedup is dominated by proposal quality. CPU n-gram acceptance was only 2.7% to 9.5% across gamma widths and produced about 0.66x target-only throughput, while oracle traces reached 1.55x at gamma 4 and 2.53x at gamma 8.

## Boundaries and scale limits

Short 32-token generations, GPT-2 small, Python verifier implementation, no production tree-attention kernel, no large-model serving stack, and only random, n-gram, and trace-oracle proposal sources were tested.

## Claim scope

On GPT-2 small with Wikitext-2 prompts, fixed seeds, one CUDA target model, and CPU-resident proposal sources, exact off-GPU verification is feasible without draft-model VRAM. Oracle-quality CPU traces speed up decoding, but the tested practical CPU n-gram proposal source does not beat target-only greedy decoding.

## Why it stopped

Tier-2 fixed-seed validation with a real target-only baseline, random control, oracle control, and gamma ablation found that the tested practical off-GPU proposal source is too weak to improve throughput despite the verifier mechanism working.

## Recommended next action

Stop this run as no-paper useful signal; a next bounded test should replace the n-gram proposer with a stronger CPU/off-GPU proposer and require direct speedup over the same target-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger CPU/off-GPU proposer for exact no-draft-VRAM verification
- Success threshold: At least 1.2x mean tokens/s versus target-only greedy with exact_match_all true, no CUDA draft-model allocation, and acceptance high enough to reduce target forwards by at least 25% on non-oracle proposals.
- Stop condition: Stop as negative if the stronger non-oracle CPU/off-GPU proposer remains below 1.0x target-only throughput or exactness fails under deterministic float32 verification.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-off-gpu-proposal-source-for-no-draft-vram-tree-e0b25372f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
