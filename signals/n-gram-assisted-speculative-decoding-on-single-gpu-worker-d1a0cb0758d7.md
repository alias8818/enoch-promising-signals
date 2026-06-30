# N-gram assisted speculative decoding on single GPU worker

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-assisted-speculative-decoding-on-single-gpu-worker-d1a0cb0758d7`
Run ID: `n-gram-assisted-speculative-decoding-on-single-gpu-worker-d1a0cb0758d7-20260612T205858555473+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5ed6553a91ed

## What looked useful

Copy-heavy cases showed an overall median best-lookup speedup of 3.58x by case, with Qwen2.5-0.5B at 5.02x and Qwen2.5-1.5B at 4.07x. The mechanism was fewer target-model forward calls: e.g. Qwen2.5-1.5B copy_sequence_long used 10 calls for 74 generated tokens at lookup 8 versus 74 calls for baseline. Controls were near-neutral for Qwen models but sped up on the 135M model, so the general control claim is mixed.

## Boundaries and scale limits

Batch size one, short synthetic/local prompt suite, greedy decoding only, cached models no larger than 1.5B parameters, no 7B+ model, no production serving stack, no real task-quality benchmark, and prompt lookup outputs were not always exactly identical to baseline greedy outputs.

## Claim scope

On a single NVIDIA GB10 GPU using Hugging Face Transformers prompt_lookup_num_tokens with greedy decoding, n-gram prompt lookup reduced target-model forward calls and improved tokens/sec on short copy-heavy prompts for cached 135M, 0.5B, and 1.5B causal LMs. The strongest supported claim is practical local throughput benefit when generated tokens substantially reuse prompt n-grams.

## Why it stopped

Bounded local benchmark supports the speed mechanism but is not full validation; outputs differed from baseline in 22 of 45 model/case/lookup comparisons, and the suite is too small and synthetic for paper-ready claims.

## Recommended next action

Stop this worker run as useful no-paper evidence; next run should evaluate a real copy-heavy workload with task-quality or exact-output acceptance criteria before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-gated prompt lookup decoding on real copy-heavy tasks
- Success threshold: At least 1.5x median latency or tokens/sec improvement on high-reuse examples with no statistically meaningful quality degradation and no unacceptable exact-output mismatches for deterministic tasks.
- Stop condition: Stop if prompt lookup gives less than 1.2x median speedup on high-reuse real examples, materially degrades task quality, or output-equivalence requirements fail for deterministic use cases.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-assisted-speculative-decoding-on-single-gpu-worker-d1a0cb0758d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
