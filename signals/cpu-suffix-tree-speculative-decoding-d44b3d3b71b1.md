# CPU Suffix Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-tree-speculative-decoding-d44b3d3b71b1`
Run ID: `cpu-suffix-tree-speculative-decoding-d44b3d3b71b1-20260529T142045459789+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/18d97d379b2d

## What looked useful

Suffix-copy drafting strongly reduces verifier calls on repeated/template streams (synthetic_repetitive 3.457x upper-bound speedup; local_system_text 2.416x), but is essentially absent on Tiny Shakespeare (1.003x) and random text (1.000x).

## Boundaries and scale limits

No target LLM was run; oracle_speedup_upper_bound measures verifier-call reduction only, not end-to-end latency. Real corpora were limited to local documentation/licenses and Tiny Shakespeare; results do not validate broad production serving workloads.

## Claim scope

Bounded oracle-trace simulation of CPU suffix-table speculative drafting on 25k-token continuations from synthetic repetitive, synthetic random, local system text, and Tiny Shakespeare token streams.

## Why it stopped

Proxy evidence is mixed: the mechanism works on repetitive streams but does not support a broad natural-text speculative decoding claim, and no real LLM serving validation was performed.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next action is a direct serving follow-up on repeat-heavy RAG/code-edit prompts with a real target model and measured end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct serving test of CPU suffix drafting on repeat-heavy RAG/code prompts
- Success threshold: At least 1.2x median end-to-end decode speedup with no p95 latency regression and accepted-token-per-verifier-call above 1.2 on repeat-heavy prompts.
- Stop condition: Stop if median speedup is below 1.1x or p95 latency regresses by more than 5% after CPU overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-speculative-decoding-d44b3d3b71b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
