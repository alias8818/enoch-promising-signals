# Trained GPT-2-small EAGLE head with cheap K=256/K=512 dynamic selector

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trained-gpt-2-small-eagle-head-with-cheap-k-256-k-512-dyna-ef4958c1fe`
Run ID: `trained-gpt-2-small-eagle-head-with-cheap-k-256-k-512-dyna-ef4958c1fe-20260520T012746767897+0000`

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

- Parent run decision: Dynamic Speculative Vocabulary for DFlash and EAGLE Heads: enoch://control-plane/projects/dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2/runs/dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2-20260519T234516956601+0000
- Parent run decision: Real-model dynamic vocabulary trace for EAGLE-like speculative heads: enoch://control-plane/projects/real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69/runs/real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69-20260520T003942830919+0000

## What looked useful

Dynamic K=256/512 recovered most of fixed512 quality at avg K 429.6: reference coverage 85.57% vs 86.21% for fixed512 and 81.82% for fixed256; full-head top-1 retention 95.38% vs 95.48% for fixed512 and 94.57% for fixed256. The trained auxiliary head improved CE by about 1.94 nats/token versus the untrained logit-lens selector.

## Boundaries and scale limits

Three fixed seeds, WikiText-2 only, 384 train blocks per seed, no end-to-end speculative verifier, no acceptance-length or latency benchmark, and the cheap selector is a logit-lens proxy rather than a production selector/kernel.

## Claim scope

On GPT-2 small with a trained residual penultimate-hidden auxiliary head over WikiText-2, a logit-lens dynamic K=256/512 selector preserved most fixed-K=512 reference coverage and full-head top-1 retention while reducing average K by about 16%, but required average K about 430 rather than near 256.

## Why it stopped

Tier 2 evidence supports the mechanism but not a publication claim: the dynamic selector's quality/compute tradeoff is modest and lacks end-to-end acceptance and latency validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should be an end-to-end GPT-2-small speculative verifier measuring accepted tokens per target forward and latency with the same trained head and dynamic selector.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small speculative verifier for trained EAGLE dynamic K selector
- Success threshold: Dynamic K must match fixed512 acceptance within 1 percentage point, beat fixed256 accepted tokens per target forward by at least 3%, and show a measured latency or verifier-work improvement over fixed512.
- Stop condition: Stop if dynamic K fails to improve accepted tokens per target forward over fixed256, loses more than 1 percentage point acceptance versus fixed512, or provides no measured latency/verifier-work gain.

## Evidence references

- Artifact root: `<local-path>/projects/trained-gpt-2-small-eagle-head-with-cheap-k-256-k-512-dyna-ef4958c1fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
