# Learned Exact-Anchor Memory on Realistic Exact-Recall Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-exact-anchor-memory-on-realistic-exact-recall-task-e16027ce01`
Run ID: `learned-exact-anchor-memory-on-realistic-exact-recall-task-e16027ce01-20260614T064022084326+0000`

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

- Parent run decision: Exact-Anchor Memory with Compressed Semantic State: enoch://control-plane/projects/exact-anchor-memory-with-compressed-semantic-state-ffa95df1448b/runs/exact-anchor-memory-with-compressed-semantic-state-ffa95df1448b-20260614T062232538353+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d7f0382a986

## What looked useful

Natural-query anchor memory reached 1.000 slot accuracy and exact-match on 16 records / 48 slots by step 100 and through step 800; seq2seq remained at 0.000 exact-match. However, an untrained shared encoder also solved exact-key lookup perfectly through 128 records / 384 slots, so exact-key success alone is not evidence of learned memory.

## Boundaries and scale limits

Only 16-record natural-query tests and exact-key ablations were run. Data were synthetic, memory slots were structured rather than learned from raw text, baselines were limited to a GRU seq2seq model, and robustness to aliases, near-duplicate anchors, real documents, transformer baselines, multiple seeds, and longer raw contexts remains untested.

## Claim scope

Tier 1 controlled small direct test on synthetic realistic contact/order exact-recall records. A learned anchor-key memory mapped natural exact-recall queries to one of 48 structured record slots and copied the exact email, phone, or order value with 1.000 exact-match, while a GRU seq2seq baseline reached 0.000 exact-match under the same short training budget.

## Why it stopped

Tier 1 direct evidence supports a bounded mechanism but is mixed and not publication-grade because exact-key lookup was solved by an untrained shared encoder and the stronger natural-query result still uses structured slots and limited baselines.

## Recommended next action

Stop this run as no-paper useful signal; next run should test raw-text anchor construction with non-identical aliases/paraphrases, a non-shared-encoder memory control, a small transformer/GPT-2-class baseline, and at least 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Raw-text and alias-robust learned anchor memory for exact recall
- Success threshold: Mean exact-match >= 0.90 for learned anchor memory and >= 0.20 absolute exact-match over every baseline/control on 16-64 record tasks across at least 3 seeds.
- Stop condition: Stop as negative if learned anchor memory fails to exceed 0.70 exact-match or fails to beat the best control by 0.10 absolute exact-match on the 16-record raw-text condition after calibrated training.

## Evidence references

- Artifact root: `<local-path>/projects/learned-exact-anchor-memory-on-realistic-exact-recall-task-e16027ce01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
