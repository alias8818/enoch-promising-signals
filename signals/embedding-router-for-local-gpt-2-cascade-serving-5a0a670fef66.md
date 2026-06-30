# Embedding router for local GPT-2 cascade serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `embedding-router-for-local-gpt-2-cascade-serving-5a0a670fef66`
Run ID: `embedding-router-for-local-gpt-2-cascade-serving-5a0a670fef66-20260520T161421823450+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9f37381b8b8

## What looked useful

On the 256-sample confirmation, last-token embedding AUC was 0.424, mean-pooled embedding AUC was 0.388, and mean-pooled embedding plus entropy AUC was 0.387 for predicting whether distilgpt2 was within 0.15 nats/token of gpt2. The simple entropy baseline was 0.566 AUC and gave a better NLL frontier at roughly 25% cheap-model routing.

## Boundaries and scale limits

256 samples, one train/test split, GPT-2-small-class models only, teacher-forced NLL quality proxy, no production serving stack, no batching/latency measurements, no human or task-specific quality evaluation.

## Claim scope

A bounded local GPT-2-class cascade probe using WikiText-2 prefixes, distilgpt2 as the cheap model, gpt2 as the fallback model, and continuation NLL as the direct quality metric did not find support for a learned embedding router.

## Why it stopped

Bounded local GPT-2 evidence did not show an embedding router beating simpler baselines; this is an early direct negative rather than a full-scale serving validation.

## Recommended next action

Stop this project as an early direct negative/useful-signal result; any future work should first require the embedding router to beat entropy on a larger cross-validated corpus with measured serving latency.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/embedding-router-for-local-gpt-2-cascade-serving-5a0a670fef66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
