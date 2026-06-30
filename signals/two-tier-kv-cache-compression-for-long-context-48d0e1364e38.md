# Two-tier KV cache compression for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-tier-kv-cache-compression-for-long-context-48d0e1364e38`
Run ID: `two-tier-kv-cache-compression-for-long-context-48d0e1364e38-20260629T044051965388+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7b7caee9d55

## What looked useful

Block-only old KV compression reached 12.96x compression at 8k but 0.000 retrieval accuracy, matching recent-only truncation. Adding 128 oracle-salient old exact entries with 64-token old block centroids reached 10.81x compression and 0.804 retrieval accuracy at 8k; random old retention reached only 0.004.

## Boundaries and scale limits

No real transformer layers, learned salience estimator, GPU kernel, latency measurement, generation quality benchmark, or production serving workload was tested.

## Claim scope

Synthetic attention-level proxy over 2k and 8k KV caches: naive old-token block-centroid compression fails rare old-fact retrieval, while an oracle exact old-token salience tier plus compressed old summaries can preserve much of retrieval at high KV-entry compression.

## Why it stopped

Bounded synthetic proxy produced useful mechanism evidence but not direct transformer or serving validation; naive block-only two-tier compression is early-falsified for rare old-fact retrieval in this setup.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement learned or online salience selection inside a small transformer attention module and compare quality/memory against exact KV and recent-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned salience tier for two-tier KV compression in a small transformer
- Success threshold: At 4x or better KV memory reduction, learned salience two-tier KV should recover at least 80% of the full-exact retrieval accuracy and outperform random retention by at least 20 percentage points on old-fact queries.
- Stop condition: Stop if learned salience does not beat random retention by 10 percentage points at matched memory or if overhead removes the practical memory/latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/two-tier-kv-cache-compression-for-long-context-48d0e1364e38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
