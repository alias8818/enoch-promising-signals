# Learned semantic compressor on delayed-memory agent trajectories

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-semantic-compressor-on-delayed-memory-agent-trajec-5bbbc86d9c`
Run ID: `learned-semantic-compressor-on-delayed-memory-agent-trajec-5bbbc86d9c-20260610T123532988221+0000`

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

- Parent run decision: Semantic memory compression to reduce VRAM during agent training: enoch://control-plane/projects/semantic-memory-compression-to-reduce-vram-during-agent-training-0d3a11e65ece/runs/semantic-memory-compression-to-reduce-vram-during-agent-training-0d3a11e65ece-20260610T082636079377+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b85f706b1f3e

## What looked useful

A semantic-slot compressor can preserve delayed trajectory facts when the slot schema matches the environment and capacity is sufficient. The mechanism is not supported for schema-free learned compression or over-capacity compression in this run.

## Boundaries and scale limits

Only synthetic symbolic trajectories were tested. The strongest result depends on exact entity-keyed slots and enough slot capacity. Free-slot learned compressors did not meet the threshold, and a 16-fact/4-slot stress setting failed. No real agent trajectories, natural language summaries, or LLM-context integration were validated.

## Claim scope

Controlled synthetic delayed-memory trajectories with symbolic key/value facts: an engineered key-addressed semantic slot compressor with one slot per entity preserved delayed facts perfectly, while recency and nonsemantic same-budget controls failed.

## Why it stopped

Tier 1 direct evidence produced a useful mechanism signal but is synthetic and schema-engineered, so it is not paper-ready.

## Recommended next action

Run a bounded deepen test that learns the entity-slot schema from richer event records without exact key-addressed slots, using the same recency and mean-bucket controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned schema discovery for semantic compression of delayed trajectory facts
- Success threshold: Mean validation accuracy >= 85% and >= 20 percentage points above the best nonsemantic same-budget control across at least 3 seeds, with slot/entity alignment diagnostics showing nontrivial learned structure.
- Stop condition: Stop as negative if the schema-discovery compressor remains within 10 percentage points of the best nonsemantic control or below 70% mean accuracy after a calibrated small GPU run.

## Evidence references

- Artifact root: `<local-path>/projects/learned-semantic-compressor-on-delayed-memory-agent-trajec-5bbbc86d9c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
