# Speculative Decoding with N-Gram Draft Models for Home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-draft-models-for-home-gpus-1a24f3683486`
Run ID: `speculative-decoding-with-n-gram-draft-models-for-home-gpus-1a24f3683486-20260605T055606260403+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

The benchmark found 2.47x-2.90x conservative speedup on repetitive/local/code-like traces for 4-token drafts, but Wikitext-2 reached only 0.976x conservative speedup for 4-token drafts and about 0.784x for 8-token drafts. Two-token Wikitext drafts barely cleared break-even at 1.065x.

## Boundaries and scale limits

Trace-level proxy only; no real target LLM logits, no GPU verification kernel, no sampling policy, no KV-cache integration, and no end-to-end wall-clock tokens/s measurement on a 1B-8B home-GPU model.

## Claim scope

Prefix-only n-gram draft models can reduce ideal target verification passes on repeated/code-like token traces, but do not show robust break-even behavior on a natural Wikitext trace for 4-8 token drafts.

## Why it stopped

No-paper closure: this was a trace-level proxy useful-signal run, not full validation; evidence is mixed and insufficient for a broad home-GPU speculative-decoding claim.

## Recommended next action

Run a bounded end-to-end decoder test on a local 1B-8B model with real wall-clock tokens/s, accepted-token distribution, and GPU utilization on repeated code/agent prompts versus Wikitext-style prose.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end n-gram speculative decoding on a local home-GPU LLM
- Success threshold: At least 15% median wall-clock tokens/s improvement over baseline on repeated code/agent prompts with no more than 5% slowdown on prose, across at least 50 prompts per workload.
- Stop condition: Stop if the first 20 prompts show less than 5% speedup on repeated code/agent prompts or more than 10% slowdown on prose.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-draft-models-for-home-gpus-1a24f3683486`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
