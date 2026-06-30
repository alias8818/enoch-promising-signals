# Ternary Draft Speculative Decode

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ternary-draft-speculative-decode-1c4bc60ce3c0`
Run ID: `ternary-draft-speculative-decode-1c4bc60ce3c0-20260521T201004340881+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c09e02813723

## What looked useful

distilgpt2 ternary drafts had only 4.5% to 12.3% speculative acceptance, total variation around 0.88 to 0.92, and top-10 overlap below 0.09, while the dense draft-equals-target control accepted 100%.

## Boundaries and scale limits

Tested distilgpt2 and sshleifer/tiny-gpt2 only, with 16 fixed prompts, gamma=4, post-training ternarization, and no custom ternary inference kernels or production KV-cache speculative decoder.

## Claim scope

Naive post-training ternarization of a GPT-2-small-class draft copied from the dense target does not preserve enough target-distribution agreement for useful speculative decoding in this bounded local test.

## Why it stopped

Bounded early falsification: the direct speculative-acceptance metric failed on a GPT-2-small-class target, although full production serving speed was only proxied because no ternary kernels were available.

## Recommended next action

Stop this naive post-training ternary draft path; only revisit with a ternary-aware distilled draft and require at least 55% gamma=4 acceptance plus measured or well-supported speedup above 1.15x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ternary-Aware Distilled Draft for Speculative Decoding
- Success threshold: At least 55% speculative acceptance at gamma=4 and measured or kernel-supported projected decode speedup above 1.15x versus dense autoregressive decoding.
- Stop condition: Stop if trained ternary draft acceptance remains below 35% or if measured/projected speedup remains below 1.0x after accounting for draft and verification cost.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-draft-speculative-decode-1c4bc60ce3c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
