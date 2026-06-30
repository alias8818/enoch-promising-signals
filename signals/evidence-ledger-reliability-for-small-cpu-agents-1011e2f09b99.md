# Evidence-ledger reliability for small CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reliability-for-small-cpu-agents-1011e2f09b99`
Run ID: `evidence-ledger-reliability-for-small-cpu-agents-1011e2f09b99-20260608T205305288375+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0ff866bd4fb9

## What looked useful

Across 27,000 tasks per agent, the evidence-ledger agent improved mean accuracy from 0.6260 to 0.6539 versus direct retrieval, reduced wrong-answer rate from 0.3740 to 0.2566, reduced unsupported-final rate from 0.4581 to 0.3136, and improved unsupported-final rate in all 18 tested configurations, with 0.0895 mean abstention.

## Boundaries and scale limits

Synthetic templated documents and deterministic non-LLM agents only; no real LLM tool use, web/file tasks, human evaluation, or large-scale production traces were tested.

## Claim scope

In a deterministic synthetic noisy fact-retrieval benchmark with small CPU-only retrieval policies, an evidence-ledger finalization gate reduced wrong answers and unsupported final answers relative to direct top-1 retrieval across 18 configurations.

## Why it stopped

The result is a controlled synthetic proxy that supports the mechanism but is not a direct/full validation of real small CPU agents.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete step is a bounded real-agent follow-up using a small local LLM or CPU tool-agent benchmark with the same ledger metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger reliability on real small CPU LLM tool agents
- Success threshold: Evidence-ledger unsupported-final rate at least 25% lower than the best non-ledger baseline, accuracy drop no greater than 5 percentage points, and latency overhead documented under a bounded CPU budget.
- Stop condition: Stop if the ledger fails to reduce unsupported-final rate by 10% on a 100-task smoke/medium benchmark or if CPU runtime exceeds the calibrated local budget without usable checkpoints.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reliability-for-small-cpu-agents-1011e2f09b99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
