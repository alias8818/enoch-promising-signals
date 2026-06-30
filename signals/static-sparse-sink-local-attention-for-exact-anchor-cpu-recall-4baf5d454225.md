# Static sparse sink-local attention for exact anchor CPU recall

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `static-sparse-sink-local-attention-for-exact-anchor-cpu-recall-4baf5d454225`
Run ID: `static-sparse-sink-local-attention-for-exact-anchor-cpu-recall-4baf5d454225-20260525T152911009693+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a571a18fae2a

## What looked useful

Dense attention reached all anchors in 20/20 controls. Static sink-local reached all anchors only when the sink prefix plus local receptive field covered the full pre-query prefix; otherwise middle anchors were invisible. At sequence length 8192, only 4/60 sink-local sweep configurations had all-anchor reachability, and a representative N=8192, L=32, W=64, S=16 setup covered only 25.2% of anchors with 6127 far anchors unreachable.

## Boundaries and scale limits

No trained language models or large-corpus benchmarks were run. The evidence is structural and synthetic: it proves a necessary-condition failure for unreachable anchors, but does not measure quality or throughput for configurations where L * W plus sinks covers the whole tested context.

## Claim scope

For causal transformers using a static sink-local mask, arbitrary exact anchor recall is structurally impossible for anchor positions outside the fixed sink prefix and outside the L * W local receptive field behind the query. The result is a deterministic reachability analysis over sequence lengths 128-8192, layers 2-32, local windows 16-256, and sink counts 0-64.

## Why it stopped

Structural early falsification: for unreachable anchors, the final query representation is invariant to the anchor token under the tested static causal mask, so training cannot produce exact arbitrary-anchor recall. This is not a full language-model validation.

## Recommended next action

Stop this static sink-local exact-recall line unless the design guarantees L * W plus sink coverage spans the target context; pursue dynamic or content-addressed sparse routing as a separate idea if exact arbitrary-anchor recall remains the goal.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/static-sparse-sink-local-attention-for-exact-anchor-cpu-recall-4baf5d454225`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
