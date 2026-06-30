# Suffix Array Speculative Decode for GPT2 Speedup

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `suffix-array-speculative-decode-for-gpt2-speedup-09bf72a4c083`
Run ID: `suffix-array-speculative-decode-for-gpt2-speedup-09bf72a4c083-20260607T031837977299+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae5d5ea133b6

## What looked useful

Suffix-array lookup is cheap and can hit short contexts, but matches were mostly 2-token contexts and continuations diverged from GPT-2 quickly; retrieval alone did not create enough accepted draft length for a practical speedup claim.

## Boundaries and scale limits

This was a bounded local probe, not a production speculative decoding implementation. It used GPT-2 small, WikiText-2, up to 120000 suffix-index tokens, 1024 eval tokens, greedy target predictions, and an idealized speedup model rather than end-to-end KV-cache decoding throughput.

## Claim scope

On WikiText-2 with GPT-2 greedy verification, a token suffix-array retriever over 120000 training tokens produced only 0.126 accepted draft tokens per eval step at gamma 4/8, for a 1.126x idealized target-call speedup upper bound before real serving overheads.

## Why it stopped

Bounded direct GPT-2 acceptance testing plus an idealized speedup proxy gave an early falsification of the practical suffix-array-only speedup hypothesis, not a full production validation.

## Recommended next action

Stop this no-paper line unless a future run adds a stronger in-domain or model-aware draft selector and requires >1.3x measured end-to-end decoding throughput to reopen the speedup claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decode-for-gpt2-speedup-09bf72a4c083`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
