# Pretrained GPT-2-small saved-logit speculative decoding equivalence and throughput check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-gpt-2-small-saved-logit-speculative-decoding-eq-fae59c3b37`
Run ID: `pretrained-gpt-2-small-saved-logit-speculative-decoding-eq-fae59c3b37-20260619T031403447433+0000`

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

- Parent run decision: Saved-logit speculative decoding equivalence check on a small transformer: enoch://control-plane/projects/saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027/runs/saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027-20260614T115450339452+0000
- Parent run decision: CPU Speculative Decoding Equivalence Probe: enoch://control-plane/projects/cpu-speculative-decoding-equivalence-probe-d816bc58b4c4/runs/cpu-speculative-decoding-equivalence-probe-d816bc58b4c4-20260614T040712060973+0000

## What looked useful

Saved-logit blocks 2/4/8 matched the cached greedy baseline exactly with 100% acceptance and zero output mismatches. Mean speedups were 1.416x, 2.370x, and 3.541x respectively. A shuffled-logit block-4 control accepted only 1.96% of proposals, had 536 mismatches/fallbacks, and ran at 0.409x baseline speed, supporting that the throughput gain depends on correct saved logits.

## Boundaries and scale limits

CPU-only GPT-2-small, 6 prompts, 3 seeds, 32 generated tokens, greedy decoding, exact context replay, no large saved-logit index, no retrieval overhead beyond in-memory argmax lists, no prompt drift, no sampling, no GPU serving, no batching/concurrency, and no larger-model validation.

## Claim scope

For exact repeated greedy contexts on pretrained GPT-2-small, saved target-logit argmax replay can act as a perfect speculative draft, preserving cached greedy outputs while reducing target calls/token and improving CPU throughput for 32-token continuations over 18 fixed-seed prompt cases.

## Why it stopped

No-paper closure: the mechanism is supported in a narrow direct GPT-2-small replay test, but evidence is not broad or realistic enough for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a persisted saved-logit index, longer continuations, more prompts, exact and near-exact context reuse buckets, and measured lookup/storage overhead before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persisted saved-logit index replay with lookup overhead and longer GPT-2-small continuations
- Success threshold: Exact-match replay has zero output mismatches, at least 95% proposal acceptance, and at least 2x end-to-end throughput versus cached greedy after lookup overhead; near-match buckets must either meet the same equivalence threshold or clearly report rejection/fallback rates.
- Stop condition: Stop if exact-match replay has any uncorrected output mismatch, if end-to-end throughput including lookup overhead is below 1.2x baseline, or if near-match retrieval acceptance falls below 50% without a clear narrower useful claim.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-small-saved-logit-speculative-decoding-eq-fae59c3b37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
