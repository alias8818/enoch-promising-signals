# Direct 32K model needle retrieval with exact-anchor KV retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-32k-model-needle-retrieval-with-exact-anchor-kv-ret-ade8743e95`
Run ID: `direct-32k-model-needle-retrieval-with-exact-anchor-kv-ret-ade8743e95-20260621T020842277712+0000`

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

- Parent run decision: Exact-anchor KV cache preserves needle retrieval at 32K: enoch://control-plane/projects/exact-anchor-kv-cache-preserves-needle-retrieval-at-32k-2536528544d5/runs/exact-anchor-kv-cache-preserves-needle-retrieval-at-32k-2536528544d5-20260621T014822139274+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/736bfc6bce23

## What looked useful

Exact-anchor KV retention carried needle information at long context: at the main 32K run, anchor_tail retained 1,280 of 31,450 prefill tokens, generated the exact answer, and had mean answer logprob -0.1205 versus -8.5587 for tail_only. Replicates showed 2/3 additional 32K seeds exact under anchor_tail and 0/3 under tail_only, but one seed failed exact greedy retrieval despite first-token rank 1.

## Boundaries and scale limits

Single 0.5B instruct model, synthetic haystack, fixed answer string, simple HF cache slicing, 8K/16K/32K prompt targets, four total 32K seeds including the main run; no multi-model benchmark, no production sparse-cache implementation, no broad robustness sweep.

## Claim scope

In a controlled synthetic needle task using Qwen/Qwen2.5-0.5B-Instruct with real CUDA past_key_values up to 31,451 prompt tokens, retaining an exact-anchor KV window plus a recent query tail preserved substantially more answer likelihood than a tail-only dropped-anchor control, and produced exact greedy retrieval in most but not all 32K seeds.

## Why it stopped

Tier 1 direct test completed with mixed useful signal: mechanism support against a dropped-anchor control, but not stable enough for publication readiness.

## Recommended next action

Run a bounded multi-seed/multi-answer 32K sweep comparing retention policies and exact-match rates before any paper claim; stop treating the current simple cache splice as sufficient because one 32K seed failed exact greedy retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 32K exact-anchor KV retention robustness sweep
- Success threshold: Anchor-retention policy reaches at least 90% exact greedy retrieval at 32K, remains within 0.5 nats/token of full-cache forced-answer logprob on average, and beats tail-only by at least 5 nats/token on average.
- Stop condition: Stop as unsupported if anchor-retention exact greedy retrieval is below 75% after 20 trials or if failures persist after one predeclared retention-policy adjustment.

## Evidence references

- Artifact root: `<local-path>/projects/direct-32k-model-needle-retrieval-with-exact-anchor-kv-ret-ade8743e95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
