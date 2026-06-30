# End-to-end exact cached verifier in a real speculative decoder

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-exact-cached-verifier-in-a-real-speculative-dec-75925cf534`
Run ID: `end-to-end-exact-cached-verifier-in-a-real-speculative-dec-75925cf534-20260523T163642815225+0000`

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

- Parent run decision: Exact cached verifier for n-gram target-cache speculative decoding: enoch://control-plane/projects/exact-cached-verifier-for-n-gram-target-cache-speculative-666670e78c/runs/exact-cached-verifier-for-n-gram-target-cache-speculative-666670e78c-20260523T154135129868+0000
- Parent run decision: N-gram Target-Cache Speculative Decoding: enoch://control-plane/projects/n-gram-target-cache-speculative-decoding-34ab1641c85e/runs/n-gram-target-cache-speculative-decoding-34ab1641c85e-20260523T145504379504+0000

## What looked useful

Cached target verification is mechanically valid in fp32 and reduced target verifier work to 11.9% of no-cache at 64 tokens and 4.0% at 256 tokens. Wall-clock was 0.63x target greedy at 64 tokens and 0.69x target greedy at 256 tokens, so this is not paper-ready speed evidence.

## Boundaries and scale limits

Tested 8 prompts x 64 new tokens and 4 prompts x 256 new tokens with gamma=4, greedy decoding only, one target/draft pair, single-request execution, and an unoptimized draft path that recomputes prefix KV each round. fp16 exactness failed in the medium run.

## Claim scope

On GPT-2 target plus DistilGPT-2 draft greedy decoding on one GB10 GPU, an fp32 cached verifier exactly matched cached target greedy outputs and reduced target verifier forward-token work versus a no-cache verifier ablation; it did not beat the real cached target greedy baseline end-to-end.

## Why it stopped

Tier 2 evidence supports the cached-verifier mechanism but not an end-to-end speedup over a real cached target greedy baseline; fp16 exactness also failed, so publication-grade claims are premature.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add persistent draft KV caching and rerun the same exactness/performance matrix before considering larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent draft-cache speculative decoder with exact cached target verification
- Success threshold: For fp32, exact_match must be true for every prompt and cached speculative decoding must reach at least 1.10x target greedy throughput on the 256- or 512-token setting while retaining at least a 10x target-work reduction versus no-cache verification.
- Stop condition: Stop if persistent draft caching still fails to exceed target greedy throughput, if fp32 exactness diverges, or if implementation complexity requires production serving infrastructure outside this local worker.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-exact-cached-verifier-in-a-real-speculative-dec-75925cf534`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
