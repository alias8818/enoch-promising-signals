# Evidence-Ledger Agent Reliability on Bounded Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-on-bounded-tool-traces-ac4da41441cf`
Run ID: `evidence-ledger-agent-reliability-on-bounded-tool-traces-ac4da41441cf-20260620T215432137408+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

The mechanism appears useful: tracking provenance, source reliability, recency, and abstention separates observed facts from answerable facts and avoids baseline over-trust on bounded traces.

## Boundaries and scale limits

Synthetic traces only; deterministic policies only; no live LLM extraction, no real tool APIs, no human-authored production traces, and no adversarial natural-language tool outputs.

## Claim scope

In a deterministic synthetic benchmark of 25,000 bounded tool traces with injected stale, conflicting, ambiguous, and missing evidence, a typed evidence ledger improved correctness and eliminated hallucinations relative to first-match, last-match, and majority-vote trace heuristics by abstaining when evidence was ambiguous or low quality.

## Why it stopped

Synthetic deterministic evidence supports the mechanism but is not direct publication-grade validation for real LLM agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger protocol on natural-language tool traces with an LLM extraction/action layer and pre-registered abstention/correctness metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger reliability on natural-language tool traces
- Success threshold: Ledger agent reduces unsupported or hallucinated answers by at least 30% relative to the no-ledger baseline with no more than a 15 percentage point drop in accuracy on answerable cases.
- Stop condition: Stop if ledger extraction fidelity is below 90% on audited traces or if unsupported-answer reduction is below 10% after at least 300 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-bounded-tool-traces-ac4da41441cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
