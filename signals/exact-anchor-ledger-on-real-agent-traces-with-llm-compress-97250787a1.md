# Exact-anchor ledger on real agent traces with LLM compression

Status: `useful_signal`
Project ID: `exact-anchor-ledger-on-real-agent-traces-with-llm-compress-97250787a1`
Run ID: `exact-anchor-ledger-on-real-agent-traces-with-llm-compress-97250787a1-20260516T001002943701+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/908298541335

## What looked useful

The exact-anchor ledger mechanism achieved 80/80 exact anchor recall with zero dataset offset/hash mismatches and 8/8 tamper checks, while plain GPT-2 compression preserved 0/80 anchors exactly under the same scored setup.

## Boundaries and scale limits

Small Tier 1 local validation only: 8 traces, 80 scored anchors, GPT-2 compression, no strong instruction-following LLM comparison, no live downstream agent replay, and no large adversarial robustness suite.

## Claim scope

On 8 real local Codex/Enoch agent traces with 80 scored anchors, an out-of-band exact-anchor ledger preserved every scored anchor byte-for-byte through cached GPT-2 compression while keeping total compressed state plus scored anchor payloads at a mean 0.190 source-window byte ratio.

## Why it stopped

Tier 1 direct mechanism evidence is useful but not publication-grade; the local GGUF instruction model path was too slow, and the completed GPT-2-based test is too small and structurally favorable to the ledger for a paper-positive decision.

## Recommended next action

Run a bounded deepen test on at least 50 held-out real traces with stronger instruction-following LLMs, adversarial anchor selection, and downstream audit-question replay before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model held-out exact-anchor ledger replay on real agent traces
- Success threshold: Ledger condition achieves >=99% exact anchor recall, detects all synthetic anchor tampering, and improves downstream audit-question exact-evidence accuracy by >=25 percentage points over plain LLM compression at <=25% total byte ratio.
- Stop condition: Stop if ledger exact anchor recall falls below 95%, total byte ratio exceeds 35% on median traces, or plain strong-LLM compression matches ledger downstream audit accuracy within 5 percentage points while preserving >=95% exact anchors.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-on-real-agent-traces-with-llm-compress-97250787a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
