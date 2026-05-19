# Suffix-history speculative decoding in a real KV-cache serving path

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `suffix-history-speculative-decoding-in-a-real-kv-cache-ser-f44e0013af`
Run ID: `suffix-history-speculative-decoding-in-a-real-kv-cache-ser-f44e0013af-20260519T094822777607+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Suffix-history speculative decoding in a real KV-cache serving path: internal_generated:suffix-history-speculative-decoding-in-a-real-kv-cache-ser-f44e0013af

## What looked useful

Natural held-out traffic slowed down: suffix-4 was -2.14% tokens/s with 6.77% acceptance, and suffix-5 was -0.65% with 15.17% acceptance. Replay/overlap traffic had a narrow positive case: suffix-5 reached +1.78% tokens/s with 45.18% acceptance and zero mismatches, while suffix-4 was -1.28%. Random-draft controls were strongly negative, confirming verification/repair overhead dominates unless acceptance is high.

## Boundaries and scale limits

Single small model, single dataset, single GB10 machine, no production batching scheduler, no vLLM/TGI/SGLang paged KV implementation, primary exact-output timing uses fp32 eager attention because fp16/bf16 verification exposed deterministic parity hazards.

## Claim scope

Bounded local validation of suffix-history speculative decoding on distilgpt2 with WikiText-2 prompts, a real Hugging Face KV-cache decode path, greedy target verification, fixed seeds, natural held-out and replay/overlap workloads, and random-draft/no-KV controls.

## Why it stopped

Direct target metrics did not support the broad speedup claim: exact-output suffix-history speculation slowed natural traffic and only produced a small +1.78% replay speedup in the best sequential sweep.

## Recommended next action

Stop this run as no-paper useful signal; the only justified next bounded action is a production-style copy-on-write KV and deterministic fp16 acceptance test with an explicit >=5% replay speedup and nonnegative natural-traffic overhead threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style copy-on-write KV suffix-history speculation with deterministic fp16 acceptance
- Success threshold: Zero exact-output mismatches, natural held-out throughput no worse than greedy KV baseline, and replay/overlap throughput at least 5% faster than greedy KV baseline with random-draft control remaining negative.
- Stop condition: Stop if exact parity cannot be maintained in fp16/bf16, if natural held-out traffic remains slower than baseline, or if replay/overlap speedup remains below 5% after copy-on-write KV branching.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-history-speculative-decoding-in-a-real-kv-cache-ser-f44e0013af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
