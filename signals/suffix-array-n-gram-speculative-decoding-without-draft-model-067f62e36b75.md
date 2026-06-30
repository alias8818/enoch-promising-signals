# Suffix-Array N-gram Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculative-decoding-without-draft-model-067f62e36b75`
Run ID: `suffix-array-n-gram-speculative-decoding-without-draft-model-067f62e36b75-20260524T233241419912+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cd361cc01529

## What looked useful

On 325k local documentation tokens, suffix-array global lookup raised mean accepted prefix from 2.5443 to 2.8194 tokens versus a 4096-token window n-gram baseline, increasing ideal target-call yield from 3.5443 to 3.8194. On a long-gap synthetic repeat control, suffix-array lookup achieved 0.6450 mean accepted tokens while the window baseline achieved 0.

## Boundaries and scale limits

No live LLM serving was benchmarked; no GPU target verification, online suffix-array update, batching, KV-cache, stochastic decoding, or 7B+ model traces were tested. The suffix-array prototype is unoptimized Python and slower than the preindexed window baseline in evaluation time.

## Claim scope

Trace-level evidence shows that a global suffix-array n-gram proposer can recover repeated continuations without a draft model and can beat a 4096-token recent-window n-gram cache on local documentation traces and long-gap repeat controls.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a proxy token-trace benchmark, not direct serving-speed validation.

## Recommended next action

Run a bounded live decoding follow-up on a small open model with end-to-end tokens/sec, online index maintenance, and generated traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live small-model suffix-array n-gram speculative decoding benchmark
- Success threshold: At least 10% end-to-end tokens/sec improvement over both no-speculation and recent-window n-gram baselines on a repetitive/code/doc workload, with no regression larger than 5% on a non-repetitive workload.
- Stop condition: Stop if online index overhead eliminates throughput gains or if accepted-prefix lift over the recent-window baseline is below 0.2 tokens/call on generated traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculative-decoding-without-draft-model-067f62e36b75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
