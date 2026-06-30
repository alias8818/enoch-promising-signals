# Suffix-Array Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `suffix-array-speculative-decoding-on-cpu-17f6e9f34aea`
Run ID: `suffix-array-speculative-decoding-on-cpu-17f6e9f34aea-20260608T035228888969+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48a4ed233ae9

## What looked useful

Suffix-array retrieval occasionally finds repeated continuations, but the accepted-token yield is far below one token/query at p95 1, while hash n-gram lookup provides similar yield at 14-55x lower lookup latency in this bounded CPU proxy.

## Boundaries and scale limits

This was a Python prototype on Tiny Shakespeare and Alice in Wonderland with exact held-out matching, not an optimized C/C++ implementation and not an end-to-end target-language-model speculative decoding benchmark.

## Claim scope

On two small public-text held-out splits using exact continuation recovery as a proxy for speculative acceptance, suffix-array retrieval is not a compelling general CPU draft source: it recovers only 0.14-0.22 accepted tokens/query and is much slower than a hash n-gram control.

## Why it stopped

Early proxy falsification: exact held-out continuation yield was too low and suffix-array lookup overhead was much worse than a simpler CPU hash baseline; this is not a full validation of all optimized/domain-specific variants.

## Recommended next action

Stop this general suffix-array CPU path unless a future direct LM-serving test uses an optimized implementation and demonstrates >1 accepted token/query plus net wall-clock speedup over hash n-gram retrieval.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-on-cpu-17f6e9f34aea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
