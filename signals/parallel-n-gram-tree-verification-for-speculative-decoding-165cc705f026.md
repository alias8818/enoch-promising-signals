# Parallel N-Gram Tree Verification for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `parallel-n-gram-tree-verification-for-speculative-decoding-165cc705f026`
Run ID: `parallel-n-gram-tree-verification-for-speculative-decoding-165cc705f026-20260607T043437643944+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8a0847754e5c

## What looked useful

Parallel tree verification is mechanically viable, but the measured GB10 CUDA launch/level overhead makes it unattractive for small and medium speculative candidate budgets unless verification is fused with model-side GPU work or candidate trees are extremely large.

## Boundaries and scale limits

No language model forward pass, real n-gram proposer, KV-cache layout, tree-attention mask, batching scheduler, or end-to-end decoding throughput was tested. The largest tested tree is far larger than many practical speculative decoding candidate budgets.

## Claim scope

On synthetic n-gram candidate trees up to 299593 nodes, tensorized per-depth verification correctly reproduces serial verification and substantially reduces Python bookkeeping overhead; CUDA only beats tensor CPU at very large tree sizes near hundreds of thousands of nodes.

## Why it stopped

Synthetic/proxy benchmark gives useful early falsification of a standalone GPU-verification speedup claim for realistic small candidate budgets; it is not a full validation of speculative decoding.

## Recommended next action

Stop this worker run as no-paper proxy evidence; next run should integrate the verifier into a small real-model speculative decoding loop and require end-to-end latency improvement, not just bookkeeping speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model N-Gram Tree Verification Latency Probe
- Success threshold: At least 10% end-to-end latency reduction versus sequential speculative verification at matched output quality and batch size, with verifier bookkeeping not exceeding 5% of decode time.
- Stop condition: Stop if candidate trees under realistic acceptance rates remain below the measured CUDA crossover range or if end-to-end latency is not improved in two representative prompts/batches.

## Evidence references

- Artifact root: `<local-path>/projects/parallel-n-gram-tree-verification-for-speculative-decoding-165cc705f026`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
