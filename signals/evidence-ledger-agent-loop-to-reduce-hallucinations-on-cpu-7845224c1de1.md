# Evidence-ledger agent loop to reduce hallucinations on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-to-reduce-hallucinations-on-cpu-7845224c1de1`
Run ID: `evidence-ledger-agent-loop-to-reduce-hallucinations-on-cpu-7845224c1de1-20260604T010213715489+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de04c27d0779

## What looked useful

The mechanism is promising under structured-claim assumptions: ledger verification eliminated unsupported and irrelevant synthetic claims, and repair recovered many requested facts when evidence was retrieved. The result motivates a bounded direct small-model evaluation but should not be reported as a real-world hallucination reduction claim.

## Boundaries and scale limits

This run did not evaluate real LLM outputs, natural-language claim extraction, real retrieval corpora, human factuality labels, long-horizon agent loops, or model-size scaling. It is a CPU-only proxy mechanism test, not publication-grade validation.

## Claim scope

In a deterministic synthetic structured-claim benchmark with imperfect retrieval and distractor evidence, an evidence-ledger filter plus repair loop reduced unsupported claims from 1.09 per answer to 0.0 and improved fully correct answers from 0.2395 to 0.8165 over 2,000 paired trials.

## Why it stopped

Proxy-only synthetic structured benchmark supports the mechanism but lacks direct evidence on real LLM hallucinations, so it is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger loop on natural-language answers from a CPU-runnable small instruction model with explicit claim extraction and factuality grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model natural-language evidence-ledger hallucination test
- Success threshold: At least 30% relative reduction in unsupported claims versus baseline with paired 95% CI excluding zero, while completeness falls by no more than 10% absolute.
- Stop condition: Stop if claim extraction agreement is below 0.8 on an audit sample, if unsupported-claim reduction is below 10%, or if CPU runtime exceeds the worker budget without producing paired metrics.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-to-reduce-hallucinations-on-cpu-7845224c1de1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
