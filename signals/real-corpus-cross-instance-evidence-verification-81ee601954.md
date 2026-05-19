# Real-Corpus Cross-Instance Evidence Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-cross-instance-evidence-verification-81ee601954`
Run ID: `real-corpus-cross-instance-evidence-verification-81ee601954-20260517T195724404558+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2e8dc4035b73

## What looked useful

At the primary 10% corruption setting, five seeds achieved AUROC 0.965-0.978 and precision-at-budget 0.70-0.78 versus a 0.10 random base rate, supporting the cross-instance evidence mechanism under controlled real-corpus conditions.

## Boundaries and scale limits

Single corpus family, four classes, 1000 sampled documents per run, injected label corruption only, simple TF-IDF representation, no natural annotation-error labels, no open-world factual verification, and no stronger baseline comparison beyond random base rate.

## Claim scope

In a controlled 20 Newsgroups real-corpus label-corruption task with 1000 documents across four categories, a simple TF-IDF cross-instance neighbor evidence score reliably identifies deliberately mislabeled instances.

## Why it stopped

No-paper useful signal: the Tier 1 direct controlled test supports the mechanism, but this is not paper-positive because it uses injected corruption on one corpus family and lacks natural-error labels and strong baselines.

## Recommended next action

Run a medium confirmation on two additional real corpora with stronger baselines, including classifier confidence and sentence-embedding kNN evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Multi-Corpus Cross-Instance Evidence Verification
- Success threshold: Across at least three total corpora, mean AUROC >= 0.80 and precision-at-budget >= 2x the random base rate at 10% corruption, while beating the strongest non-cross-instance baseline on at least two corpora.
- Stop condition: Stop if cross-instance evidence fails to reach AUROC 0.70 or precision-at-budget 1.5x random on two corpora, or if performance is not competitive with classifier-confidence baselines.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-cross-instance-evidence-verification-81ee601954`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
