# Natural-language evidence ledger halt test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-evidence-ledger-halt-test-c688355380`
Run ID: `natural-language-evidence-ledger-halt-test-c688355380-20260605T185438516360+0000`

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

- Parent run decision: Evidence-ledger agent halts on contradiction: enoch://control-plane/projects/evidence-ledger-agent-halts-on-contradiction-4f3a6d6990c0/runs/evidence-ledger-agent-halts-on-contradiction-4f3a6d6990c0-20260604T191744115732+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/59bc0e094268

## What looked useful

An explicit natural-language evidence ledger can enforce a fail-closed paper halt rule that catches evidence-incomplete metric-passing cases missed by a metric-only baseline.

## Boundaries and scale limits

The test used controlled generated ledger sentences and deterministic extraction only; it did not evaluate real research logs, noisy paraphrases, missing fields, LLM extraction, human review, or live agent behavior.

## Claim scope

In 48 oracle-labeled controlled traces with explicit natural-language fields for evidence directness, threshold, controls, and reproduction, a deterministic ledger auditor halted all evidence-incomplete paper escalations and advanced only the two oracle paper-ready traces.

## Why it stopped

Tier 1 controlled direct mechanism test passed, but evidence is grammar-dependent and not publication-grade.

## Recommended next action

Run a bounded deepen test on paraphrased and missing-field natural-language ledgers with blinded oracle labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paraphrased evidence ledger fail-closed halt test
- Success threshold: Zero missed halt-required cases, false-positive halt rate no higher than 5%, and fewer missed halts than both baselines.
- Stop condition: Stop as negative if any halt-required case is advanced under the fail-closed ledger rule, or if false-positive halt rate exceeds 5% after parser or rubric fixes are frozen.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-evidence-ledger-halt-test-c688355380`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
