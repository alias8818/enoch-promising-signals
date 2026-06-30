# Agent reliability via evidence ledger with counterexamples

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2`
Run ID: `agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2-20260605T153409056113+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0797ab292fce

## What looked useful

Across 2000 primary seeds, counterexample_ledger had 0.0000 final observed-contradicted active claims versus 0.6240 for support_only_ledger, and 0.1180 final hidden-world false claims versus 0.6684 for support_only_ledger. Sensitivity runs over low exceptions, high exceptions, and unbiased stream order preserved zero observed contradiction for the counterexample ledger.

## Boundaries and scale limits

No LLMs, natural-language tasks, retrieval, tool use, or user-facing agent workflows were tested. Intermediate claim-time metrics are sampled every 10 observations. The benchmark is construction-aligned with the proposed counterexample mechanism, so it is a mechanism probe rather than broad validation.

## Claim scope

In a synthetic sequential evidence benchmark of category-property universal claims with item-level exceptions, a persistent evidence ledger that records counterexamples eliminates active claims contradicted by the agent's observed evidence and improves hidden-world claim precision relative to support-only or sticky claim policies.

## Why it stopped

Synthetic evidence supports the mechanism but does not provide direct publication-grade evidence for real LLM-agent reliability.

## Recommended next action

Run a bounded natural-language LLM-agent follow-up with identical ledger policies embedded in prompt/state and held-out counterexample traces; do not write a paper from this synthetic-only mechanism probe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language LLM-agent counterexample ledger harness
- Success threshold: Counterexample-ledger agents reduce final contradicted answer rate by at least 30% relative to support-only memory while retaining at least 70% of support-only answer coverage.
- Stop condition: Stop if the ledger reduces contradicted answers by less than 10%, if it achieves the reduction only by abstaining on more than half of support-only answered tasks, or if counterexamples are not persistently represented after distractor turns.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
