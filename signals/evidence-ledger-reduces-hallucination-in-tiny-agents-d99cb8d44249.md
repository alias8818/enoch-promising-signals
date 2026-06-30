# Evidence Ledger Reduces Hallucination in Tiny Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249`
Run ID: `evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249-20260603T195533993078+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c067134b618a

## What looked useful

The active mechanism is the ledger plus emission gate, not ledger storage alone: the gated ledger had 0.000 mean hallucination rate across five robustness seeds, while no-ledger averaged 0.705 and ledger-without-gate averaged 0.554.

## Boundaries and scale limits

Synthetic facts, regex extraction, hand-coded protocol agents, short contexts, and no learned language model generation; does not validate real tiny LLM agents, natural-language evidence parsing, or broad factual QA.

## Claim scope

In a synthetic retrieval/extraction tiny-agent benchmark, an evidence ledger with a source-bound answer-emission gate eliminated unsupported entity-field answers across 2,000-trial medium and five-seed robustness runs.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic protocol benchmark, but learned tiny-agent behavior and natural-language evidence handling were only proxied.

## Recommended next action

Run a bounded deepen follow-up using a small instruction model on a real answerable/unanswerable QA dataset with the same no-ledger, ledger-no-gate, and gated-ledger comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger gate on small-model factual QA agents
- Success threshold: Gated ledger reduces unsupported factual emissions by at least 30 percentage points versus no-ledger and by at least 15 percentage points versus ledger-no-gate, while preserving at least 70% of no-ledger correct-answer recall on answerable questions.
- Stop condition: Stop if the gated ledger mainly reduces hallucination by abstaining on more than 60% of answerable examples or if citation audits show emitted answers are not reliably source-supported.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
