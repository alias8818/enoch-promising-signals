# Small-model natural-language evidence-ledger hallucination test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-model-natural-language-evidence-ledger-hallucination-e817b62b2e`
Run ID: `small-model-natural-language-evidence-ledger-hallucination-e817b62b2e-20260604T031724201180+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-ledger agent loop to reduce hallucinations on CPU: enoch://control-plane/projects/evidence-ledger-agent-loop-to-reduce-hallucinations-on-cpu-7845224c1de1/runs/evidence-ledger-agent-loop-to-reduce-hallucinations-on-cpu-7845224c1de1-20260604T010213715489+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de04c27d0779

## What looked useful

Ledger prompting improved answerable exact-code extraction from 0.825 to 0.975 and reduced answerable-case hallucination from 0.175 to 0.025, but unanswerable hallucination remained 0.975 in both baseline and ledger conditions with zero abstentions.

## Boundaries and scale limits

One small seq2seq instruction model, one generated context-QA task family, 40 answerable and 40 unanswerable examples, exact string scoring, no few-shot demonstrations, no structured output enforcement, and no naturalistic web QA.

## Claim scope

In an 80-example controlled invented-fact context-QA test with google/flan-t5-small and greedy decoding, a natural-language evidence-ledger prompt did not reduce hallucinated code answers on unanswerable questions relative to a baseline prompt.

## Why it stopped

Direct Tier-1 controlled test falsified the predeclared 30% relative unanswerable-hallucination reduction threshold for natural-language ledger prompting alone; this is not a full validation of all evidence-ledger variants.

## Recommended next action

Stop this run as a no-paper useful negative; the next bounded test should evaluate whether few-shot abstention examples or structured ledger parsing can fix the missing-evidence failure mode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Few-shot abstention and structured ledger test for small-model missing-evidence QA
- Success threshold: At least 30% relative reduction in unanswerable hallucination versus baseline with answerable exact-code accuracy no more than 20 percentage points below baseline, on at least 80 examples.
- Stop condition: Stop if few-shot and structured ledger prompts both leave unanswerable hallucination above 70% or reduce answerable accuracy below baseline by more than 20 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-natural-language-evidence-ledger-hallucination-e817b62b2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
