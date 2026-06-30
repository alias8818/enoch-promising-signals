# Natural Duplicate and Boilerplate-Hard Negative Threshold Check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-duplicate-and-boilerplate-hard-negative-threshold-04797f1e10`
Run ID: `natural-duplicate-and-boilerplate-hard-negative-threshold-04797f1e10-20260613T170100851435+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Small-Transformer Near-Duplicate Threshold Sweep on Real Tiny Corpus: enoch://control-plane/projects/small-transformer-near-duplicate-threshold-sweep-on-real-t-cf31ddbdf4/runs/small-transformer-near-duplicate-threshold-sweep-on-real-t-cf31ddbdf4-20260613T155700587420+0000
- Parent run decision: Near-Duplicate Threshold Sweep for Tiny Pretrain: enoch://control-plane/projects/near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467/runs/near-duplicate-threshold-sweep-for-tiny-pretrain-213e920a0467-20260613T151548827821+0000

## What looked useful

Across five fixed seeds, raw char-5 cosine calibrated on easy negatives had mean hard-negative FPR 0.9993. Stripping boilerplate reduced mean FPR by 0.368 absolute to 0.6313, supporting boilerplate dominance as a mechanism while showing the simple ablation is insufficient.

## Boundaries and scale limits

Synthetic prompt templates only; no private production traces, no human-labeled real duplicate corpus, no learned semantic duplicate model, and no cross-domain robustness claim.

## Claim scope

In a deterministic fixed-seed worker-style prompt benchmark, duplicate thresholds calibrated on natural duplicates plus easy negatives false-accept boilerplate-hard negatives at very high rates; deterministic boilerplate stripping materially reduces but does not solve the failure.

## Why it stopped

Tier 2 local evidence supports the failure mechanism but remains synthetic and the best ablation still has high hard-negative FPR, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful evidence; a next bounded deepen should test the same threshold-transfer protocol on a real or semi-real labeled agent transcript corpus with stronger semantic baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Boilerplate-Hard Duplicate Threshold Transfer
- Success threshold: A calibrated semantic or core-aware method reduces hard-negative FPR by at least 50% relative to raw lexical thresholds while preserving at least 0.90 duplicate recall on held-out real/semi-real data.
- Stop condition: Stop if real/semi-real data do not reproduce a raw-threshold hard-negative FPR of at least 0.20 or if no bounded non-private labeled corpus can be assembled.

## Evidence references

- Artifact root: `<local-path>/projects/natural-duplicate-and-boilerplate-hard-negative-threshold-04797f1e10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
