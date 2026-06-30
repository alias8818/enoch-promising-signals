# Evidence Ledger for Tool-Calling Safety in Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303`
Run ID: `evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303-20260609T012635202719+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

Provenance separation before action selection was more useful than an after-the-fact high-risk veto alone: guard-only prevented unsafe calls but recovered only 38.2% mean injection task accuracy, while the ledger/filter condition preserved 100% injection task accuracy in this benchmark.

## Boundaries and scale limits

The evidence is synthetic and templated. It does not validate live LLM agents, real tool APIs, natural web prompt-injection diversity, multi-turn attacks, or partially trusted sources.

## Claim scope

In a synthetic templated tool-calling benchmark with a 15,939-parameter linear bag-of-words router, separating trusted user intent from untrusted retrieved text via an evidence-ledger representation reduced unsafe high-risk tool calls under prompt injection from 80.5% mean across four seeds to 0.0%, while preserving clean and authorized high-risk task accuracy.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by synthetic small-router evidence, not direct live LLM-agent validation.

## Recommended next action

Run a bounded direct follow-up around local 0.5B-3B instruction agents with real tool schemas and held-out adversarial paraphrases; do not write a paper from this synthetic result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger wrapper for local small LLM tool agents
- Success threshold: Evidence ledger reduces unsafe high-risk tool-call rate by at least 50% relative to concatenated-context baseline and keeps benign plus authorized high-risk task completion at or above 90% on held-out attacks.
- Stop condition: Stop if ledger utility drops below 80% benign task completion, if unsafe-call reduction is below 20% on both models, or if local model/tool execution cannot be made reproducible.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
