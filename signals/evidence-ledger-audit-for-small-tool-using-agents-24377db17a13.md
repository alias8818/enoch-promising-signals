# Evidence-Ledger Audit for Small Tool-Using Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-audit-for-small-tool-using-agents-24377db17a13`
Run ID: `evidence-ledger-audit-for-small-tool-using-agents-24377db17a13-20260527T202013260880+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/80d69c8860f5

## What looked useful

Evidence ledgers made unsupported claims, wrong citations, digest mismatches, observation tampering, wrong observation ids, and omitted ledger entries mechanically auditable in a bounded synthetic harness. The result provides a reproducible failure taxonomy and benchmark scaffold, not a paper-ready real-agent validation.

## Boundaries and scale limits

Synthetic symbolic traces only; exact-match structured entailment; no live LLM agents, no natural-language claim decomposition, no adversarial prompt setting, and no validation of tool truthfulness.

## Claim scope

On 1,200 deterministic synthetic structured traces for small tool-using agents, a claim-level evidence ledger with observation ids and content hashes improved corruption detection recall from 0.5000 for transcript-only audit to 1.0000 with no false positives.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but cannot validate real small tool-using agents or natural-language entailment.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded live-agent validation on at least 200 natural-language tool-use traces with human-checked support labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Agent Evidence-Ledger Audit on Natural-Language Tool Traces
- Success threshold: Ledger audit recall at least 20 percentage points higher than transcript-only audit with false positive rate at or below 5% on human-labeled traces.
- Stop condition: Stop if ledger recall is less than 10 percentage points above transcript-only or false positive rate exceeds 10% after 200 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-audit-for-small-tool-using-agents-24377db17a13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
