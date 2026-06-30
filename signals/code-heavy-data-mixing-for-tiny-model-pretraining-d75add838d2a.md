# Code-heavy data mixing for tiny model pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `code-heavy-data-mixing-for-tiny-model-pretraining-d75add838d2a`
Run ID: `code-heavy-data-mixing-for-tiny-model-pretraining-d75add838d2a-20260527T131851140705+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2bacaca076fc

## What looked useful

Code-heavy data mixing behaved as specialization rather than a free general pretraining win: 100% code improved code NLL by 0.0766 versus the 50% baseline, while 75%+ code worsened balanced mean NLL through prose degradation.

## Boundaries and scale limits

Synthetic corpora, mean-pooled character model, 18 short CPU trainings, no transformer architecture, no subword tokenizer, no real-code corpus, no downstream benchmark evaluation, and no large-token-budget validation.

## Claim scope

In a controlled NumPy tiny neural character-LM proxy with synthetic Python-like code and prose, increasing the code fraction improves held-out code NLL but does not improve the balanced code/prose objective; the 50% code mix was best on mean NLL over three seeds.

## Why it stopped

The local proxy produced a useful mixed signal but is not direct/full validation and is insufficient for paper readiness.

## Recommended next action

Run a bounded deepen test with a real tokenizer and a parameter-matched tiny transformer on real code/prose shards before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer code-mix sweep
- Success threshold: A code-heavy ratio must improve the declared target-weighted aggregate metric versus 50% code by at least 1% relative while not worsening prose loss by more than 3% relative across at least three seeds.
- Stop condition: Stop if all code-heavy ratios improve code loss only by trading off larger prose degradation, or if seed variance exceeds the observed ratio effect.

## Evidence references

- Artifact root: `<local-path>/projects/code-heavy-data-mixing-for-tiny-model-pretraining-d75add838d2a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
