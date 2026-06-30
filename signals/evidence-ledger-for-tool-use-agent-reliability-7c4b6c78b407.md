# Evidence Ledger for Tool-Use Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tool-use-agent-reliability-7c4b6c78b407`
Run ID: `evidence-ledger-for-tool-use-agent-reliability-7c4b6c78b407-20260604T131416055624+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/051f75e5febd

## What looked useful

The ledger verifier achieved 1.000 mean invalid detection and 0.000 false accept rate on the synthetic oracle benchmark, while the naive baseline detected only 0.252 mean invalid traces and falsely accepted 0.748 of invalid traces in the main run.

## Boundaries and scale limits

Proxy-only evidence: 20,000 main synthetic traces plus 40,000 sweep traces; no real LLM agents, no natural-language claim extraction, no adversarial ledger formatting, and no long multi-step workflows.

## Claim scope

In deterministic synthetic lookup and arithmetic tool-use traces with structured final claims, a claim-level evidence ledger rejected injected unsupported, stale, uncited, and missing-tool claims that a naive tool-presence baseline frequently accepted.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy evidence, not full validation on real tool-use agents.

## Recommended next action

Run a bounded real-agent trace study with oracle or human labels to test whether natural-language claim extraction plus evidence-ledger validation preserves low false accepts without high false rejects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger validation on real tool-use agent traces
- Success threshold: At least 50% relative reduction in unsupported-claim false accepts versus baseline with valid-claim false reject rate below 10%.
- Stop condition: Stop if claim extraction fails on more than 20% of traces or if ledger validation does not reduce unsupported-claim false accepts by at least 25% in the first 100 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-use-agent-reliability-7c4b6c78b407`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
