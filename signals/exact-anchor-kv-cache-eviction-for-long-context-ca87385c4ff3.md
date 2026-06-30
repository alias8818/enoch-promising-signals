# Exact Anchor KV-Cache Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-cache-eviction-for-long-context-ca87385c4ff3`
Run ID: `exact-anchor-kv-cache-eviction-for-long-context-ca87385c4ff3-20260620T020428215468+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/86bb76839617

## What looked useful

Exact-anchor KV retention matched an oracle target-retention policy for anchor facts, with 1.0 target retention and 1.0 top-1 target retrieval at both 6.25% and 1.56% retained-cache budgets. It failed on old non-anchor facts with 0.0 top-1 retrieval, showing the mechanism is anchor-coverage-limited.

## Boundaries and scale limits

No real decoder model, learned anchor selector, real prompts, multi-layer cache dynamics, latency benchmark, or comparison to production KV compression implementations. Evidence is synthetic and mechanism-level.

## Claim scope

Synthetic attention-cache selection with irregular preselected anchors at sequence length 8192 and fixed KV budgets of 512 and 128. Exact-anchor retention preserves queried old facts only when those facts are designated anchors.

## Why it stopped

Proxy mechanism result only: it supports deterministic retention of preselected anchors but early-falsifies any broad claim that exact anchors recover arbitrary old context without a reliable anchor-selection mechanism.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, test the same policy inside a small decoder generation loop on synthetic needle retrieval with equal-budget baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-decoder exact-anchor KV eviction on equal-budget needle retrieval
- Success threshold: At equal KV budget, exact-anchor retention improves marked-needle retrieval accuracy by at least 20 percentage points over recent-only and periodic/random baselines without improving unmarked controls by selection leakage.
- Stop condition: Stop if exact-anchor retention does not beat recent-only by at least 10 percentage points on marked needles, or if the implementation cannot enforce equal retained KV budgets.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-cache-eviction-for-long-context-ca87385c4ff3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
