# StreamingKV with sinks extends context on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `streamingkv-with-sinks-extends-context-on-gb10-95bcf1781c71`
Run ID: `streamingkv-with-sinks-extends-context-on-gb10-95bcf1781c71-20260522T155724413234+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bab4ca2ce6b9

## What looked useful

Attention sinks are useful as retained anchors in bounded StreamingKV, but they should not be treated as extending arbitrary context: old facts outside the sink prefix and recent window were lost at the same rate as recent-only eviction.

## Boundaries and scale limits

No real language model, no perplexity/downstream task, no production serving backend, and only sampled synthetic key retrieval up to 32,768 tokens with d_head=128.

## Claim scope

Synthetic GB10 cache-policy probe: preserving 4 sink tokens plus a 512-token recent window keeps sink-prefix retrieval at 100% through 32,768 tokens while using about 1.57% of full KV positions, but it does not improve arbitrary old-token retrieval over a recent-only cache.

## Why it stopped

Closed as a no-paper useful signal: the synthetic mechanism supports sink-anchor retention but explicitly falsifies arbitrary old-context retention for this cache policy.

## Recommended next action

Run a bounded direct LM evaluation with full KV, recent-only eviction, and sink-plus-recent eviction on long-context retrieval/perplexity tasks before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LM evaluation of StreamingKV sinks on long-context retrieval
- Success threshold: At equal KV budget, sink-plus-recent must beat recent-only on stability/perplexity or sink-position retrieval while matching recent-only on recent-token tasks; it must not claim success on arbitrary old facts unless those improve over recent-only.
- Stop condition: Stop if sink-plus-recent does not improve over recent-only on direct LM metrics, or if gains appear only on synthetic/prompts where the answer is deliberately placed in sink positions.

## Evidence references

- Artifact root: `<local-path>/projects/streamingkv-with-sinks-extends-context-on-gb10-95bcf1781c71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
