# Medium Multi-Corpus Cross-Instance Evidence Verification

Status: `useful_signal`
Project ID: `medium-multi-corpus-cross-instance-evidence-verification-9ea0827de6`
Run ID: `medium-multi-corpus-cross-instance-evidence-verification-9ea0827de6-20260517T200201207923+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium Multi-Corpus Cross-Instance Evidence Verification: internal_generated:medium-multi-corpus-cross-instance-evidence-verification-9ea0827de6

## What looked useful

Multi-corpus retrieval was strongly beneficial versus single-corpus BM25 (+0.2021 macro-F1), but requiring two independent corpora to agree caused many true SUPPORTS/REFUTES claims to become NEI and reduced macro-F1 by 0.1585 versus pooled BM25.

## Boundaries and scale limits

Synthetic corpus with deterministic fact extraction; no learned NLI verifier, no real FEVER/SciFact/open-domain corpus, and no large-scale naturally occurring evidence distribution.

## Claim scope

On a deterministic medium synthetic multi-corpus claim-verification benchmark with 12,000 claims over five fixed seeds, simple multi-corpus retrieval improves over a single-corpus baseline, but the tested hard source-diverse cross-instance verifier underperforms pooled BM25 and an entity-linked no-diversity ablation.

## Why it stopped

Medium fixed-seed direct metrics falsified the tested hard source-diverse cross-instance mechanism against a real pooled BM25 baseline and entity-linked no-diversity ablation; this is a no-paper useful signal rather than full external validation.

## Recommended next action

Run one bounded deepen test of calibrated soft source-diversity voting that can abstain less aggressively, then stop unless it beats pooled BM25 and the no-diversity ablation by at least 0.03 macro-F1 on held-out synthetic stress settings and one real claim-verification dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Soft Source Diversity for Cross-Corpus Claim Verification
- Success threshold: Mean macro-F1 at least 0.03 above pooled BM25 and entity-linked no-diversity with non-overlapping or clearly separated seed bootstrap intervals, while not reducing SUPPORTS/REFUTES recall by more than 0.02.
- Stop condition: Stop if calibrated soft diversity fails to beat pooled BM25 and the no-diversity ablation on either the synthetic stress suite or the real benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/medium-multi-corpus-cross-instance-evidence-verification-9ea0827de6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
