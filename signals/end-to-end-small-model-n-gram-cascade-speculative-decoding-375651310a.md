# End-to-end small-model n-gram cascade speculative decoding latency test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-small-model-n-gram-cascade-speculative-decoding-375651310a`
Run ID: `end-to-end-small-model-n-gram-cascade-speculative-decoding-375651310a-20260531T121840979981+0000`

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

- Parent run decision: CPU Speculative Decoding via N-gram Cascade: enoch://control-plane/projects/cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586/runs/cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586-20260530T032813438751+0000
- Parent run decision: Real-tokenizer CPU verifier test for n-gram cascade speculative decoding: enoch://control-plane/projects/real-tokenizer-cpu-verifier-test-for-n-gram-cascade-specul-676fccf078/runs/real-tokenizer-cpu-verifier-test-for-n-gram-cascade-specul-676fccf078-20260530T071035793276+0000

## What looked useful

Tier 2 local validation produced a mixed/no-paper signal: cascade latency improved versus target-only, but accepted only 0.82% of drafted tokens, reduced target calls only from 12.0 to 11.67, and was close to assistant-only latency despite assistant-only accepting 0% of drafts.

## Boundaries and scale limits

This was not an optimized KV-cache serving implementation, GPU result, long-context workload, large-model validation, or trained target-aligned assistant result. The measured speedup appears mostly attributable to implementation/runtime effects rather than accepted speculative drafts.

## Claim scope

On a CPU-only local benchmark using distilgpt2 as target and sshleifer/tiny-gpt2 as assistant, fixed greedy prompts/seeds, and n-gram/assistant/cascade ablations, the naive n-gram plus small-model cascade preserved target output and showed 1.27x mean raw latency speedup over target-only but did not show strong speculative acceptance or a meaningful advantage over assistant-only.

## Why it stopped

Tier 2 direct latency test found weak cascade mechanism support: negligible accepted drafts and no clear cascade-specific win over assistant-only, so the result is useful but not paper-positive.

## Recommended next action

Stop this configuration as no-paper evidence; only revisit with a target-aligned draft model and cache-correct serving harness that must beat assistant-only and n-gram-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Target-aligned draft acceptance sweep for n-gram plus small-model cascade
- Success threshold: Cascade must achieve at least 35% accepted drafted tokens, reduce target calls by at least 20%, and beat both assistant-only and n-gram-only median latency by at least 15% on the same prompts.
- Stop condition: Stop if acceptance remains below 20% or cascade median latency fails to beat assistant-only after two target-aligned assistant choices.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-model-n-gram-cascade-speculative-decoding-375651310a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
