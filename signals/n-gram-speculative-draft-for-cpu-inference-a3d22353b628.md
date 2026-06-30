# N-Gram Speculative Draft for CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-cpu-inference-a3d22353b628`
Run ID: `n-gram-speculative-draft-for-cpu-inference-a3d22353b628-20260525T204401204774+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

The mechanism is real and cheap: GPT-2 accepted 86 of 104 drafted tokens on repeated prompts and 43 of 56 on non-repeating controls with min_n=4, while n-gram schedule evaluation cost about 0.01s versus about 16.5s for 240-token CPU greedy generation. This supports a bounded follow-up to implement direct KV-cache verification.

## Boundaries and scale limits

Only 5 prompts per condition, 240 target tokens per calibrated run, greedy decoding only, GPT-2/distilgpt2 only, and no optimized end-to-end speculative decoder tokens/s measurement. Results should not be generalized to sampled decoding, larger models, broad instruction workloads, or production CPU serving.

## Claim scope

On cached GPT-2-class CPU greedy traces with small repeated and control prompt sets, exact n-gram prompt/context lookup can draft tokens that the target model accepts, with negligible lookup overhead and simulated verifier-call reductions from 16.7% to 34.6% under a stricter 4-token minimum match for GPT-2.

## Why it stopped

No-paper useful signal: this run measured target acceptance and simulated verifier-call reduction, but not production-quality end-to-end speedup or broad workload robustness.

## Recommended next action

Implement a direct CPU speculative decoder with KV-cache draft verification and compare actual tokens/s against greedy decoding on a 100+ prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU n-gram speculative decoding benchmark
- Success threshold: At least 10% geometric-mean tokens/s improvement on repeated-context prompts, no more than 5% slowdown on non-repeating controls, and exact greedy-output equality across all benchmark prompts.
- Stop condition: Stop if optimized verifier overhead erases the simulated call-count gain, if output equality fails, or if repeated-context speedup remains below 5% after min_n/max_draft tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-inference-a3d22353b628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
