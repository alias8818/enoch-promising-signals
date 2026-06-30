# Early-Exit Self-Speculative Decoding Without Draft Model VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-without-draft-model-vram-edfa2f95bba2`
Run ID: `early-exit-self-speculative-decoding-without-draft-model-vram-edfa2f95bba2-20260524T002252977218+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f4f74a40b8f0

## What looked useful

On distilgpt2 the best always-draft exit was layer 5/6 with 40.4% top-1 agreement and an optimistic 0.152x greedy-speed estimate. On gpt2 the best always-draft exit was layer 11/12 with 56.5% agreement and an optimistic 0.250x estimate. Confidence-gated near-final exits reached 100% agreement on roughly 5% of positions but still stayed below 1.0x because the exits were too late.

## Boundaries and scale limits

Tested sshleifer/tiny-gpt2 only as a smoke check, plus distilgpt2 and gpt2 on 20 short prompts with max length 64. Latency was estimated analytically from layer fraction and acceptance, not measured in a production KV-cache decoder. No 7B+ model, large corpus, trained exit head, or end-to-end serving stack was validated.

## Claim scope

Unmodified GPT-2-family models using intermediate hidden states plus the final lm_head as a no-extra-VRAM draft source do not produce enough greedy-token agreement to beat greedy decoding under an optimistic block-4 speculative cost model on this bounded prompt probe.

## Why it stopped

Proxy/early falsification: the directly measured early-exit agreement is too low, and even confidence-gated positions fail the optimistic speed threshold before real decoder overhead.

## Recommended next action

Stop this naive untrained-lm_head path as an early bounded falsification; only continue if the next run trains or calibrates early-exit heads and benchmarks a real KV-cache self-speculative decoder against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Early-Exit Heads for No-Draft-Model Self-Speculation
- Success threshold: At least one exit at <=50% depth achieves measured wall-clock speedup >1.10x over greedy decoding with identical greedy outputs on held-out prompts, while adding <5% model memory overhead.
- Stop condition: Stop if held-out <=50% depth top-1 agreement remains below 80%, or if the end-to-end decoder does not exceed 1.0x greedy speed after accounting for KV-cache and control overhead.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-without-draft-model-vram-edfa2f95bba2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
