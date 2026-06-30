# Real-text small-corpus confirmation of dedup-aware domain mixing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-text-small-corpus-confirmation-of-dedup-aware-domain-a2807af629`
Run ID: `real-text-small-corpus-confirmation-of-dedup-aware-domain-a2807af629-20260530T033903467190+0000`

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

- Parent run decision: Dedup-aware domain mixing tiny pretraining: enoch://control-plane/projects/dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2/runs/dedup-aware-domain-mixing-tiny-pretraining-3a9b2de0c7e2-20260529T230701003748+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4febaac72315

## What looked useful

Primary duplicate-factor-8 sci.space run improved pooled held-out NLL by 2.70%. A 15-condition sweep showed neutral behavior without duplicate pressure and threshold-clearing improvements in 8/15 settings, with stronger gains as duplicate pressure increased.

## Boundaries and scale limits

Three domains, 180 training and 120 test documents per domain, controlled exact duplicates only, smoothed unigram language model only; no neural LM, no near-deduplication, no web-scale corpus, and no publication-grade robustness.

## Claim scope

On a small public 20 Newsgroups real-text corpus with controlled exact duplicate pressure in one domain, exact-dedup-aware weighting reduced pooled held-out unigram language-model loss versus raw duplicated domain mixing once duplicate pressure was large enough.

## Why it stopped

Tier 1 controlled small direct test completed and produced useful mechanism support, but evidence is not publication-grade because the model is a unigram LM and the duplicate pressure is controlled exact repetition.

## Recommended next action

Run a bounded deepen follow-up using a small neural language model on the same real-text duplicate-control setup before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small neural LM confirmation of dedup-aware domain mixing under real-text duplicate pressure
- Success threshold: Dedup-aware training reduces pooled held-out NLL by at least 0.5% versus raw duplicated mixing in at least two of three duplicated-domain settings at duplicate factor 4 or 8, without worsening the duplicated domain by more than 0.5%.
- Stop condition: Stop as negative if the neural LM sweep fails the threshold in at least two duplicate domains or if gains appear only in the unigram proxy and not in matched neural training.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-small-corpus-confirmation-of-dedup-aware-domain-a2807af629`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
