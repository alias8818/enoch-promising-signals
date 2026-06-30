# Commit-Reveal Anti-Plagiarism for Gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-anti-plagiarism-for-gradients-51a68eb89b81`
Run ID: `commit-reveal-anti-plagiarism-for-gradients-51a68eb89b81-20260528T093911155692+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4bc252eb86c7

## What looked useful

Commit-reveal rejected 2880/2880 reactive exact-copy attempts across six seeds while naive reveal accepted 2880/2880 exact-copy submissions. However, 2880/2880 precommitted 2% relative-L2 near-copies passed commitment checks with mean cosine about 0.999803, showing the mechanism is a consistency check, not a standalone anti-plagiarism proof.

## Boundaries and scale limits

Tested only synthetic CPU-local FedSGD with 24 clients, 6 adversaries, 64-dimensional gradients, 80 rounds, and six random seeds. Did not test real distributed timing, production FL frameworks, large model gradients, secure transport, incentive systems, or adaptive adversaries beyond exact reactive copy and precommitted near-copy.

## Claim scope

Synthetic federated logistic-regression rounds show that commit-reveal prevents same-round after-the-fact exact byte-for-byte gradient copying, but does not prove gradient originality or prevent precommitted near-copy submissions.

## Why it stopped

Bounded synthetic evidence supports the narrow reactive-copy prevention mechanism but early-falsifies the broader standalone anti-plagiarism claim; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test commit-reveal plus an explicit near-copy/originality detector on a real FL benchmark with false-positive, dropout-abuse, and utility metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Plus Similarity Detection on a Real FL Benchmark
- Success threshold: Reject at least 95% of reactive exact-copy attempts, detect at least 80% of 1-5% relative-L2 near-copies, keep honest false-positive rate below 1%, and keep final task accuracy within 1 percentage point of the honest baseline.
- Stop condition: Stop as negative if near-copy detection below 50% at false-positive rate below 1%, or if dropout/commit-abort abuse makes attribution unavailable in more than 10% of adversarial rounds.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-anti-plagiarism-for-gradients-51a68eb89b81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
