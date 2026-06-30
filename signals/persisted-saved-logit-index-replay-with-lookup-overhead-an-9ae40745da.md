# Persisted saved-logit index replay with lookup overhead and longer GPT-2-small continuations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `persisted-saved-logit-index-replay-with-lookup-overhead-an-9ae40745da`
Run ID: `persisted-saved-logit-index-replay-with-lookup-overhead-an-9ae40745da-20260619T034008378025+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Pretrained GPT-2-small saved-logit speculative decoding equivalence and throughput check: enoch://control-plane/projects/pretrained-gpt-2-small-saved-logit-speculative-decoding-eq-fae59c3b37/runs/pretrained-gpt-2-small-saved-logit-speculative-decoding-eq-fae59c3b37-20260619T031403447433+0000
- Parent run decision: Saved-logit speculative decoding equivalence check on a small transformer: enoch://control-plane/projects/saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027/runs/saved-logit-speculative-decoding-equivalence-check-on-a-sm-f722a7b027-20260614T115450339452+0000

## What looked useful

Persisted replay exactly matched fresh GPT-2-small greedy continuations for all tested prompts. Fresh baseline decode took 53.2982 s total at 19.21 tok/s; persisted replay took 0.02741 s total at 37,356.74 tok/s, a 1,944.38x speedup. Artifact cost was 216,489 bytes total, or 211.42 bytes per generated token.

## Boundaries and scale limits

Validation was limited to 8 fixed synthetic prompts, 1024 generated tokens total, greedy decoding, top-32 saved logits rather than full-vocabulary logits, a small warm local filesystem index, and CPU-only GPT-2-small execution.

## Claim scope

On a CPU-only local worker, a persisted per-prompt GPT-2-small saved-logit index replayed 8 deterministic greedy continuations of 128 tokens each exactly, with measured disk-backed lookup overhead far below a fresh GPT-2-small decode baseline.

## Why it stopped

The scoped deterministic mechanism is supported, but the evidence is too narrow for publication readiness because it does not validate stochastic replay, full-vocabulary logit persistence, broad prompt distributions, or large-index lookup behavior.

## Recommended next action

Do not write a paper from this run; run one bounded deepen test on 32+ prompts with 256-token continuations, cold/warm lookup separation, and stochastic or full-logit fidelity checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded stochastic and cold-cache saved-logit replay validation
- Success threshold: Deterministic replay exact-match rate remains 100%; persisted warm replay is at least 100x faster than fresh decode; cold replay remains at least 20x faster; stochastic replay reproduces fixed-seed sampling decisions or distribution metrics within the pre-registered tolerance on at least 95% of steps.
- Stop condition: Stop if deterministic exact-match falls below 100%, if cold persisted replay is less than 20x faster than fresh decode, or if stochastic fidelity misses the pre-registered tolerance on more than 5% of steps.

## Evidence references

- Artifact root: `<local-path>/projects/persisted-saved-logit-index-replay-with-lookup-overhead-an-9ae40745da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
