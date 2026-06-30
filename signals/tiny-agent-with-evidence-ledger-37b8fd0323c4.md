# Tiny agent with evidence ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-with-evidence-ledger-37b8fd0323c4`
Run ID: `tiny-agent-with-evidence-ledger-37b8fd0323c4-20260605T144638506456+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0eb48d708acf

## What looked useful

Across 10 seeds of 500 tasks each, the no-ledger baseline had mean unsupported assertion rate 0.3092, while the evidence-ledger agent had 0.0000; supported-task accuracy improved from 0.8635 to 1.0000 and latency overhead averaged 1.0174x.

## Boundaries and scale limits

Evidence is synthetic and local only. It does not validate open-ended LLM agents, real retrieval corpora, adversarial passages, human audit speed, or robustness when trusted-source metadata is absent or wrong.

## Claim scope

On a deterministic synthetic fact-QA benchmark with trusted and untrusted provenance records, a tiny retrieval/extraction agent with a mandatory evidence ledger eliminated unsupported assertions and correctly abstained on missing-evidence tasks while preserving supported-task accuracy.

## Why it stopped

No-paper useful signal: the mechanism is supported only by synthetic deterministic evidence, not by direct real-agent or real-corpus validation.

## Recommended next action

Run a bounded real-corpus follow-up using a small local LLM or tool agent on labeled QA/fact-checking tasks with retrieved passages and human-verified evidence labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Real QA Retrieval
- Success threshold: At least 50% relative reduction in unsupported assertion rate versus baseline, no more than 5 percentage point loss in answerable-question accuracy, and evidence validity above 95% on a held-out labeled set.
- Stop condition: Stop if the ledger reduces unsupported assertions by less than 20% relative, evidence validity falls below 90%, or answerable-question accuracy drops by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-with-evidence-ledger-37b8fd0323c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
