# Medium BPE/tokenizer confirmation of equal-token length-stratified real-text pretraining advantage

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `medium-bpe-tokenizer-confirmation-of-equal-token-length-st-c149c2551e`
Run ID: `medium-bpe-tokenizer-confirmation-of-equal-token-length-st-c149c2551e-20260527T005343272395+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Length-Stratified Long Context Pretraining: enoch://control-plane/projects/length-stratified-long-context-pretraining-7d650e3873b3/runs/length-stratified-long-context-pretraining-7d650e3873b3-20260525T174111937355+0000
- Parent run decision: Real-text equal-token length-stratified pretraining probe: enoch://control-plane/projects/real-text-equal-token-length-stratified-pretraining-probe-e5ebb99df6/runs/real-text-equal-token-length-stratified-pretraining-probe-e5ebb99df6-20260526T182401285178+0000

## What looked useful

Token-length stratification was nearly tied with random overall (mean paired delta -0.00055 NLL, wins 2/3 seeds) and on long examples (delta -0.00091), while character-length stratification was stronger overall (delta -0.00602 NLL, wins 3/3 seeds). This argues against a BPE-token-specific mechanism and suggests any small gain may come from generic length-aware sampling.

## Boundaries and scale limits

The controller repeatedly SIGTERM-killed longer monolithic 300-700 step runs, so the completed evidence uses condition-level jobs of 100 training steps each. This is direct fixed-seed evidence with a real baseline and ablation, but not long-horizon or full-scale pretraining evidence.

## Claim scope

On WikiText-2 real-text causal LM training with a trained byte-level BPE tokenizer, a small Transformer, fixed seeds 11/23/37, 100 steps per seed-condition, and validation by BPE-token length stratum, BPE-token length-stratified batching does not show a robust advantage over random batching and is weaker than a character-length stratification control.

## Why it stopped

Bounded direct fixed-seed evidence failed the success threshold because BPE-token stratification did not robustly outperform random and did not beat the character-length control.

## Recommended next action

Stop the BPE-token-specific claim; branch only if testing the distinct generic length-aware sampling hypothesis with a resumable longer-horizon harness.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Generic length-aware sampling versus BPE-token-specific stratification
- Success threshold: Character or generic length-aware sampling beats random by at least 0.01 validation NLL overall and on the long stratum in at least 4/5 seeds, while BPE-token-specific stratification is not required to obtain the gain.
- Stop condition: Stop if the longer-horizon run shows deltas below 0.005 NLL, inconsistent seed wins, or no separation from random on the long BPE-token stratum.

## Evidence references

- Artifact root: `<local-path>/projects/medium-bpe-tokenizer-confirmation-of-equal-token-length-st-c149c2551e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
