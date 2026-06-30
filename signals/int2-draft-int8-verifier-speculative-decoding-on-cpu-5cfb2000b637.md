# INT2 draft + INT8 verifier speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int2-draft-int8-verifier-speculative-decoding-on-cpu-5cfb2000b637`
Run ID: `int2-draft-int8-verifier-speculative-decoding-on-cpu-5cfb2000b637-20260630T063242139734+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff1ce5b8c3a

## What looked useful

Verifier batching scaled up to 7.65x positions/s at batch 8 in the main run, but the speculative loop still peaked at 0.885x greedy INT8 throughput. Sensitivity runs peaked at 0.731x and 0.679x, so the local proxy is an early negative for a same-shape INT2 draft on CPU.

## Boundaries and scale limits

Not a full transformer benchmark; no fused packed-INT2 kernel, KV cache, tokenizer, real prompts, or smaller draft model was tested. Runs used dim=768, vocab=4096, 96 generated tokens, and logit-scale sensitivity at 1.0, 4.0, and 8.0.

## Claim scope

Bounded synthetic CPU proxy for quantization-only speculative decoding where an INT2 draft and INT8 verifier have the same matrix shape; no tested draft length or logit sharpness produced an end-to-end speedup over greedy INT8.

## Why it stopped

Proxy early falsification, not full validation: the tested CPU proxy showed no speedup in all bounded sweeps despite verifier batch scaling.

## Recommended next action

Stop this proxy run; the next bounded direct test is a llama.cpp-style CPU implementation with a real INT8 verifier, actually cheaper INT2 or smaller draft, and counters for draft cost, verifier calls, acceptance, and generated tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM speculative decoding benchmark with a cheaper INT2 draft
- Success threshold: At least 1.15x generated tokens/s versus greedy INT8 with no quality-invalidating acceptance shortcut and with draft cost below 25% of verifier cost per proposed token.
- Stop condition: Stop if the real implementation cannot exceed 1.0x greedy INT8 in two prompt-length regimes or if acceptance falls below 70% at the draft length needed for speedup.

## Evidence references

- Artifact root: `<local-path>/projects/int2-draft-int8-verifier-speculative-decoding-on-cpu-5cfb2000b637`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
