# CPU N-gram Draft Speculative Decode for 1B Local Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-speculative-decode-for-1b-local-model-f9f25b2d92f1`
Run ID: `cpu-n-gram-draft-speculative-decode-for-1b-local-model-f9f25b2d92f1-20260601T032512287176+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/24bdd0ffe31a

## What looked useful

Prompt-lookup CPU n-gram drafting works on copy-heavy/repetitive outputs but gives too little upper-bound gain on ordinary assistant prompts to support a general default-path speedup claim. The positive control shows the implementation can find useful spans when task structure supplies repetition.

## Boundaries and scale limits

Single 1.5B-class local target model, 10 general prompts, 5 repetitive positive-control prompts, max 96 new tokens per prompt. Results are offline exact-match replay over target traces, not online end-to-end speculative decoding latency. Verification batch cost, scheduler overhead, longer workloads, and larger models were not measured.

## Claim scope

On 935 greedy continuation tokens from Qwen/Qwen2.5-1.5B-Instruct general assistant-style prompts, CPU prompt-lookup n-gram drafting produced only a 1.009x-1.049x optimistic target-call speedup upper bound for n-gram lengths 1-5. On 480 repetitive positive-control tokens, the same mechanism produced a 1.348x-1.534x upper bound.

## Why it stopped

Offline replay over direct 1B-class target traces is an early falsification for the broad practical-speedup hypothesis: general prompts reached only 1.049x best-case target-call speedup before real serving overhead, while meaningful gains appeared only in repetitive positive controls.

## Recommended next action

Stop as no-paper useful signal unless pursuing a bounded deepen test: implement online speculative verification and require at least 1.15x median end-to-end latency speedup on general prompts before continuing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online latency test for CPU prompt-lookup n-gram speculative decoding
- Success threshold: At least 1.15x median end-to-end latency speedup with no p95 regression above 5% on the scoped structured/copy-heavy workload, and a clear neutral or positive result on general prompts.
- Stop condition: Stop if online overhead reduces general-prompt median speedup below 1.05x or structured/copy-heavy median speedup below 1.15x after basic implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-speculative-decode-for-1b-local-model-f9f25b2d92f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
