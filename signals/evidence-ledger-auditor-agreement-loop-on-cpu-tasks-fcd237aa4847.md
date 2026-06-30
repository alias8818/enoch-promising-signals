# Evidence Ledger Auditor Agreement Loop on CPU Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-auditor-agreement-loop-on-cpu-tasks-fcd237aa4847`
Run ID: `evidence-ledger-auditor-agreement-loop-on-cpu-tasks-fcd237aa4847-20260619T172618271577+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

Reference-only ledger auditing is unsafe for value claims because wrong claims can cite real evidence. Direct exact-value or replay checks are sufficient on this bounded benchmark; the agreement loop worked but did not improve over single strict auditors.

## Boundaries and scale limits

Synthetic CPU tasks only; no real LLM tool-agent traces, semantic claim normalization, stale/conflicting evidence, multi-hop claims, or human/model auditor disagreement were tested.

## Claim scope

On a synthetic deterministic CPU-task evidence ledger with metric-equality claims, accepting claims by evidence-reference presence alone produced high false accepts, while exact metric/text/replay auditors and a 2-of-3 agreement loop rejected all injected wrong-value and missing-reference claims.

## Why it stopped

Proxy/local evidence only: the agreement loop eliminated false accepts versus a weak reference-only baseline, but single strict auditors matched it, so the result does not support a paper-ready novelty claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a held-out real-trace benchmark where natural-language claims and known false claims are audited by single strict verifiers versus an agreement loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace auditor agreement benchmark for evidence-ledger claims
- Success threshold: At least 30 percent relative false-accept reduction versus the best single strict verifier at no more than 5 percent absolute false-reject increase on a held-out real-trace claim set.
- Stop condition: Stop if the agreement loop fails to beat the best single strict verifier on false accepts, or if semantic claim normalization dominates errors and prevents a clean verifier comparison.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditor-agreement-loop-on-cpu-tasks-fcd237aa4847`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
