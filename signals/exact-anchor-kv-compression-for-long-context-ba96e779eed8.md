# Exact anchor KV compression for long context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `exact-anchor-kv-compression-for-long-context-ba96e779eed8`
Run ID: `exact-anchor-kv-compression-for-long-context-ba96e779eed8-20260611T021123556867+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/79b0409ff79c

## What looked useful

Full-cache baselines were exact, but anchor-only, mean-block, and optimized-global compressed caches failed the near-exact threshold by large margins: non-anchor retrieval mean relative L2 stayed around 0.95-1.49 and top-1 match stayed 0.0-0.16 across 4x to 63x cache reductions.

## Boundaries and scale limits

No trained transformer, downstream benchmark, multi-layer model, or GPU serving throughput was evaluated; evidence is synthetic but directly tests attention output equivalence.

## Claim scope

At the single-head softmax attention-operation level with synthetic 4096-token caches, exact preservation of anchor-token K/V does not make query-independent non-anchor KV compression exact for non-anchor retrieval queries.

## Why it stopped

Proxy/direct attention-operation early falsification, not a full trained-model validation: preserving anchors exactly did not preserve outputs when non-anchor tokens carried most retrieval attention mass.

## Recommended next action

Stop this exact-anchor-only compression path unless a new mechanism can prove or enforce that future queries attend almost exclusively to exact anchors or can reconstruct non-anchor contributions query-dependently.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-ba96e779eed8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
