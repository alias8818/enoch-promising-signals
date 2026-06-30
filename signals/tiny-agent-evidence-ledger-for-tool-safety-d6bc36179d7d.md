# Tiny Agent Evidence Ledger for Tool Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d`
Run ID: `tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d-20260527T205101480337+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c64e4140781c

## What looked useful

Trust provenance was the useful mechanism: the full evidence-ledger gate reached 0.0 unsafe action rate and 1.0 benign success, while the no-provenance ablation still accepted unsafe actions in 20.44% of scenarios.

## Boundaries and scale limits

Synthetic scenarios, simple keyword action extraction, no real LLM agent loop, no realistic tool schemas, no production prompt-injection corpus, and no comparison to mature policy engines beyond simple baselines and one provenance ablation.

## Claim scope

In a deterministic 5,000-scenario synthetic tool-safety benchmark, a tiny provenance-aware evidence ledger blocked all generated unsafe tool actions while preserving benign read/send task completion.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only despite supporting the mechanism in the local benchmark.

## Recommended next action

Run a bounded deepen test by replaying 100-300 realistic agent tool traces with injected untrusted observations against the ledger gate and stronger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Realistic Agent Tool Traces Through a Provenance Evidence Ledger
- Success threshold: Ledger unsafe action rate at least 80% lower than trusted-only baseline, benign false-block rate below 10%, and no worse than the strongest non-ledger baseline on both metrics.
- Stop condition: Stop if realistic traces show unsafe-action reduction below 30% or benign false-block rate above 25%, because the synthetic mechanism would not transfer enough to justify broader work.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
