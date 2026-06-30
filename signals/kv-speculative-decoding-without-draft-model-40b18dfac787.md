# KV-Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-speculative-decoding-without-draft-model-40b18dfac787`
Run ID: `kv-speculative-decoding-without-draft-model-40b18dfac787-20260619T062022170479+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/224517be825a

## What looked useful

Batched target suffix verification is cheap on GB10, but the strict no-draft/no-head/no-approximate-pass proposer is the weak link. The broad idea needs a stronger proposal mechanism; current KV/logits alone were insufficient except in repetitive degenerate traces.

## Boundaries and scale limits

Evaluated only distilgpt2 and gpt2 on 24 fixed prompts with 64 greedy tokens each. No sampling, no 7B+ models, no production end-to-end decoder with KV cache commit/rollback, and no standard benchmark corpus.

## Claim scope

Small GPT-2-class greedy decoding probe on GB10: current-logit-only draft-free proposal rules are not robust future-token predictors. A repeated-current-token policy can exploit repetitive traces, but local top-k policies and gpt2 results show near-zero future acceptance.

## Why it stopped

Early bounded falsification of the broad mechanism: proxy acceptance/timing evidence does not support robust draft-free KV speculative decoding, and full validation would require an implemented decoder plus larger benchmarks.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, implement a real lossless KV cache commit/rollback decoder and test a stronger non-trained proposer against lookahead and self-speculative baselines on a standard prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end lossless lookahead baseline for draft-free KV speculation
- Success threshold: At least 1.2x end-to-end tokens/sec over autoregressive decoding on gpt2-class or larger models with exact greedy output equivalence and mean future accepted beyond current argmax >= 0.5 on non-repetitive prompts.
- Stop condition: Stop if exact output equivalence fails, cache rollback overhead erases speedup, or future-token acceptance remains below 0.2 on non-repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-speculative-decoding-without-draft-model-40b18dfac787`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
