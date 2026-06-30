# CPU N-Gram Draft Speculative Decoding for GB10 Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-n-gram-draft-speculative-decoding-for-gb10-inference-23f19b41f141`
Run ID: `cpu-n-gram-draft-speculative-decoding-for-gb10-inference-23f19b41f141-20260607T180015216903+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98febe24a9fe

## What looked useful

CPU n-gram drafting is cheap enough in Python and achieved exact greedy equivalence with material target-call reduction for repetitive/code/structured prompts, but acceptance is workload dependent and warm-cache text did not clearly improve GPT-2 results.

## Boundaries and scale limits

Not a production serving validation: verifier uses simple full-context forwards rather than optimized KV-cache verification, tested only GPT-2-small-class and tiny models, six prompts, greedy decoding, and no continuous batching or 7B+ model.

## Claim scope

In a bounded local GB10 CUDA harness, a CPU suffix n-gram drafter preserved greedy output for tiny-gpt2 and gpt2 while reducing target verifier forward calls on six short prompts; GPT-2 prompt-local reductions ranged from 38.0% to 46.9% across draft_k 2, 4, and 8.

## Why it stopped

Bounded mechanism signal is useful, but the current evidence is a small harness/proxy for production latency rather than a publication-grade GB10 inference result.

## Recommended next action

Run one deepen follow-up that integrates the CPU n-gram drafter into an optimized KV-cache GB10 inference path and measures real tokens/s, p50/p95 latency, CPU/GPU utilization, and acceptance on a larger model and prompt trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache GB10 CPU n-gram speculative decoding latency validation
- Success threshold: At least 15% end-to-end tokens/s improvement over greedy on the target prompt subset with exact output equivalence and no p95 latency regression above 5%.
- Stop condition: Stop if optimized verifier-call reduction fails to exceed 20% or CPU draft/integration overhead eliminates tokens/s gains on the small model.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-speculative-decoding-for-gb10-inference-23f19b41f141`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
