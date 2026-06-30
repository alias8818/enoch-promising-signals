# KVCache-RetrDraft: Draft from Existing KV Cache on Repetitive Workloads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kvcache-retrdraft-draft-from-existing-kv-cache-on-repetitive-workloads-006eb4d3f733`
Run ID: `kvcache-retrdraft-draft-from-existing-kv-cache-on-repetitive-workloads-006eb4d3f733-20260609T125008281034+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7332396d4975

## What looked useful

Exact repeats accepted nearly all available draft tokens after the first occurrence: distilgpt2 exact repeats had 0.75 hit rate and 12/16 mean accepted tokens. Short suffix-8 matching was risky: on distilgpt2 shared-prefix/changed-suffix prompts it hit 0.833 but accepted only 2.88/16 tokens on average, and it also hit 0.625 of non-repetitive controls.

## Boundaries and scale limits

Tested only tiny-gpt2 and distilgpt2 on 104-312 synthetic requests with greedy decoding. No production KV tensor grafting, serving-stack latency, real trace cache residency, multi-tenant eviction, sampling, long-context, or 1B-7B+ validation was performed.

## Claim scope

Synthetic small-model probe shows retrieval drafting from prior continuations is useful for exact repeated requests and sufficiently specific long-context matches, but short suffix retrieval is noisy and can hit changed or control prompts with low accepted span.

## Why it stopped

Proxy-only synthetic evidence supports a narrow mechanism but is insufficient for a paper or broad viability claim; actual KV-cache integration and real serving latency remain untested.

## Recommended next action

Stop this run as no-paper useful signal; next perform a bounded serving-stack benchmark with strict retrieval keys, real or recorded repetitive traces, and latency/memory comparison against no-draft and prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-stack RetrDraft latency benchmark with strict cache keys
- Success threshold: At least 10% median latency reduction or throughput gain on a repetitive trace with no quality regression, accepted draft length of at least 4 tokens on 50% or more cache hits, and KV memory overhead documented below a predeclared serving budget.
- Stop condition: Stop if strict retrieval hit rate is below 10%, accepted draft length is below 2 tokens on median cache hits, or KV retention overhead erases latency gains versus prompt-lookup/no-draft baselines.

## Evidence references

- Artifact root: `<local-path>/projects/kvcache-retrdraft-draft-from-existing-kv-cache-on-repetitive-workloads-006eb4d3f733`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
