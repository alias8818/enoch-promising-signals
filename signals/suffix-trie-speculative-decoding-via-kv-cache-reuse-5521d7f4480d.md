# Suffix-Trie Speculative Decoding via KV-Cache Reuse

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-trie-speculative-decoding-via-kv-cache-reuse-5521d7f4480d`
Run ID: `suffix-trie-speculative-decoding-via-kv-cache-reuse-5521d7f4480d-20260629T173101925922+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/101a628c8c88

## What looked useful

The exact suffix-trie KV reuse premise fails a correctness prerequisite for standard decoder-only transformers because suffix hidden states, and therefore deeper-layer K/V entries, depend on the left prefix. In a 4-layer probe only 0.25 of suffix K/V vectors were exactly reusable, matching the first-layer-only mechanism; controls remained exact.

## Boundaries and scale limits

Synthetic random-weight tiny transformers only; no pretrained GPT-2/7B model, real prompt corpus, serving engine integration, or end-to-end speculative decoding latency benchmark was run.

## Claim scope

Deterministic tiny causal-transformer probes show that exact cross-prefix suffix KV-cache reuse is not valid beyond the first layer: identical suffix tokens after different prefixes produce different deeper-layer K/V tensors and changed suffix logits.

## Why it stopped

Closed as a no-paper useful signal: the local synthetic probe is an early correctness falsification of exact cross-prefix suffix KV reuse, not full production-scale validation.

## Recommended next action

Run a bounded pretrained GPT-2-small deepen test that measures exact K/V equality, logit KL, and top-k/top-1 disruption under approximate suffix reuse; stop if divergent-prefix top-1 mismatch stays above 1% or exact K/V equality remains limited to layer 0.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 Small Suffix-KV Reuse Error Probe
- Success threshold: Confirm exact K/V equality is restricted to layer 0 and divergent-prefix top-1 mismatch exceeds 1% or top-5 overlap drops below 99% on at least 1,000 suffix positions.
- Stop condition: Stop if pretrained-model divergent-prefix metrics match identical-prefix controls within numerical tolerance, or if model/download/runtime issues prevent collecting at least 1,000 suffix positions in under 15 minutes.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-speculative-decoding-via-kv-cache-reuse-5521d7f4480d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
