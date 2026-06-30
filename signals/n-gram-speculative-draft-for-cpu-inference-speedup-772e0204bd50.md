# N-gram speculative draft for CPU inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-inference-speedup-772e0204bd50`
Run ID: `n-gram-speculative-draft-for-cpu-inference-speedup-772e0204bd50-20260529T075131149085+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eddb43fb175d

## What looked useful

N-gram lookup strongly reduces target calls on repetitive/code-like traces, but natural prose is near break-even or negative under conservative cost and only approximately break-even under the synthetic CPU kernel. The mechanism is workload-sensitive rather than a broad CPU inference speedup.

## Boundaries and scale limits

No real transformer, BPE tokenizer, KV cache, logits comparison, sampling behavior, or end-to-end CPU serving stack was measured. Results are bounded to 60k-token traces and synthetic verification kernels.

## Claim scope

Proxy trace benchmark of prompt/history n-gram speculative drafting on two Gutenberg prose texts plus synthetic repetitive boilerplate and code, using wordpunct and byte tokenizations with conservative linear and synthetic NumPy CPU verification cost estimates.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper: repetitive traces support the mechanism, but natural prose does not show robust CPU speedup and no real LM backend was measured.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should run an actual CPU decoder-only LM with prompt-lookup drafting on matched natural prose, code, and boilerplate prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LM prompt-lookup speculative decoding benchmark
- Success threshold: At least 1.2x end-to-end tokens/sec on code or boilerplate with no more than 5% slowdown on natural prose, including all lookup and verification overhead.
- Stop condition: Stop if actual end-to-end speedup is below 1.1x on repetitive/code workloads or natural prose slowdown exceeds 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-inference-speedup-772e0204bd50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
