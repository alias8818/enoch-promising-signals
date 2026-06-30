# Evidence-ledger constraint for hallucination reduction in tiny agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-hallucination-reduction-in-tiny-agents-4ef424252b5f`
Run ID: `evidence-ledger-constraint-for-hallucination-reduction-in-tiny-agents-4ef424252b5f-20260604T120216701035+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6ed8e4d03c38

## What looked useful

Ledger gating reduced hallucination rate from 0.3998 to 0.0000 on 14,400 paired rows per condition, with paired bootstrap hallucination delta -0.3998 CI [-0.4076, -0.3924]. The cost was a large abstention increase from 0.0422 to 0.4676 and a slight supported-question accuracy drop in the main run.

## Boundaries and scale limits

Proxy-only synthetic evidence; no neural language model, natural-language entailment, real retrieval corpus, multi-turn agent behavior, or human/API grading was tested.

## Claim scope

In a deterministic synthetic slot-value tiny-agent harness with paired retrieval samples and priors, an evidence-ledger gate eliminated unsupported value emissions and improved overall correctness when absent-evidence queries were common.

## Why it stopped

Proxy-only synthetic result supports the mechanism but is not direct/full validation of hallucination reduction in LLM agents.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same ledger gate on a real small instruction model with natural-language evidence and matched no-ledger prompting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language small-model ledger-gate validation
- Success threshold: Unsupported-answer rate decreases by at least 25 percentage points with 95% CI excluding 0, and supported-question accuracy decreases by less than 10 percentage points.
- Stop condition: Stop as negative if ledger gating fails to reduce unsupported answers by 10 percentage points or if supported-question accuracy drops by 20 percentage points or more.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-hallucination-reduction-in-tiny-agents-4ef424252b5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
