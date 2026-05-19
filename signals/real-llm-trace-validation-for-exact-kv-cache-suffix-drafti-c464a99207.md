# Real LLM Trace Validation for Exact KV-Cache Suffix Drafting

Status: `useful_signal`
Project ID: `real-llm-trace-validation-for-exact-kv-cache-suffix-drafti-c464a99207`
Run ID: `real-llm-trace-validation-for-exact-kv-cache-suffix-drafti-c464a99207-20260514T162326666471+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/408ce29cffcd

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct Tier 1 tests on two real causal LMs showed identical token suffixes after different prefixes do not produce identical KV tensors, so exact KV-cache suffix reuse is not viable as stated.

## Recommended next action

Stop this exact KV-cache suffix reuse line as an early direct falsification; branch only the distinct token-suffix speculative drafting idea with verifier and latency accounting.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Token-Suffix Speculative Drafting Without KV-Cache Reuse
- Success threshold: For suffix lengths 8-32, achieve at least 20% drafting opportunity rate and at least 70% acceptance on a diverse prompt set, with at least 1.15x accepted-token throughput over no-draft verification.
- Stop condition: Stop if opportunity rate is below 10%, acceptance is below 50%, or verifier overhead removes throughput gains on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-trace-validation-for-exact-kv-cache-suffix-drafti-c464a99207`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
