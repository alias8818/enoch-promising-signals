# Real Tiny Tool-Agent Evidence Ledger Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-tool-agent-evidence-ledger-harness-7bdea1a2e5`
Run ID: `real-tiny-tool-agent-evidence-ledger-harness-7bdea1a2e5-20260608T161212574230+0000`

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

- Parent run decision: Structured Evidence Ledger for Tiny Tool Agents: enoch://control-plane/projects/structured-evidence-ledger-for-tiny-tool-agents-eb020c87ce0a/runs/structured-evidence-ledger-for-tiny-tool-agents-eb020c87ce0a-20260608T091711310885+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48a4ed233ae9

## What looked useful

Citation presence alone accepted all unsupported cited claims, while the evidence-ledger entailment verifier rejected all unsupported cited claims in the 60-case controlled suite.

## Boundaries and scale limits

No live LLM planner, free-form natural-language entailment, external tools, adversarial prompting, long trajectories, or large task distribution was tested.

## Claim scope

A deterministic tiny Python tool-agent harness with structured claims, hashed tool observations, and citation entailment checks accepted 30/30 supported claims and rejected 30/30 unsupported claims that cited real observations.

## Why it stopped

Tier 1 direct structured-harness threshold was satisfied, but the evidence remains too small and structured for publication-grade claims.

## Recommended next action

Close as a no-paper Tier 1 useful signal; the concrete next action is a bounded deepen run with prose claims from a small live or scripted language-agent and a natural-language entailment verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language evidence ledger verifier for tiny tool agents
- Success threshold: Accept at least 90% of supported prose claims and reject at least 90% of unsupported prose claims that cite real observations, with citation-only baseline materially worse on unsupported claims.
- Stop condition: Stop if unsupported cited-claim rejection is below 80%, supported-claim acceptance is below 80%, or failures are dominated by ambiguous natural-language labels that prevent reproducible scoring.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-tool-agent-evidence-ledger-harness-7bdea1a2e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
