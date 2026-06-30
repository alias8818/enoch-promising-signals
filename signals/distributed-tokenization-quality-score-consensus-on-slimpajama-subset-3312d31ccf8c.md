# Distributed tokenization + quality-score consensus on SlimPajama subset

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distributed-tokenization-quality-score-consensus-on-slimpajama-subset-3312d31ccf8c`
Run ID: `distributed-tokenization-quality-score-consensus-on-slimpajama-subset-3312d31ccf8c-20260621T072332243974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

Distributed deterministic scoring worked exactly across tested worker counts, but uncalibrated multi-tokenizer median consensus did not outperform the best single tokenizer: consensus AUC was 0.9556 versus whitespace AUC 0.9725.

## Boundaries and scale limits

This was a bounded CPU-only subset experiment on a sampled public derivative, not the full SlimPajama-627B corpus, not human-labeled quality evaluation, and not a downstream language-model training ablation.

## Claim scope

On a 500-document public SlimPajama-6B subset with 150 controlled perturbation controls, deterministic distributed tokenization/scoring was shard-invariant across 1, 2, and 4 CPU workers, and median multi-tokenizer consensus separated original from perturbed documents with AUC 0.9556.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports distributed determinism and perturbation sensitivity, but the central consensus-improves-quality claim was not supported against the best single-tokenizer baseline.

## Recommended next action

Run a bounded deepen follow-up on a stratified 5k-row sample with natural or annotated quality labels, comparing uncalibrated consensus, best single-tokenizer scoring, and calibrated weighting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stratified SlimPajama quality-label calibration for tokenization consensus
- Success threshold: Calibrated consensus improves AUC by at least 0.02 over the best single-tokenizer baseline while preserving exact shard-invariant scores across worker counts.
- Stop condition: Stop if calibrated consensus fails to beat the best single-tokenizer baseline by 0.02 AUC or if label quality is insufficient to support a direct comparison.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-tokenization-quality-score-consensus-on-slimpajama-subset-3312d31ccf8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
