# Early-Exit Self-Speculative Decoding in GPT-2-Small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-in-gpt-2-small-62eb2aaeb201`
Run ID: `early-exit-self-speculative-decoding-in-gpt-2-small-62eb2aaeb201-20260526T093551016210+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ccd8285403a

## What looked useful

Untrained tied-head early exits in GPT-2-small are a poor draft source: all tested configurations exactly matched full greedy output after verification, but every configuration was slower than baseline both in measured wall-clock and in idealized transformer-layer work. Best main-grid acceptance was 5.66%, best measured speedup was 0.67x, and best idealized layer speedup was 0.83x.

## Boundaries and scale limits

Evaluated 16 prompts and 512 generated tokens for the main grid plus a 512-token layer-11 diagnostic on one GB10. The harness is a direct but simple Hugging Face implementation without production KV-cache optimization, sampling-correct speculative decoding, trained exit heads, larger models, or broad benchmark coverage.

## Claim scope

On GPT-2-small greedy decoding with WikiText-2 validation prompts, using untrained intermediate hidden states passed through GPT-2's existing final layer norm and tied LM head as the draft model, self-speculative verification exactly reconstructs full greedy decoding but does not reduce work because draft acceptance is only about 1.2% to 5.7% in the main grid and about 7.0% when skipping only the final transformer block.

## Why it stopped

Direct local evidence is an early falsification of the untrained tied-head mechanism rather than a full validation: acceptance is far too low for speedup, including at layer 11, and idealized layer-work speedup remains below 1.0.

## Recommended next action

Stop this untrained tied-head early-exit path as a no-paper negative result; the only recommended adjacent test is a bounded trained-exit-head experiment with a predeclared acceptance and layer-work threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train lightweight GPT-2-small early-exit heads for self-speculative decoding
- Success threshold: On held-out prompts, exact greedy reconstruction after verification, acceptance at or above 45%, corrections below 55 per 100 generated tokens, and idealized layer-work speedup above 1.10 for at least one exit-layer/draft-length/gating configuration.
- Stop condition: Stop as negative if trained heads remain below 25% acceptance or below 1.0 idealized layer-work speedup after the bounded training budget and one gating ablation.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-in-gpt-2-small-62eb2aaeb201`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
