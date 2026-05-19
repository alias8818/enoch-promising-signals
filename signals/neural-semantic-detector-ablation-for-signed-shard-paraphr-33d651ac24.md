# Neural semantic detector ablation for signed-shard paraphrase poison scanning

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `43`
Project ID: `neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24`
Run ID: `neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24-20260519T064104947579+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `43`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Neural semantic detector ablation for signed-shard paraphrase poison scanning: internal_generated:neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24

## What looked useful

The direct shard target is solved by neural semantic detectors, but equally solved by realistic lexical TF-IDF baselines. Semantic models beat weak keyword, random, centroid-only, and label-shuffle controls, so the mechanism is learnable, but the neural-specific novelty claim is unsupported.

## Boundaries and scale limits

Synthetic corpus only; no production shard traffic, live LLM adversarial paraphrases, multilingual/code-mixed attacks, very long context documents, or real provenance infrastructure were tested.

## Claim scope

In a controlled synthetic signed-shard paraphrase poison scanning benchmark with held-out paraphrases, eight fixed seeds, 1200 train shards and 2400 test shards per seed, MiniLM semantic LR/MLP detectors do not outperform supervised word or character TF-IDF logistic baselines on shard-level AUROC, AUPRC, best F1, or recall at 1% FPR.

## Why it stopped

Bounded full validation directly falsified the neural-specific advantage threshold: semantic_embedding_mlp matched but did not exceed word/char TF-IDF baselines, with paired recall-at-1%-FPR delta 0.0 over both lexical baselines.

## Recommended next action

Stop this follow-up as no-paper evidence; only reopen with a real or adversarially generated corpus where supervised TF-IDF is expected to fail and a neural detector has a predeclared advantage threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
