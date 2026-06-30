# Evidence-ledger agent halts on contradiction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-halts-on-contradiction-4f3a6d6990c0`
Run ID: `evidence-ledger-agent-halts-on-contradiction-4f3a6d6990c0-20260604T191744115732+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/59bc0e094268

## What looked useful

Across 10 seeds, 10,000 cases, and 30,000 agent evaluations, the ledger agent had 0.00 unsafe-answer rate, 0.00 missed-halt rate, and 0.00 false-halt rate; first/last-writer baselines answered through all contradiction cases, producing 0.20 aggregate unsafe-answer and missed-halt rates.

## Boundaries and scale limits

The result is symbolic and synthetic only. It does not test natural-language extraction, retrieval quality, source credibility, temporal staleness, ontology matching, multi-hop contradictions, or LLM compliance after a halt signal.

## Claim scope

In a deterministic synthetic harness with already-normalized evidence records, a ledger policy that checks new target assertions against prior target assertions halted on every direct entity/attribute value contradiction and did not false-halt on the included clean controls.

## Why it stopped

Closed as no-paper useful signal because the current evidence supports only the normalized symbolic mechanism, not real retrieval or natural-language agent behavior.

## Recommended next action

Run a bounded natural-language deepen test with labeled contradiction snippets and an extractor/verifier layer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language evidence ledger halt test
- Success threshold: At least 0.90 contradiction halt recall, at most 0.05 false halt rate on clean controls, and lower unsafe-answer rate than first/last-writer baselines on at least 500 labeled natural-language cases.
- Stop condition: Stop if extractor/verifier normalization error causes halt recall below 0.75 or false halt rate above 0.10 after the first 200 labeled cases.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-halts-on-contradiction-4f3a6d6990c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
