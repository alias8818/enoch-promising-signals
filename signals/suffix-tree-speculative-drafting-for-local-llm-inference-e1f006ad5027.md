# Suffix-tree speculative drafting for local LLM inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-drafting-for-local-llm-inference-e1f006ad5027`
Run ID: `suffix-tree-speculative-drafting-for-local-llm-inference-e1f006ad5027-20260620T202803730525+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/56f71e69a40f

## What looked useful

Suffix lookup reached 9.00x theoretical target-step reduction on a repetitive template trace versus 6.60x for fixed 3-gram, with about 42 CPU microseconds per output token. On stdlib code, both methods reached only about 1.4x theoretical target-step reduction and suffix was slightly worse and more CPU expensive.

## Boundaries and scale limits

No real LLM verifier, tokenizer, GPU decode path, KV cache, batching, tree attention, or end-to-end serving latency was measured. Corpora were local proxy traces capped at 30000 tokens each.

## Claim scope

CPU-only oracle trace replay shows suffix-style exact-match drafting can reduce simulated sequential target verification steps on highly repetitive token traces, but does not outperform fixed 3-gram lookup on the stdlib code trace.

## Why it stopped

Proxy trace evidence is mixed and insufficient for a paper-ready local LLM inference claim; it supports workload-dependent usefulness only under high exact repetition.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the proposer with a local LLM verifier and benchmark repeated agentic prompts against fixed n-gram and no-speculation baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end local LLM verifier benchmark for suffix drafting on repeated agentic prompts
- Success threshold: At least 20% end-to-end decode throughput improvement over fixed 3-gram and at least 35% over no speculation on repeated agentic prompts, with no output changes under greedy decoding and no regression above 5% on non-repetitive prompts.
- Stop condition: Stop if suffix drafting fails to beat fixed 3-gram by 10% end-to-end throughput on repeated prompts or if CPU/index overhead exceeds the latency saved by reduced verifier steps.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-drafting-for-local-llm-inference-e1f006ad5027`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
