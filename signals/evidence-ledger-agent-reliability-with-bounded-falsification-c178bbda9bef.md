# Evidence Ledger Agent Reliability with Bounded Falsification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-with-bounded-falsification-c178bbda9bef`
Run ID: `evidence-ledger-agent-reliability-with-bounded-falsification-c178bbda9bef-20260605T051251017562+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb58a872501e

## What looked useful

Main run: accuracy improved from 0.6624 to 0.8170, unverifiable false-positive rate fell from 0.9837 to 0.4049, abstention rose from 0.0060 to 0.2482, and mean checked sources rose from 3 to 8. Sensitivity runs preserved positive accuracy deltas and lower unverifiable false-positive rates across tested noise levels and falsification budgets.

## Boundaries and scale limits

Proxy-only CPU benchmark with deterministic policies, synthetic evidence relations, 5,000 main tasks, 400 bootstrap rounds, and a small sensitivity sweep; no real LLM, real corpus, interactive agent loop, or deployed retrieval stack was tested.

## Claim scope

In a controlled synthetic claim-verification benchmark, an explicit evidence ledger with bounded falsification improved accuracy and reduced false positives on unverifiable claims compared with an answer-first policy.

## Why it stopped

Proxy-only evidence supports the mechanism but is not direct/full validation of real agent reliability.

## Recommended next action

Stop this run as proxy useful-signal evidence; next run should test the same ledger and bounded falsification protocol with a real small LLM, real passages, citation verification, and answer-first/retrieval-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-passage LLM evidence-ledger reliability benchmark
- Success threshold: Evidence-ledger policy reduces unverifiable false-positive or unsupported answer rate by at least 25% relative to answer-first with non-overlapping bootstrap confidence interval and no decrease in accuracy greater than 2 percentage points.
- Stop condition: Stop if citation validation cannot be made deterministic, if the ledger policy fails to reduce false positives by at least 10% in a 200-claim pilot, or if latency/source-check overhead exceeds 3x without a reliability gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-with-bounded-falsification-c178bbda9bef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
