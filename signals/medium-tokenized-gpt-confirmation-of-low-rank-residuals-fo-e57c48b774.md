# Medium tokenized GPT confirmation of low-rank residuals for ternary linear maps

Status: `useful_signal`
Project ID: `medium-tokenized-gpt-confirmation-of-low-rank-residuals-fo-e57c48b774`
Run ID: `medium-tokenized-gpt-confirmation-of-low-rank-residuals-fo-e57c48b774-20260519T145646495663+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Medium tokenized GPT confirmation of low-rank residuals for ternary linear maps: internal_generated:medium-tokenized-gpt-confirmation-of-low-rank-residuals-fo-e57c48b774

## What looked useful

True residual subspaces after ternary quantization carry useful GPT function: ternary-only mean validation loss was 2.5598 versus dense 1.9692, and rank-64 SVD residual correction improved to 2.0307. Randomized singular-vector residuals with the same singular values worsened to 2.7950, showing the effect depends on learned residual directions. The strict spectral low-rank claim is mixed because rank90/rank95 energy was close to matched Gaussian baselines.

## Boundaries and scale limits

This run used small character-token GPTs, 900 training steps, and post-hoc SVD corrections only. It did not test BPE-token GPT-2-small-class models, pretrained checkpoints, learned low-rank residual training, multiple corpora, downstream tasks, or deployment kernels. Residual spectra were not strongly more low-rank than matched Gaussian controls.

## Claim scope

On three fixed-seed 4-layer 128-wide character-token GPTs trained on Tiny Shakespeare, post-training ternary quantization of learned linear maps is substantially repaired by true SVD residual directions: rank-64 corrections recover about 89.6% of the ternary validation-loss gap, while randomized singular-vector controls degrade loss.

## Why it stopped

No-paper closure: this Tier 2 run provides a useful mechanism signal but not publication-grade or broad-scale confirmation, and the spectral low-rank evidence is mixed rather than strongly positive.

## Recommended next action

Run a bounded GPT-2-small-class BPE follow-up that compares dense, ternary-only, true SVD residual, learned low-rank residual, and randomized residual controls on at least two text corpora before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class BPE validation of functional ternary low-rank residual repair
- Success threshold: Rank no greater than 64 or no greater than 25% of each matrix minimum dimension recovers at least 80% of the ternary-only validation-loss gap on both corpora, with randomized residual controls recovering no more than 10% and residual spectra or learned-subspace diagnostics explaining why.
- Stop condition: Stop if true low-rank residuals recover less than 50% of the ternary gap on either corpus, if randomized controls match true residual recovery, or if residual spectra/subspace diagnostics remain indistinguishable from random after functional gains are accounted for.

## Evidence references

- Artifact root: `<local-path>/projects/medium-tokenized-gpt-confirmation-of-low-rank-residuals-fo-e57c48b774`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
