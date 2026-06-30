# Anchor-token KV eviction for 128k context on 10GB GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-token-kv-eviction-for-128k-context-on-10gb-gpu-0787c953713e`
Run ID: `anchor-token-kv-eviction-for-128k-context-on-10gb-gpu-0787c953713e-20260531T130930951014+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eeb1ceb17c75

## What looked useful

At the Llama-2-style 7B fp16 MHA 10 GiB budget of 20,480 retained tokens, anchor+recency achieved 0.8175 dependency hit rate versus 0.5540 for recency-only on a 30% anchor, 50% recent synthetic trace. The gain shrank to +0.056 when anchors were rare and became neutral/slightly negative when anchors were absent.

## Boundaries and scale limits

No full language-model quality evaluation was run. The 10 GiB limit was enforced through KV-token budgets on a GB10 with larger reported UMA memory. Results use synthetic attention targets plus small PyTorch CUDA decode microbenchmarks, not paged-attention serving or production batching.

## Claim scope

Synthetic 128k-token attention/dependency traces show anchor+recency KV eviction retains more anchor-dependent attention mass and dependency targets than recency-only under analytically enforced 10 GiB KV budgets, when queries actually depend on anchor tokens.

## Why it stopped

Closed as a no-paper useful signal because the current evidence is synthetic/proxy evidence, not direct model-quality or serving evidence.

## Recommended next action

Run a bounded real-model deepen test using long-context retrieval prompts or captured attention traces to verify whether trained queries revisit explicit anchors at the same retained-token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model anchor KV eviction on long-context retrieval prompts
- Success threshold: Anchor+recency improves anchor-dependent answer accuracy by at least 10 absolute percentage points over recency-only at the same retained-token budget, while non-anchor/recent accuracy drops by no more than 3 points and decode throughput drops by no more than 15%.
- Stop condition: Stop if real-model anchor-dependent accuracy improves by less than 3 absolute points over recency-only, or if anchor reservation causes more than a 10 point loss on recent/non-anchor controls at the target budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-token-kv-eviction-for-128k-context-on-10gb-gpu-0787c953713e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
