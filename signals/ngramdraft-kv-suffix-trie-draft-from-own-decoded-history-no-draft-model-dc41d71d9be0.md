# NGramDraft-KV: Suffix-Trie Draft from Own Decoded History, No Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ngramdraft-kv-suffix-trie-draft-from-own-decoded-history-no-draft-model-dc41d71d9be0`
Run ID: `ngramdraft-kv-suffix-trie-draft-from-own-decoded-history-no-draft-model-dc41d71d9be0-20260621T210615405667+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c880ed71591

## What looked useful

The mechanism is real for exact repeated continuations and modestly present in GPT-2-tokenized natural text, but the measured gain is an upper bound and not yet evidence of practical serving speedup.

## Boundaries and scale limits

Proxy trace only; no target-model forward passes, GPU latency, KV-cache integration, sampling divergence, batching, or multi-corpus robustness were measured.

## Claim scope

On a 120k-token Tiny Shakespeare GPT-2-token trace, an own-history suffix drafter with oracle verification achieved an 18.4% ideal target-call reduction in the best tested short-context configuration; positive and negative controls behaved as expected.

## Why it stopped

Proxy-only useful signal; not full validation and not paper-ready without direct target-model serving evidence.

## Recommended next action

Run a bounded direct serving benchmark with a small local target model, preserving greedy outputs and measuring real tokens/second, verifier calls, accepted draft tokens, CPU overhead, and GPU utilization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small serving benchmark for own-history suffix drafting
- Success threshold: At least 10% end-to-end tokens/second improvement over greedy decoding on GPT-2-small-class local runs with identical greedy outputs and no worse than 5% regression on negative-control prompts.
- Stop condition: Stop if accepted draft tokens per verifier call stay below 0.1 or CPU/index overhead eliminates measured throughput gains across the prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/ngramdraft-kv-suffix-trie-draft-from-own-decoded-history-no-draft-model-dc41d71d9be0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
