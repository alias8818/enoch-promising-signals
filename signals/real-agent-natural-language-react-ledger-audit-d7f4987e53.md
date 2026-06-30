# Real-Agent Natural-Language ReAct Ledger Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-natural-language-react-ledger-audit-d7f4987e53`
Run ID: `real-agent-natural-language-react-ledger-audit-d7f4987e53-20260529T092003455864+0000`

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

- Parent run decision: Falsifiable Evidence Ledger for CPU ReAct Agents: enoch://control-plane/projects/falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7/runs/falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7-20260528T231903427362+0000
- Parent run decision: Live CPU ReAct Evidence Ledger Against Schema-Only Tool Traces: enoch://control-plane/projects/live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5/runs/live-cpu-react-evidence-ledger-against-schema-only-tool-tr-c2534fabd5-20260529T051343320572+0000

## What looked useful

Ledger-aware reconciliation detected all injected fault classes in the bounded harness, while the combined non-ledger baseline missed all ledger-arithmetic faults and had 0.793 recall overall. The result supports the mechanism but is not paper-ready.

## Boundaries and scale limits

The agent is deterministic rather than an LLM agent; language is templated; faults are injected rather than naturally sampled from production trajectories; the auditor uses structured parsing rather than robust open-ended language understanding.

## Claim scope

On 700 deterministic executed ReAct-style accounting traces with templated natural-language ledger lines, fixed seeds, clean controls, and injected ledger/action/observation/final-answer faults, a ledger-aware auditor achieved higher fault recall than final-answer-only, tool-replay-only, and combined non-ledger baselines at zero clean false-positive rate.

## Why it stopped

No-paper useful signal: medium deterministic evidence supports the mechanism, but naturalistic real-agent evidence is still required before any publication claim.

## Recommended next action

Run a bounded deepen follow-up on real LLM ReAct accounting traces with paraphrased ledgers and the same fixed baseline suite; require retained recall lift over the combined non-ledger baseline at low clean false-positive rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM ReAct Ledger Audit on Paraphrased Natural Traces
- Success threshold: Ledger-aware auditor improves recall by at least 10 percentage points over the combined non-ledger baseline with 95% bootstrap CI lower bound above 0 and clean false-positive rate <= 2%.
- Stop condition: Stop as negative if recall lift is below 5 percentage points, the CI includes zero, or clean false-positive rate exceeds 5% after reasonable parser/prompt calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-natural-language-react-ledger-audit-d7f4987e53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
