# Tiny On-Device Drafter for CPU Speculative Decoding: GPT-2-87M vs N-gram

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-on-device-drafter-for-cpu-speculative-decoding-gpt-2-87m-vs-n-gram-b46831be2546`
Run ID: `tiny-on-device-drafter-for-cpu-speculative-decoding-gpt-2-87m-vs-n-gram-b46831be2546-20260613T004700903965+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d8268183657c

## What looked useful

N-gram drafting was nearly free but accepted only 4.3% of proposed tokens and slowed decoding to 0.477x. Distilgpt2 accepted 42.1% and halved verifier calls, but CPU draft cost produced a 0.418x slowdown. Neither drafter improved latency over plain gpt2 greedy decoding in this bounded setup.

## Boundaries and scale limits

Not a production mobile runtime, not quantized or compiled inference, not batched serving, not stochastic sampling, and not a broad corpus validation. Distilgpt2 is a readily available proxy for the requested GPT-2-87M-class drafter.

## Claim scope

Bounded CPU/PyTorch greedy decoding microbenchmark with gpt2 target, distilgpt2 GPT-2-87M-class proxy drafter, token n-gram drafter, 6 prompts, 96 generated tokens, block size 4, exact target greedy reproduction required.

## Why it stopped

Bounded direct CPU evidence falsified the practical latency hypothesis for both tested drafters; this is an early scoped falsification, not a full production validation.

## Recommended next action

Stop this run as a useful negative signal; a bounded follow-up should test an int8/compiled sub-50M neural drafter in the same exact-match harness and require at least 1.1x end-to-end CPU speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized sub-50M CPU drafter for GPT-2 speculative decoding
- Success threshold: At least 1.1x end-to-end speedup over target greedy on CPU with exact target greedy reproduction and no more than 2 GiB additional RSS.
- Stop condition: Stop if draft_time plus verifier_time remains slower than 0.9x target greedy after a 96-token smoke or if acceptance stays below 30%.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-on-device-drafter-for-cpu-speculative-decoding-gpt-2-87m-vs-n-gram-b46831be2546`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
