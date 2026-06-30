# Robustness sweep for attention-quality KV retention on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robustness-sweep-for-attention-quality-kv-retention-on-gpt-8388bce6ca`
Run ID: `robustness-sweep-for-attention-quality-kv-retention-on-gpt-8388bce6ca-20260612T230857420285+0000`

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

- Parent run decision: KV-Cache Sliding-Window Eviction with Quality-Weighted Retention on GPT-2-Small: enoch://control-plane/projects/kv-cache-sliding-window-eviction-with-quality-weighted-retention-on-gpt-2-small-3739fa48aef3/runs/kv-cache-sliding-window-eviction-with-quality-weighted-retention-on-gpt-2-small-3739fa48aef3-20260612T224834941193+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Attention quality alone is not a robust KV retention policy for GPT-2-small, but combining attention-received scores with mandatory recent-token retention produced a repeatable small improvement over recency in this controlled cache-degradation test.

## Boundaries and scale limits

24 samples per context length, context lengths 128/192/256, next-token-only evaluation, zeroed KV slots rather than true sparse cache compaction, one pretrained GPT-2-small model, WikiText-2 validation only, no throughput or memory benchmark.

## Claim scope

Small direct GPT-2-small cached-inference test on WikiText-2 validation chunks: pure attention-received KV retention is worse than recency, while attention-received retention with a forced recent tail modestly reduces next-token NLL drift versus recency at 20-50% retention under KV-slot zeroing.

## Why it stopped

Tier 1 direct validation completed; evidence is useful but mixed and not paper-positive because pure attention-quality retention failed against recency and the hybrid positive signal is limited to small next-token cache-zeroing sweeps.

## Recommended next action

Run a bounded deepen test using true sparse KV compaction and 8-16 token continuations on GPT-2-small to verify whether the attention-plus-recent signal survives without zeroed-slot softmax artifacts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True sparse KV compaction test for attention-plus-recent retention on GPT-2-small
- Success threshold: Attention-plus-recent has at least 0.2 lower mean delta NLL than recency at two or more retention fractions between 20% and 50%, with lower paired delta on at least 60% of examples and no worse throughput/memory accounting than recency.
- Stop condition: Stop if attention-plus-recent fails to beat recency by 0.1 mean delta NLL at all tested retention fractions or if true cache compaction cannot preserve valid GPT-2 position semantics.

## Evidence references

- Artifact root: `<local-path>/projects/robustness-sweep-for-attention-quality-kv-retention-on-gpt-8388bce6ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
