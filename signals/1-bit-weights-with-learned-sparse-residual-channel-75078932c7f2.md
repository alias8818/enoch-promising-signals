# 1-bit weights with learned sparse residual channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-weights-with-learned-sparse-residual-channel-75078932c7f2`
Run ID: `1-bit-weights-with-learned-sparse-residual-channel-75078932c7f2-20260524T211350949799+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3865595438b

## What looked useful

The learned sparse residual mechanism is sensitive to the mask estimator. A hard top-k estimator with poor surrogate gradients can freeze near random masks; a patched estimator produced a small +0.31 percentage point mean accuracy gain over random sparse at 0.5% density, but the effect was within seed variance and disappeared or reversed at higher densities.

## Boundaries and scale limits

The run used synthetic 128-dimensional inputs, same-shape MLP students, 3 seeds, 10 epochs, and residual densities up to 2%. It did not test language modeling, GPT-2-small-class baselines, real datasets, long training, kernel efficiency, storage/serving implementation, or large models.

## Claim scope

On a bounded synthetic dense-teacher MLP classification proxy, a 1-bit student with a learned sparse residual channel showed only a small, non-robust gain at 0.5% residual density and no consistent advantage at 1-2% density versus binary-only and random-sparse controls.

## Why it stopped

Proxy evidence is mixed rather than publication-grade: the learned residual channel produced only a small, non-monotonic gain on synthetic MLP distillation and did not robustly beat random sparse controls.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded small language-model follow-up comparing binary, random-sparse residual, and learned-sparse residual controls on a real next-token dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small language-model validation for learned sparse residual 1-bit weights
- Success threshold: Learned sparse residual beats both binary-only and random-sparse residual controls by at least 1% relative validation loss at the same residual density in at least two densities, with consistent paired-seed signs.
- Stop condition: Stop if learned sparse residual fails to beat random-sparse residual by 0.5% relative validation loss after a calibrated small-LM run, or if mask diagnostics show the learned mask remains effectively random.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-learned-sparse-residual-channel-75078932c7f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
