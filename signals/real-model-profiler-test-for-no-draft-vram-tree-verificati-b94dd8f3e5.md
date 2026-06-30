# Real-model profiler test for no-draft-VRAM tree verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-profiler-test-for-no-draft-vram-tree-verificati-b94dd8f3e5`
Run ID: `real-model-profiler-test-for-no-draft-vram-tree-verificati-b94dd8f3e5-20260610T162758782613+0000`

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

- Parent run decision: SpecDec Tree Verification with No Draft VRAM: enoch://control-plane/projects/specdec-tree-verification-with-no-draft-vram-c02df782e8d4/runs/specdec-tree-verification-with-no-draft-vram-c02df782e8d4-20260610T160127936192+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1f41c074e5ce

## What looked useful

The direct profiler showed target_only_tree had draft_param_bytes == 0 and 261,468,672 CUDA allocated bytes after load, while target_plus_draft_resident had 431,588,352 bytes. The 170,119,680 byte delta matches the 170,116,620 byte measured draft parameter footprint within allocator rounding, supporting the no-draft-VRAM verification mechanism for supplied candidates.

## Boundaries and scale limits

Tested one real GPT-2-class target, one distilgpt2 resident-draft control, fp16 inference, one prompt, deterministic precomputed candidates, depth 4, branching 4, and no optimized shared-prefix tree attention or end-to-end speculative decoding loop.

## Claim scope

On GB10 CUDA with PyTorch 2.12 and Hugging Face Transformers, a GPT-2 target model can perform packed candidate-tree verification with no draft model loaded; compared with a gpt2+distilgpt2 resident control, target-only load allocation is lower by the draft model footprint.

## Why it stopped

Tier 1 direct mechanism threshold was met, but evidence is not paper-ready because proposals were precomputed and the run did not test end-to-end speculative decoding, acceptance quality, larger models, or optimized tree kernels.

## Recommended next action

Run a bounded end-to-end follow-up that feeds candidate trees from a CPU/off-GPU proposal source into the target-only verifier and compares memory, latency, and accepted tokens against a GPU-resident draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end off-GPU proposal source for no-draft-VRAM tree verification
- Success threshold: Target-only/off-GPU-proposal condition keeps CUDA load allocation at least 20% below the GPU-resident draft baseline and achieves at least 80% of the baseline accepted-token throughput on the same prompt set.
- Stop condition: Stop if candidate generation or transfer overhead makes accepted-token throughput below 50% of the GPU-resident draft baseline, or if any draft-sized CUDA allocation appears in the target-only condition.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-profiler-test-for-no-draft-vram-tree-verificati-b94dd8f3e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
