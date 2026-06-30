# On-device draft-model selector for speculative decoding: pick best draft per request class on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `on-device-draft-model-selector-for-speculative-decoding-pick-best-draft-per-request-class-on-gb1-69d24c84d616`
Run ID: `on-device-draft-model-selector-for-speculative-decoding-pick-best-draft-per-request-class-on-gb1-69d24c84d616-20260619T170423834766+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1312b6fa4da

## What looked useful

The tested draft pool had no useful class specialization: distilgpt2 was best in every class, tiny-gpt2 had near-zero acceptance, and target-only greedy decoding was faster than both speculative variants. Future selector work should first establish a draft pool with a real latency/acceptance Pareto frontier.

## Boundaries and scale limits

Short greedy continuations only; small GPT-2-class target; two draft candidates; no optimized KV-cache serving kernel; synthetic prompt classes rather than production traffic; no request classifier overhead measurement.

## Claim scope

On GB10, using GPT-2 as target and sshleifer/tiny-gpt2 plus distilgpt2 as GPT-2-tokenizer draft candidates over four hand-built request classes, a per-class draft selector did not improve over the best fixed draft and speculative decoding was slower than target-only greedy decoding in the bounded harness.

## Why it stopped

Bounded proxy and longer persistence check both found 0% class-selector improvement over the best fixed draft and slower-than-target speculative decoding, so the current hypothesis is unsupported rather than ready for paper writing.

## Recommended next action

Stop this run as a no-paper useful negative; a bounded deepen follow-up should use optimized KV-cache speculative decoding and at least four draft candidates before revisiting request-class selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache draft-pool Pareto test for GB10 request-class speculative decoding
- Success threshold: Class selector is at least 5% faster than the best fixed draft on mean or p95 latency and faster than target-only generation, with at least one class choosing a non-global-best draft.
- Stop condition: Stop negative if one draft dominates every class again or if optimized speculative decoding remains slower than target-only generation.

## Evidence references

- Artifact root: `<local-path>/projects/on-device-draft-model-selector-for-speculative-decoding-pick-best-draft-per-request-class-on-gb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
