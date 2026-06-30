# Exact-anchor evidence ledger for small CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87`
Run ID: `exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87-20260528T020551071549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71f9eafbd9e9

## What looked useful

Exact anchor ledgers are a practical deterministic mechanism for small CPU agents when claims can be bound to exact supporting spans; they materially improve auditability over document-only citations and line anchors at low CPU cost.

## Boundaries and scale limits

Synthetic corpus only; no real LLM/agent loop, no paraphrase or semantic-entailment audit, no multi-hop or multi-span evidence, and no human-judged production traces.

## Claim scope

In a synthetic CPU-local evidence benchmark with 5 seeds, 2000 documents and 4000 anchored facts per seed, exact span+hash anchors survived harmless document shifts, rejected edited evidence, rejected unsupported exact-value claims, and verified at about 745k anchors/s.

## Why it stopped

Synthetic mechanism evidence supports the ledger idea but does not directly validate end-to-end real-agent behavior, so this is not publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay real small-agent QA traces with mandatory exact anchors and measure unsupported citation rate, abstention rate, runtime, and context-token cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace exact-anchor replay for small CPU agents
- Success threshold: Unsupported citation rate reduced by >=50% relative with <=15% runtime overhead and <=10 percentage point abstention increase.
- Stop condition: Stop if exact anchors fail to reduce unsupported citations by at least 25% relative on the first 50 audited traces or runtime overhead exceeds 25%.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
