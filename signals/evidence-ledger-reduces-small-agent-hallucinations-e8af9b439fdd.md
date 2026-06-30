# Evidence ledger reduces small agent hallucinations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-reduces-small-agent-hallucinations-e8af9b439fdd`
Run ID: `evidence-ledger-reduces-small-agent-hallucinations-e8af9b439fdd-20260522T153634431148+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bab4ca2ce6b9

## What looked useful

Evidence ledgers appear useful as hard verification/gating interfaces, not as prompt-only instructions, for this controlled small-agent hallucination task.

## Boundaries and scale limits

Synthetic templated evidence, one small model, short-context QA only, deterministic template-matched ledger extractor, no natural corpus, no multi-step live agent, and no broad model-family validation.

## Claim scope

On a 720-case synthetic multi-document QA benchmark with google/flan-t5-small, prompt-only evidence ledger instructions did not reduce unsupported answers, but an enforced structured evidence ledger gate reduced unsupported-specific hallucinations from a 0.308 mean baseline rate to 0.000 by abstaining when facts were absent.

## Why it stopped

Closed as no-paper useful signal: local evidence is synthetic and mechanism-specific, sufficient to guide follow-up but not publication-grade broad validation.

## Recommended next action

Run a bounded deepen test on natural evidence packs with unanswerable questions, a general ledger extractor, and at least two small models; stop if enforced ledger gating fails to reduce claim-level unsupported facts by at least 25% without more than a 10-point answerable-accuracy loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: General evidence-ledger gates on natural QA evidence packs
- Success threshold: At least 25% relative reduction in unsupported claim rate versus the best prompt-only baseline, with no more than 10 percentage points loss in answerable-question accuracy across both small models.
- Stop condition: Stop as negative if the enforced ledger does not beat prompt-only/citation baselines on unsupported claim rate, or if accuracy loss exceeds 10 points despite lower hallucination rate.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-small-agent-hallucinations-e8af9b439fdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
