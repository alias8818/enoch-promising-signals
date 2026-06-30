# Evidence-ledger agent for tool safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-for-tool-safety-c40cb9a37b69`
Run ID: `evidence-ledger-agent-for-tool-safety-c40cb9a37b69-20260527T114213138716+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/904c3dfc2ffb

## What looked useful

The binding semantics of an evidence ledger matter: a weak field-existence checklist left 66.65% of invalid synthetic calls executable, while the exact-binding ledger left 0.00% executable and preserved 100% valid-call allow rate.

## Boundaries and scale limits

100,000 synthetic scenarios only; no LLM-generated traces, no real tool APIs, no natural language extraction layer, and the oracle labels are generated from the same abstract evidence semantics as the tested ledger policy.

## Claim scope

In a deterministic synthetic tool-safety harness, a typed evidence ledger that binds proposed tool-call parameters to exact entity, field, value, approved source, freshness window, and conflict state blocked all modeled invalid tool calls while allowing all modeled valid calls.

## Why it stopped

Synthetic mechanism evidence is useful but not direct enough for publication-grade claims about real agent tool safety.

## Recommended next action

Run a bounded deepen follow-up on LLM-generated tool-use traces with an independently labeled oracle before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on LLM-generated tool-use traces
- Success threshold: Ledger unsafe execution rate at least 50% lower than checklist and ledger false-block rate on valid calls below 10% across at least 500 independently labeled traces.
- Stop condition: Stop if the ledger false-block rate is 20% or higher on valid traces, or if unsafe execution reduction versus checklist is below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-tool-safety-c40cb9a37b69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
