# Self-Speculative Decoding via Early Exit

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-3adf32055b94`
Run ID: `self-speculative-decoding-via-early-exit-3adf32055b94-20260602T123844432236+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7195814c2f2d

## What looked useful

GPT-2 small early exits accepted only 3.6-5.9% of drafted tokens, produced only 1.14-1.23 emitted tokens per verification cycle, and had layer-work speedup proxies below 1.0 for every tested exit; best proxy was 0.691x at layer 2.

## Boundaries and scale limits

Tested one 124M-parameter GPT-2 model, greedy decoding only, 24 fixed English prompts, 1152 generated tokens, exits 2/4/6/8/10, draft length 4, and an unoptimized no-KV-cache harness. Does not evaluate models trained with auxiliary early-exit losses or production serving kernels.

## Claim scope

Naive greedy self-speculative decoding using untrained pretrained GPT-2-small intermediate states projected through the final LM head does not produce enough accepted tokens to reduce layer work on the tested prompts.

## Why it stopped

Proxy/early falsification, not full validation: direct GPT-2-small acceptance and layer-work metrics show the untrained early-exit draft mechanism is below the speedup threshold.

## Recommended next action

Stop this naive pretrained-head path; the only concrete bounded next action is to train or load auxiliary early-exit LM heads and repeat the same verifier acceptance test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Auxiliary-trained early-exit heads for self-speculative GPT-2 decoding
- Success threshold: At least one exit/draft-length setting achieves >=1.1x layer-work proxy with exact greedy output preservation and stable acceptance on held-out prompts.
- Stop condition: Stop if trained auxiliary heads remain below 1.0x layer-work proxy or accepted tokens per cycle stays below 1.5 on held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-3adf32055b94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
