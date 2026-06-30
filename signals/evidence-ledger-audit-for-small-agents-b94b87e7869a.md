# Evidence-Ledger Audit for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-audit-for-small-agents-b94b87e7869a`
Run ID: `evidence-ledger-audit-for-small-agents-b94b87e7869a-20260619T152002886208+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/f4d702d8b8ee

## What looked useful

Explicit machine-readable evidence ledgers caught all tested structural, freshness, and tagged-support failures without false rejecting valid ledgers, but semantic-only contradictions were all false accepted.

## Boundaries and scale limits

Synthetic hand-coded corpus only; no real LLM agent traces, no human-labeled external tasks, no adversarial paraphrase suite, and no semantic oracle beyond explicit machine-readable tags.

## Claim scope

Bounded synthetic evidence-ledger audit: a deterministic verifier checked 48 generated ledgers for structure, evidence references, explicit support tags, and freshness constraints.

## Why it stopped

Synthetic proxy evidence supports a practical mechanism and exposes a semantic gap, but it is not direct publication-grade validation on real small-agent outputs.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test a bounded real-agent trace corpus with a task oracle or semantic checker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence-ledger audit with semantic oracle
- Success threshold: At least 50 real traces with semantic contradiction cases; semantic false accept rate reduced by at least 50% versus deterministic ledger-only verifier while false reject rate remains below 10%.
- Stop condition: Stop if no real trace corpus with reliable labels can be produced locally, or if the semantic checker increases false rejects above 10% while reducing false accepts by less than 25%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-audit-for-small-agents-b94b87e7869a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
