# Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-evidence-ledger-de8437d4cb37`
Run ID: `agent-evidence-ledger-de8437d4cb37-20260530T085611021728+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3158d7e70227

## What looked useful

Structured evidence links made unsupported-claim auditing exact in the tested setting: ledger unsupported-claim F1 was 1.0 versus 0.6226 for free-form notes in the main run, and ledger tamper F1 was 1.0 versus 0.0 for notes. The 10-seed sweep preserved ledger F1 at 1.0 for both tasks while notes unsupported-claim F1 averaged 0.6281.

## Boundaries and scale limits

The run used synthetic policy-matched traces only: 500 main runs plus a 10-seed sweep of 500 runs per seed. It did not test real agents, human auditors, adversarial ledger forgery, large repositories, or production LangGraph/GitHub traces.

## Claim scope

On deterministic synthetic agent-run traces generated with typed evidence requirements, an append-only evidence ledger with claim-to-evidence links and hash chaining detects unsupported claims and post-hoc payload tampering more reliably than a simple free-form notes baseline.

## Why it stopped

No-paper closure: the mechanism is supported only by synthetic, policy-matched evidence, so this is useful signal rather than direct publication-grade validation.

## Recommended next action

Run a bounded real-trace follow-up on 20-50 actual agent coding or research runs with ledger emission enabled and blinded audit comparison against free-form notes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace audit study for an agent evidence ledger
- Success threshold: Ledger audit F1 at least 0.85 and at least 0.15 absolute F1 higher than notes baseline, with median authoring overhead below 10% and documented schema failures below 20% of runs.
- Stop condition: Stop if real agents cannot emit complete ledgers for at least 80% of runs, if ledger F1 is below 0.75, or if overhead exceeds 20% median runtime without a clear mitigation.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-de8437d4cb37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
