# Small Agent Evidence Counterexample Capture

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-agent-evidence-counterexample-capture-9c34d470544c`
Run ID: `small-agent-evidence-counterexample-capture-9c34d470544c-20260608T134015637335+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9a735872710e

## What looked useful

Typed verification was the active mechanism: typed queries without verification found the gold sentence in top 5 but never at rank 1, while the full typed agent reached 100% hit@1 across the sweep; lexical and generic exception baselines remained low.

## Boundaries and scale limits

Synthetic-only evidence; generator and verifier share the same contradiction ontology; no real corpus, unseen contradiction family, small LLM, multi-hop, no-counterexample, or adversarial false-positive validation was run.

## Claim scope

In a deterministic synthetic benchmark with four hand-coded contradiction families and high-overlap distractors, typed counterexample probes plus typed verification captured the planted counterexample at rank 1 in all 240 cases for the main seed and all cases across a 10-seed sweep.

## Why it stopped

The evidence is a bounded synthetic mechanism result, not full validation; generator/verifier coupling prevents a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same typed-probe-plus-verifier mechanism on a manually labeled natural-language counterexample corpus with no-counterexample controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Corpus Counterexample Capture With No-Counterexample Controls
- Success threshold: At least 20 percentage point hit@5 improvement over the best non-typed baseline and false-positive rate below 10% on no-counterexample cases.
- Stop condition: Stop as unsupported if the typed agent fails to beat the best baseline by 10 percentage points hit@5 or exceeds 20% false positives on no-counterexample cases.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-evidence-counterexample-capture-9c34d470544c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
