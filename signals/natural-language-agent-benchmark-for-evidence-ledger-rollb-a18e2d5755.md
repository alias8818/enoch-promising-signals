# Natural-language agent benchmark for evidence-ledger rollbacks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-agent-benchmark-for-evidence-ledger-rollb-a18e2d5755`
Run ID: `natural-language-agent-benchmark-for-evidence-ledger-rollb-a18e2d5755-20260514T072447710320+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccadfdf81a24

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mechanism supported by a controlled direct benchmark, but evidence is not publication-grade because no real LLM/tool agents were evaluated.

## Recommended next action

Stop this run as no-paper: Tier 1 controlled-policy evidence supports the rollback benchmark mechanism, but a bounded real-agent follow-up is required before any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evaluation of evidence-ledger rollback benchmark
- Success threshold: Rollback-instrumented agents improve exact ledger accuracy by at least 0.30 absolute and reduce rolled-back false-positive retention by at least 50% versus baseline on rollback-depth > 0 cases, while maintaining at least 0.90 exact accuracy on depth-0 controls.
- Stop condition: Stop if baseline and rollback-instrumented agents differ by less than 0.10 exact accuracy on rollback-depth > 0 cases or if manual audit shows the benchmark ground truth is ambiguous in more than 10% of sampled cases.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-agent-benchmark-for-evidence-ledger-rollb-a18e2d5755`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
