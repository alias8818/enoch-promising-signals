# N-gram speculative draft for 300M local target on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-300m-local-target-on-gb10-ade73dcbb47e`
Run ID: `n-gram-speculative-draft-for-300m-local-target-on-gb10-ade73dcbb47e-20260529T225651550105+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ff0a491742f

## What looked useful

Speculative outputs matched baseline on all 12 calibrated prompts. Target forwards fell from 768 to 367 overall. Mean target-forward reduction was 84.0% on repetitive prompts, 46.9% on natural prompts with model-induced repetition, and 25.8% on low-match prompts.

## Boundaries and scale limits

Prototype uses full-prefix recomputation rather than production KV-cache validation; prompt suite is small and synthetic; generation is greedy only; target was EleutherAI/pythia-410m because cached facebook/opt-350m failed local-only loading; no real user traces, batching, sampling, or long-context serving were tested.

## Claim scope

On a GB10 GPU worker using a cached 405M-parameter local causal LM target and exact greedy decoding, a full-prefix prototype of context n-gram speculative drafting preserved baseline output tokens and reduced target forward calls on a 12-prompt bounded suite, with the largest gains on repeated/template-like contexts.

## Why it stopped

Prototype evidence supports the mechanism but is synthetic/full-prefix and therefore insufficient for a paper or production-serving claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement KV-cache-aware n-gram speculation and compare against optimized target-only greedy decoding on at least 100 local prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative decoding for a 300M-class GB10 target
- Success threshold: At least 1.25x geometric-mean tokens/sec improvement on repetitive plus natural prompt groups, exact greedy-token equality on all prompts, and no more than 10% throughput regression on low-match prompts.
- Stop condition: Stop as negative if exact token equality fails, if geometric-mean speedup is below 1.10x after KV-cache optimization, or if low-match prompts regress by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-300m-local-target-on-gb10-ade73dcbb47e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
