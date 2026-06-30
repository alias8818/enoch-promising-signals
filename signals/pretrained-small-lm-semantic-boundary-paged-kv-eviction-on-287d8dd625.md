# Pretrained small-LM semantic-boundary paged-KV eviction on semi-real multi-document prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-small-lm-semantic-boundary-paged-kv-eviction-on-287d8dd625`
Run ID: `pretrained-small-lm-semantic-boundary-paged-kv-eviction-on-287d8dd625-20260531T134443591847+0000`

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

- Parent run decision: Semantic-boundary KV eviction for 6GB long-context inference: enoch://control-plane/projects/semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b/runs/semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b-20260530T043315545164+0000
- Parent run decision: Small-transformer paged-KV semantic-boundary eviction benchmark: enoch://control-plane/projects/small-transformer-paged-kv-semantic-boundary-eviction-benc-1be1a4d240/runs/small-transformer-paged-kv-semantic-boundary-eviction-benc-1be1a4d240-20260531T102503815616+0000

## What looked useful

semantic_boundary reached 0.333 MC accuracy, 0.931 target-fact retention, and 2.013 correct-code avg NLL versus tail_lru at 0.139 accuracy, 0.361 retention, and 2.627 NLL. Paired bootstrap favored semantic_boundary over tail_lru by +19.44 pp accuracy and 0.613 NLL reduction. However, semantic_boundary was not clearly better than semantic_fixed: +1.39 pp accuracy with CI crossing zero and 0.045 NLL reduction with CI crossing zero.

## Boundaries and scale limits

Eviction was emulated by passing retained text to the model rather than modifying a live paged KV cache; facts were synthetic injections into semi-real documents; validation used distilgpt2, 3 fixed seeds, 72 prompts, 8 documents per prompt, and likelihood-based multiple-choice scoring rather than free-form generation.

## Claim scope

On 72 semi-real WikiText multi-document prompts with injected exact-match code facts, distilgpt2 scoring, and a 512-token retained-context budget, semantic-boundary page selection outperformed recency/LRU, boundary-recency, and random-boundary retention on target fact retention, correct-code NLL, and multiple-choice accuracy.

## Why it stopped

Useful bounded evidence supports semantic relevance over recency/random baselines, but does not isolate semantic-boundary paging over fixed semantic pages and does not validate a true serving KV-cache implementation.

## Recommended next action

Stop paper escalation for this run; the next bounded deepening should implement actual streaming paged-KV eviction hooks and test whether the semantic-boundary advantage persists beyond retained-text emulation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual streaming paged-KV semantic-boundary eviction hooks for small-LM multi-document QA
- Success threshold: On at least 150 fixed-seed prompts, semantic-boundary must improve exact-match or multiple-choice accuracy by at least 10 percentage points over tail_lru and at least 5 percentage points over semantic_fixed, with non-overlapping paired bootstrap intervals for answer NLL or accuracy and no more than 10% latency overhead versus semantic_fixed.
- Stop condition: Stop if a live-KV implementation cannot preserve valid generation semantics, if semantic-boundary fails to beat semantic_fixed on both answer quality and retention, or if latency overhead exceeds 25% at the tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-small-lm-semantic-boundary-paged-kv-eviction-on-287d8dd625`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
