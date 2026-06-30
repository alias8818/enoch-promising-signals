# Tiny N-gram Draft with Quantized Residual Target

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-n-gram-draft-with-quantized-residual-target-5c6b899a9606`
Run ID: `tiny-n-gram-draft-with-quantized-residual-target-5c6b899a9606-20260607T221346061183+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Best Tiny Shakespeare run improved from 2.8305 to 2.7683 bits/byte versus the matched 3-gram draft and best Python-code run improved from 2.1298 to 2.0425 bits/byte. Oversized residual tables worsened NLL while raising top-1 accuracy, indicating a real overfitting/metric tradeoff.

## Boundaries and scale limits

No neural target model, subword tokenizer, speculative decoding acceptance loop, or GPT-2-class baseline was tested; corpora were small local/Tiny Shakespeare splits and model-size estimates are approximate.

## Claim scope

On two small byte-level held-out corpora, a 3-gram draft distribution plus sparse int8 5-gram residual corrections improved next-token bits-per-byte over the 3-gram-only draft at modest additional storage.

## Why it stopped

Evidence supports the local residual mechanism but remains a proxy byte-level likelihood test, not direct speculative decoding or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded speculative-decoding follow-up with a small neural target and acceptance-rate metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized n-gram residual draft in a small neural speculative decoding loop
- Success threshold: Residual draft must improve target acceptance rate by at least 5% relative or reduce target calls per generated token by at least 5% without worsening output likelihood/perplexity versus the n-gram-only draft at comparable memory.
- Stop condition: Stop if likelihood gains do not translate into acceptance-rate or target-call improvement on either corpus, or if residual storage exceeds the comparable higher-order n-gram baseline without a decoding benefit.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-n-gram-draft-with-quantized-residual-target-5c6b899a9606`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
