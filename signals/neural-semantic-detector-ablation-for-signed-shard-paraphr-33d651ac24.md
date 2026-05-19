# Neural semantic detector ablation for signed-shard paraphrase poison scanning

Status: `useful_signal`
Project ID: `neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24`
Run ID: `neural-semantic-detector-ablation-for-signed-shard-paraphr-33d651ac24-20260519T064104947579+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

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
