# N-Gram Speculative Decoding for Agent Tool-Call Syntax

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-agent-tool-call-syntax-db1ad097b73b`
Run ID: `n-gram-speculative-decoding-for-agent-tool-call-syntax-db1ad097b73b-20260521T210931945076+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a2265028a24f

## What looked useful

Simple n-gram speculative drafting is promising for stable, repeated tool-call formats but appears fragile under schema drift and is not uniquely better than templated natural text in this proxy setup.

## Boundaries and scale limits

The experiment used synthetic traces, UTF-8 byte units instead of a model tokenizer, exact-match oracle replay instead of a real target model, and ideal verifier-call reduction instead of end-to-end serving latency. Held-out tool schemas only reached 1.798x to 2.139x ideal speedup with low full-draft hit rates.

## Claim scope

Synthetic byte-level oracle replay shows that n-gram drafting can reduce verifier calls for repeated agent tool-call JSON schemas, with best ideal speedups of 10.237x for compact JSON, 10.938x for pretty JSON, and 9.769x for mixed agent traces.

## Why it stopped

Synthetic byte-level replay supports the mechanism for repeated schemas but is proxy evidence, not full validation; held-out-schema controls show enough fragility to prevent a paper-positive decision.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use real agent traces, a model tokenizer, and latency measurements in an actual speculative decoding loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace tokenizer-level n-gram speculation for stable vs drifting tool schemas
- Success threshold: At least 1.5x median end-to-end latency speedup on repeated-schema tool-call spans with no correctness regressions, and an explicit report showing whether held-out schemas remain below 1.2x or recover with adaptation.
- Stop condition: Stop if repeated-schema traces fail to reach 1.2x end-to-end speedup, if drafter overhead erases verifier-call savings, or if output/tool-call correctness changes under deterministic decoding.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-agent-tool-call-syntax-db1ad097b73b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
