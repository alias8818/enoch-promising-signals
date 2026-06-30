# N-gram speculative decoding baseline for small GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-baseline-for-small-gpu-9b77ea3e1cf2`
Run ID: `n-gram-speculative-decoding-baseline-for-small-gpu-9b77ea3e1cf2-20260607T054032051641+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

The n-gram baseline has measurable small-GPU upside in an exact-output control case, but correctness failed on deliberately repeated prompts, making this a no-paper mixed result and a clear implementation/debugging target.

## Boundaries and scale limits

Only distilgpt2, greedy decoding, 10 handcrafted prompts per checked set, 48 generated tokens per prompt, one GB10 GPU, no batching, no sampling, no production serving kernels, and no larger models or real corpus evaluation. Repeated-prompt checked runs failed exact-output validation and cannot support a speed claim.

## Claim scope

A short GB10/distilgpt2 greedy-decoding proxy shows that prompt-lookup n-gram speculative decoding can reduce target forward calls and speed up generation when exact greedy output is preserved; the checked control run achieved exact output with 75.5% fewer target forwards and 4.34x local speedup over 480 generated tokens.

## Why it stopped

No-paper useful signal: local proxy evidence showed potential speedup, but repeated-prompt exact-output failures prevent a valid broad or paper-ready claim.

## Recommended next action

Run a bounded follow-up that first fixes and audits exact greedy reproduction across repeated prompts, then repeats the same n-gram/draft sweep only after correctness is guaranteed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Correctness-audited n-gram speculative decoding on repeated prompts
- Success threshold: Across at least 40 prompts and 1920 generated tokens, all outputs must exactly match greedy decoding, speedup must be at least 2x, and target-forward reduction must be at least 50%.
- Stop condition: Stop as a hard negative if any exact-output mismatch remains after fixing cache/replay handling, or if exact runs reduce target forwards by less than 25%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-baseline-for-small-gpu-9b77ea3e1cf2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
