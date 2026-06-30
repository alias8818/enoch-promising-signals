# Evidence-Ledger Agent Reliability Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-probe-8b701e6e150c`
Run ID: `evidence-ledger-agent-reliability-probe-8b701e6e150c-20260628T053705645585+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2b982979355

## What looked useful

Schema-only evidence ledgers did not catch missing, contradictory, stale, untrusted, wrong-subject, partial, empty-reference, or drift-trap failures. Adding explicit evidence existence, trust, subject, value, support, and freshness checks caught all unsupported fixture claims.

## Boundaries and scale limits

Fixture-only evidence; no live LLM generations, no real tool traces, no independently collected transcript corpus, and no adversarial natural-language paraphrase robustness test.

## Claim scope

In a 16-case deterministic synthetic fixture of agent-style claims and evidence records, a strict evidence-ledger gate reduced false acceptance of unsupported claims from 100% for accept-all and schema-only baselines to 0%, without false rejects.

## Why it stopped

Closed as no-paper useful signal because the current result is synthetic fixture evidence, not full validation on live or replayed agent outputs.

## Recommended next action

Run the same gate on a small corpus of real or replayed LLM tool-agent transcripts with independent support labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Evidence-Ledger Gate on Labeled Tool-Agent Transcripts
- Success threshold: False accept rate is reduced by at least 50% relative to schema-only validation and false reject rate remains below 10% on independently labeled transcript cases.
- Stop condition: Stop if fewer than 50 usable labeled transcript cases can be collected locally or if the strict gate fails to improve false accept rate by at least 25% in the first 25 cases.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-probe-8b701e6e150c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
