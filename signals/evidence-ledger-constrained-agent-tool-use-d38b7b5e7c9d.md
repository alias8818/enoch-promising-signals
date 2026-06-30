# Evidence-Ledger Constrained Agent Tool Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d`
Run ID: `evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d-20260524T234243007240+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5293e1f994e2

## What looked useful

Main run: ledger accuracy 0.8250 vs unconstrained 0.5041 and cite-only 0.6121; ledger unsupported action rate 0.0011 vs 0.6102 and 0.3282; ledger injection-follow rate 0.0000 vs 0.3668 and 0.0748; ledger abstention 0.0716. Sensitivity sweep kept ledger injection-follow at 0.0 across tested settings.

## Boundaries and scale limits

No LLM, real tools, natural-language parsing, human-labeled tasks, or multi-turn planning were tested. Results are mechanism-level evidence from 50,000 main synthetic tasks plus a 6-setting sensitivity sweep, not deployment-grade agent validation.

## Claim scope

In a deterministic synthetic tool-use harness with structured evidence records, source trust/signature metadata, stale/conflicting observations, and injected untrusted tool text, an evidence-ledger policy reduced unsupported and injection-driven actions versus unconstrained and citation-only baselines while improving accuracy.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic control-policy evidence rather than direct LLM/tool-use validation.

## Recommended next action

Run a bounded deepen test with an actual LLM agent over the same evidence-record tasks, comparing ledger-gated execution against prompt-only and citation-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Agent Evidence-Ledger Gate Test
- Success threshold: Ledger-gated agent cuts unsupported and injection-follow rates by at least 50% relative to both controls while maintaining answered-task accuracy within 10 percentage points of the best control.
- Stop condition: Stop if ledger gating fails to reduce either unsupported actions or injection-follow rate by at least 25% in a 200-task smoke test, or if parse/format failures exceed 10%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
