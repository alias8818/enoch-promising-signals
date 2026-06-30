# Two-tier tool router with evidence ledger for local RAG agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-tier-tool-router-with-evidence-ledger-for-local-rag-agents-f9fb2a584909`
Run ID: `two-tier-tool-router-with-evidence-ledger-for-local-rag-agents-f9fb2a584909-20260610T000536038779+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfccda14a281

## What looked useful

The mechanism is promising for local RAG safety/cost control, but the benefit is a precision/abstention tradeoff. The ledger gate prevents unsupported answers only when trusted evidence retrieval succeeds; at high retrieval noise, answerable accuracy falls because the system abstains instead of guessing.

## Boundaries and scale limits

Synthetic corpus and deterministic router only; no real local LLM agent, no real embedding index, no production latency, no open-domain user traffic, no human relevance judgments, and no state-of-the-art learned router baseline.

## Claim scope

In a deterministic synthetic RAG benchmark with trusted evidence spans, unanswerable/ambiguous/chatter queries, and proxy tool costs, a cheap first-stage router plus evidence-ledger acceptance gate reduced unsupported answers to zero and reduced expensive retrieval calls by about 40% versus flat retrieval, while increasing false abstentions on answerable queries.

## Why it stopped

Closed as no-paper useful signal because all evidence is synthetic/proxy-only; it supports the mechanism but not a publication-grade real-agent claim.

## Recommended next action

Run a bounded real-corpus follow-up using a local RAG agent and the same ledger gate against a stronger router baseline, measuring actual latency, tool calls, support precision, and false abstention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus validation of two-tier RAG routing with evidence-ledger gating
- Success threshold: At least 50% relative reduction in unsupported-answer rate and at least 20% reduction in expensive tool calls versus flat retrieval, with answerable false-abstain rate no more than 5 percentage points worse than flat retrieval on the labeled corpus.
- Stop condition: Stop if ledger gating cannot reduce unsupported answers by at least 25% relative to the best baseline or if false abstention exceeds the flat baseline by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/two-tier-tool-router-with-evidence-ledger-for-local-rag-agents-f9fb2a584909`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
