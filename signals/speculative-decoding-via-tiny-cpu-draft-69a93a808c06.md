# Speculative Decoding via Tiny CPU Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-via-tiny-cpu-draft-69a93a808c06`
Run ID: `speculative-decoding-via-tiny-cpu-draft-69a93a808c06-20260528T013233263659+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

Across four 2,500-token replicate runs, the unigram draft achieved 0.966-0.976 mean acceptance and 2.88x-7.87x target-call reduction for gamma 2-8 with sub-0.01 ms measured break-even target latency. Larger n-gram drafts were not automatically better: order-1/order-2 drafts had lower acceptance and higher overhead, while order-3 recovered some acceptance but still carried higher CPU overhead.

## Boundaries and scale limits

No transformer target, no tokenizer-level model, no GPU/batched verification, no CPU/GPU overlap, and no real serving stack were tested. Results are proxy evidence only and cannot support a paper-ready LLM serving speedup claim.

## Claim scope

CPU-only character-level n-gram proxy showing exact speculative decoding acceptance, target-call reduction, and draft-overhead break-even behavior for tiny CPU draft models against a higher-order target n-gram model.

## Why it stopped

No-paper closure: the run supports the mechanism only in a CPU n-gram proxy and lacks direct transformer/GPU serving evidence.

## Recommended next action

Stop this run as a proxy useful signal; the next concrete action is a bounded direct serving test with a real tokenizer, transformer target, CPU draft, and GPU or accelerated target verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct transformer speculative decoding with a CPU draft
- Success threshold: At least 1.2x end-to-end tokens/s improvement over target-only generation with unchanged target-sampling distribution, mean acceptance above 0.6, and CPU draft plus synchronization overhead below 25% of saved target time.
- Stop condition: Stop as negative if acceptance is below 0.4 or end-to-end speedup is below 1.0x in two representative prompt distributions after basic gamma tuning.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-via-tiny-cpu-draft-69a93a808c06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
