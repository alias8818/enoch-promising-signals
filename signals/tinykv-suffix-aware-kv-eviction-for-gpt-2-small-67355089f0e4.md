# TinyKV: Suffix-Aware KV Eviction for GPT-2 Small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tinykv-suffix-aware-kv-eviction-for-gpt-2-small-67355089f0e4`
Run ID: `tinykv-suffix-aware-kv-eviction-for-gpt-2-small-67355089f0e4-20260609T030217455644+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Suffix-aware retention based on recent-suffix attention did not improve over suffix-only sliding context. All tested suffix-aware variants raised mean NLL versus suffix-only, with more losses than wins across examples.

## Boundaries and scale limits

Not a production KV-cache implementation; selected tokens are compacted for re-scoring, salience uses a full-context attention pass, and no long-generation latency or quality benchmark was run.

## Claim scope

Bounded proxy GPT-2-small next-token NLL evaluation on 80 WikiText-2 test stream positions with 384-token full context and compacted budgets K=64 and K=128.

## Why it stopped

Bounded proxy early falsification rather than full validation: suffix-aware compacted-context scoring underperformed suffix-only for K=64 and K=128 on GPT-2-small/WikiText-2.

## Recommended next action

Stop this exact TinyKV suffix-attention salience policy as a paper direction; only revisit with a genuinely different KV-cache mechanism that preserves positional semantics and has a direct implementation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tinykv-suffix-aware-kv-eviction-for-gpt-2-small-67355089f0e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
