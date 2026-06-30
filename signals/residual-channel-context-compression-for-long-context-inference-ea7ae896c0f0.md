# Residual-channel context compression for long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-context-compression-for-long-context-inference-ea7ae896c0f0`
Run ID: `residual-channel-context-compression-for-long-context-inference-ea7ae896c0f0-20260629T131705474981+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/507c09a4d15a

## What looked useful

Energy-selected residual channels are meaningful in the synthetic sparse-salient setting, but the apparent advantage disappears under a fair budget-matched low-rank baseline: sparse-salient mean residual-vs-budget top-1 delta was -0.0010 and mean relative-MSE ratio was 1.0018; isotropic control top-1 delta was -0.0056 and MSE ratio was 1.0023.

## Boundaries and scale limits

No trained transformer, no real language-model task, no production KV-cache runtime, no latency/memory implementation benchmark, and no 7B+/full-scale validation. This is a local CPU proxy, not a publication-grade model result.

## Claim scope

Synthetic attention-level KV-cache compression probe at length 2048, dimension 64, 24 trials per run, 12 grid runs. Residual-channel plus low-rank compression identifies high-energy salient channels and beats random residual selection, but does not beat a parameter-budget-matched low-rank baseline.

## Why it stopped

Budget-matched synthetic attention evidence did not support the core advantage claim; this is an early proxy falsification, not a full validation.

## Recommended next action

Stop this run as a proxy early falsification; only revisit with a direct small-transformer KV-cache experiment against equal-memory low-rank and quantized baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer residual-channel KV compression against equal-memory baselines
- Success threshold: At matched memory budget, residual-channel compression improves retrieval accuracy or perplexity by at least 5% relative over the strongest compressed baseline without worse latency.
- Stop condition: Stop if residual-channel compression is within +/-1% of or worse than equal-memory low-rank/quantized baselines across two seeds and two context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-context-compression-for-long-context-inference-ea7ae896c0f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
