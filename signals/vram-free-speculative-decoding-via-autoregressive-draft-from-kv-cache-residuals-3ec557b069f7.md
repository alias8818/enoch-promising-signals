# VRAM-free speculative decoding via autoregressive draft from KV-cache residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vram-free-speculative-decoding-via-autoregressive-draft-from-kv-cache-residuals-3ec557b069f7`
Run ID: `vram-free-speculative-decoding-via-autoregressive-draft-from-kv-cache-residuals-3ec557b069f7-20260605T135358057018+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/4be1fc6fa736

## What looked useful

A 512-dimensional projected KV probe reached 43.6% top-1 target-greedy agreement versus 10.4% unigram control; a 1024-dimensional probe reached 47.3% top-1 but still missed the approximate 52% threshold for one optimistic expected accepted token at draft length 4. The best probe also requires about 103 MB fp16 parameters for GPT-2 small, so it is not truly weight-free.

## Boundaries and scale limits

Single-token greedy-agreement proxy only; GPT-2 small only; no end-to-end speculative decoding loop, no sampling acceptance test, no 1B+ or 7B+ target model, and no production-prompt validation.

## Claim scope

On GPT-2 small with WikiText-2 validation contexts, a learned linear readout from target-model KV-cache tensors contains a strong next-token signal but did not reach the predeclared greedy speculative-decoding usefulness threshold.

## Why it stopped

Early proxy falsification of the practical VRAM-free speculative-decoding claim: the KV readout learned signal but did not meet the predeclared acceptance proxy threshold, and the stronger probe still adds nontrivial parameters.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should put a low-rank or candidate-restricted KV readout into an actual greedy speculative decoding loop and require at least 10% wall-clock speedup over vanilla decoding at equal outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end low-rank KV-readout speculative decoding loop
- Success threshold: At least 10% wall-clock throughput improvement over vanilla greedy decoding at identical generated outputs, with added readout weights below 25 MB fp16 and mean accepted draft tokens at least 1.0 for draft length 4.
- Stop condition: Stop as negative if the end-to-end loop is slower than vanilla decoding, if greedy outputs diverge, or if reducing the readout below 25 MB fp16 drops mean accepted draft tokens below 1.0.

## Evidence references

- Artifact root: `<local-path>/projects/vram-free-speculative-decoding-via-autoregressive-draft-from-kv-cache-residuals-3ec557b069f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
