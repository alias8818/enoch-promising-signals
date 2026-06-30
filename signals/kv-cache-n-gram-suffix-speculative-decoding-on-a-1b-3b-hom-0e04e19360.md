# KV-cache n-gram suffix speculative decoding on a 1B-3B home-GPU model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-n-gram-suffix-speculative-decoding-on-a-1b-3b-hom-0e04e19360`
Run ID: `kv-cache-n-gram-suffix-speculative-decoding-on-a-1b-3b-hom-0e04e19360-20260531T162421190641+0000`

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

- Parent run decision: N-Gram Suffix Draft for Speculative Decoding on Home GPUs: enoch://control-plane/projects/n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40/runs/n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40-20260531T123900901537+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

The mechanism works when suffix proposals are fully accepted, reducing 260 baseline forwards to 99 speculative forwards across the controlled set. It is fragile under low acceptance because rejected multi-token verification and cache rebuilds can erase the gain.

## Boundaries and scale limits

Small Tier 1 direct test only: synthetic controlled prompts, 64 generated tokens per prompt, one 1.5B model, greedy decoding only, batch size 1, no serving-engine integration, no broad natural workload or 3B validation.

## Claim scope

On four controlled repetitive/structured prompts using Qwen/Qwen2.5-1.5B-Instruct on a GB10 GPU, exact n-gram suffix speculative decoding preserved greedy outputs and achieved 5.35x mean wall-clock speedup, but one low-acceptance structured prompt slowed to 0.79x.

## Why it stopped

Tier 1 direct test produced a useful bounded mechanism signal but not publication-grade evidence; the workload is too small and controlled, and one prompt showed slowdown under low acceptance.

## Recommended next action

Run a medium direct follow-up with acceptance-aware proposal gating and efficient cache rollback on realistic repeated-span long-context prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-gated suffix n-gram speculation on realistic repeated-span prompts
- Success threshold: Exact output match on all prompts; geometric-mean speedup >= 1.20x; no prompt slower than 0.95x after gating; accepted/proposed diagnostics explain wins and losses.
- Stop condition: Stop if exactness fails, if gated speculation remains below 1.05x geometric-mean speedup, or if more than 10% of prompts are slower than 0.95x greedy.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-suffix-speculative-decoding-on-a-1b-3b-hom-0e04e19360`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
