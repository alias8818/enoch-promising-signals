# Real-Agent Evidence Ledger on Public Fact Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-on-public-fact-verification-227d304520`
Run ID: `real-agent-evidence-ledger-on-public-fact-verification-227d304520-20260608T234035847372+0000`

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

- Parent run decision: Evidence-Ledger Tool Agent: enoch://control-plane/projects/evidence-ledger-tool-agent-694a643b3495/runs/evidence-ledger-tool-agent-694a643b3495-20260608T200732045104+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/32e06eb072fe

## What looked useful

A source-backed evidence ledger reduced unsupported final answers from 100% for a bare retrieval baseline to 0% while improving accuracy from 50% to 100% on the final bounded public-fact test; summary-only retrieval initially failed coverage, showing source coverage is a key dependency.

## Boundaries and scale limits

Small hand-configured corpus, claim-specific audit rules, simple baseline, no LLM agent, no adversarial or ambiguous claims, and no large held-out public benchmark.

## Claim scope

On a 16-claim controlled public fact-verification corpus using Wikipedia public-source retrieval, a ledger-gated agent eliminated unsupported final answers and preserved full coverage after full-page retrieval fallback.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal but remains too small and configured for paper-positive closure.

## Recommended next action

Run a deepen follow-up on a larger held-out public fact-verification set with stronger citation-capable baselines and non-hand-authored audit logic.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out public fact-verification benchmark for evidence-ledger gating
- Success threshold: Unsupported final answer rate at least 50% lower than the strongest baseline, ledger accuracy at least 80%, and abstention no higher than 25% on held-out claims.
- Stop condition: Stop if ledger unsupported-answer reduction is under 25% or abstention exceeds 40% after retrieval-source calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-on-public-fact-verification-227d304520`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
