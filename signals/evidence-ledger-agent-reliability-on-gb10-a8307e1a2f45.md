# Evidence-Ledger Agent Reliability on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-on-gb10-a8307e1a2f45`
Run ID: `evidence-ledger-agent-reliability-on-gb10-a8307e1a2f45-20260629T083431903627+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58869bd8e939

## What looked useful

Across 3,000,000 synthetic CUDA trials, ledger accuracy stayed near 0.9506 with zero invalid citations and 1.0 tamper recall, while baseline accuracy fell from 0.5719 to 0.2821 as attack strength increased and unsupported-answer rate rose from 0.1147 to 0.5629.

## Boundaries and scale limits

No real LLM agent, tool-calling workflow, real retrieval corpus, human evaluation, or long-running serving workload was tested. The benchmark partly encodes the ledger advantage in policy rules, so it supports mechanism plausibility but not real-world agent reliability.

## Claim scope

Synthetic GB10-executed Monte Carlo mechanism probe: an evidence-ledger policy with trusted-source filtering, payload hash validation, latest-evidence selection, contradiction detection, and abstention improved reliability over a provenance-free baseline under stale, contradictory, and injected evidence.

## Why it stopped

The result is synthetic/proxy evidence only, useful for mechanism triage but not a full validation of evidence-ledger agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the ledger against a real small local LLM/tool agent on adversarial QA traces with matched retrieval context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Reliability on Adversarial QA Traces
- Success threshold: At least 200 real-agent QA trials showing >=50% reduction in unsupported answers and invalid citations with <=10% relative accuracy loss and median latency overhead below 2x.
- Stop condition: Stop if the ledger agent fails to reduce invalid citations by 25% in the first 50 real-agent trials or if abstention exceeds 40% without accuracy benefit.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-gb10-a8307e1a2f45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
