# Low-rank KV factorization with 4-bit doubles effective context on 1B

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-factorization-with-4-bit-doubles-effective-context-on-1b-6524b85d8519`
Run ID: `low-rank-kv-factorization-with-4-bit-doubles-effective-context-on-1b-6524b85d8519-20260530T011901006594+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e6f3dc984d66

## What looked useful

Memory compression is mechanically plausible, but 4-bit factor quantization produced an approximately 20% attention-output relative-error floor even at full rank for D=512. Direct per-channel int4 KV used 0.25x bf16 memory and had lower mean attention-output error, about 0.14-0.16 across regimes, than low-rank int4 factors.

## Boundaries and scale limits

No real 1B checkpoint, no real transformer KV activations, no perplexity/retrieval benchmark, and no production KV-cache kernel were tested. Results use controlled synthetic spectra plus random full-rank controls.

## Claim scope

Bounded GPU proxy at T=4096, D=512 shows low-rank signed-int4 KV factors easily meet the <=0.5 memory ratio needed to double a Llama-1B-like KV-cache budget, but preserve attention outputs poorly enough that a direct per-channel int4 KV baseline is better at comparable memory.

## Why it stopped

No-paper useful signal: this proxy is an early falsification of the low-rank 4-bit quality mechanism, not a full long-context validation.

## Recommended next action

Run a bounded real-activation follow-up on a GPT-2-small or 1B-class checkpoint comparing low-rank 4-bit factors against direct int4 KV at equal memory before spending on long-context training or serving validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation low-rank int4 KV versus direct int4 KV
- Success threshold: Low-rank 4-bit factors reduce attention-output error or end-to-end quality loss by at least 25% versus direct int4 KV at the same memory ratio <=0.5.
- Stop condition: Stop if direct int4 KV matches or beats low-rank 4-bit factors on both attention-output error and end-to-end quality under equal memory accounting.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-factorization-with-4-bit-doubles-effective-context-on-1b-6524b85d8519`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
