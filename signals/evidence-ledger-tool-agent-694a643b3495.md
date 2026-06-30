# Evidence-Ledger Tool Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-tool-agent-694a643b3495`
Run ID: `evidence-ledger-tool-agent-694a643b3495-20260608T200732045104+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/32e06eb072fe

## What looked useful

The evidence-ledger pattern appears useful as a precision/safety gate: it converts uncertain or conflicting retrieved evidence into abstention and preserves very high answered-case accuracy in this controlled harness. The main practical cost is large coverage loss.

## Boundaries and scale limits

Synthetic data only; no real LLM tool-calling behavior, real retriever, public benchmark, human-labeled citation validity, latency, or cost measurement. Results should be treated as mechanism evidence, not deployment validation or publication-grade proof.

## Claim scope

In a deterministic synthetic factual-QA harness with injected distractors, contradictions, and missing evidence, an explicit evidence ledger plus answer gate reduced unsupported answered claims from 14.0% to 0.0% and wrong answered claims from 25.4% to 0.3%, at the cost of reducing coverage from 100.0% to 45.3%.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-level and does not validate real LLM agents or real-world evidence quality.

## Recommended next action

Run a bounded real-agent follow-up on a public fact-verification or multi-hop QA benchmark with matched retrieval and token budgets, measuring unsupported answer rate, abstention, answer accuracy, citation validity, latency, and cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger on Public Fact Verification
- Success threshold: Unsupported answered claims reduced by at least 50% relative to no-ledger baseline, answered-case accuracy not worse by more than 5 percentage points, and answer coverage at least 60%.
- Stop condition: Stop if the ledger fails to reduce unsupported answered claims by at least 25% in the first 300 labeled examples or if coverage falls below 40% after threshold tuning.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-agent-694a643b3495`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
