# Tool-Call Evidence Ledger with Counter-Example Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-call-evidence-ledger-with-counter-example-audit-38cec9ef93e6`
Run ID: `tool-call-evidence-ledger-with-counter-example-audit-38cec9ef93e6-20260611T010459638247+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

In 5,000 synthetic cases, citation-only accuracy was 0.4914, ledger support-only accuracy was 0.6106, and ledger with counter-example audit accuracy was 0.9972. Unsupported-claim caught rate improved from 0.2158 for citation-only and 0.3996 for support-only to 0.9991 with counter-example audit.

## Boundaries and scale limits

The benchmark uses generated structured triples, not natural-language tool outputs, real agent transcripts, human labels, or an extraction layer. It does not validate production robustness or paper-grade generality.

## Claim scope

On deterministic synthetic structured tool-call traces, a ledger audit that requires cited support and searches all ledger entries for fresher or more reliable counterexamples catches stale, irrelevant, and contradicted claims much better than citation-only or cited-support-only checks.

## Why it stopped

No-paper closure: the result is a useful synthetic structured-signal benchmark, not direct publication-grade evidence on real tool-call traces.

## Recommended next action

Run a bounded deepen follow-up on real or realistic tool-call transcripts with labeled claim support/contradiction outcomes and an explicit natural-language extraction layer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transcript Counter-Example Audit Evaluation
- Success threshold: Counter-example audit improves unsupported-claim F1 by at least 0.15 absolute over the best baseline while keeping supported-claim false rejection below 10%.
- Stop condition: Stop if extraction quality cannot exceed 0.80 exact/semantically equivalent fact match on a 50-item labeled calibration set or if counter-example audit fails to beat support-only by at least 0.05 unsupported-claim F1.

## Evidence references

- Artifact root: `<local-path>/projects/tool-call-evidence-ledger-with-counter-example-audit-38cec9ef93e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
