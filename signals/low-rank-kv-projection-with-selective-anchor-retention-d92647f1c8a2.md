# Low-Rank KV Projection with Selective Anchor Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-projection-with-selective-anchor-retention-d92647f1c8a2`
Run ID: `low-rank-kv-projection-with-selective-anchor-retention-d92647f1c8a2-20260530T021953454309+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e595c1ffba14

## What looked useful

Exact anchor retention is highly effective when retained anchors carry the dense attention mass, but naive high-key-norm selection can waste budget and underperform uniform low-rank compression on smooth low-rank traces or misleading high-norm distractors.

## Boundaries and scale limits

No trained model, real-token perplexity, long-context retrieval, online projection cost, decode latency, quantization, or multi-layer transformer interactions were tested.

## Claim scope

CPU-only synthetic attention-output reconstruction proxy for KV-cache compression at comparable scalar-element budgets.

## Why it stopped

Proxy experiment found conditional support for the mechanism but early falsification of naive norm-based selective anchors as a robust standalone method; this is not full validation.

## Recommended next action

Run a bounded real-token follow-up with a query/history-based anchor selector on a tiny or GPT-2-small-class model; stop here for this run because the current evidence is proxy-only and mixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token test of query-aware selective KV anchor retention
- Success threshold: At matched cache budget, query/history-aware selective anchors reduce attention-output relative MSE by at least 25% versus low-rank-only and do not worsen perplexity or retrieval accuracy by more than 2% relative to the better compressed baseline.
- Stop condition: Stop if the query/history selector fails to beat low-rank-only on reconstruction in two real-token regimes or if quality loss exceeds the threshold despite reconstruction gains.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-projection-with-selective-anchor-retention-d92647f1c8a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
