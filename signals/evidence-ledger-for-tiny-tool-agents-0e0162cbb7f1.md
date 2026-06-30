# Evidence Ledger for Tiny Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1`
Run ID: `evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1-20260603T221203805557+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4defc5bd2466

## What looked useful

The evidence ledger reached 100% accuracy and 100% valid citation rate across all synthetic distractor settings. Removing timestamp policy dropped accuracy to about 49-51% despite valid citations; removing entity filtering degraded from 93.9% accuracy at one distractor to 62.2% at eight distractors.

## Boundaries and scale limits

Synthetic deterministic policies only; no real LLM agents, live tool APIs, natural-language parsing, adversarial outputs, or long-horizon tasks were tested. Full benchmark was 20,000 generated tasks across four distractor settings.

## Claim scope

In a synthetic lookup benchmark for tiny tool-agent traces, an append-only structured evidence ledger with entity-field filtering and timestamp conflict resolution eliminated stale and distractor binding errors while producing valid evidence citations.

## Why it stopped

This is a synthetic mechanism result only; it is useful for deciding the next experiment but is not direct evidence for real tiny LLM tool agents or paper-ready validation.

## Recommended next action

Run a bounded deepen follow-up using real small LLM tool-agent traces with the same ledger protocol, comparing accuracy, citation validity, and overhead against no-ledger and transcript-scan controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Real Tiny LLM Tool-Agent Traces
- Success threshold: Evidence-ledger condition improves answer accuracy by at least 15 percentage points over the best no-ledger control and reaches at least 95% valid citation rate, with less than 25% end-to-end latency overhead on traces under 12 observations.
- Stop condition: Stop if the ledger improves citation validity but fails to improve answer accuracy by at least 5 percentage points over controls, or if overhead exceeds 50% on traces under 12 observations.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
