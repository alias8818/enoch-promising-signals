# Downstream validation of GPT-2 perplexity percentile filtering on public noisy text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `downstream-validation-of-gpt-2-perplexity-percentile-filte-54f5a59fab`
Run ID: `downstream-validation-of-gpt-2-perplexity-percentile-filte-54f5a59fab-20260630T074712104932+0000`

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

- Parent run decision: Perplexity-bucket quality filtering for GPT-2-tiny pretraining: enoch://control-plane/projects/perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae/runs/perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae-20260630T071642025813+0000
- Parent run decision: GPT-2-tokenized perplexity bucket filtering on naturally noisy public text: enoch://control-plane/projects/gpt-2-tokenized-perplexity-bucket-filtering-on-naturally-n-28a17fd44f/runs/gpt-2-tokenized-perplexity-bucket-filtering-on-naturally-n-28a17fd44f-20260630T072934583615+0000

## What looked useful

High-perplexity tail removal had a small repeatable in-domain benefit and small average WikiText-2 benefit, but one clean-eval seed tied/slightly regressed. Middle-percentile filtering was consistently harmful on WikiText-2. Treat GPT-2 PPL filtering as cutoff-sensitive rather than generally beneficial.

## Boundaries and scale limits

Only 150k training tokens per variant before block truncation, 300 update steps, 4-layer 128-wide scratch models, 3 seeds, one public web corpus sample, GPT-2 scoring over first 256 tokens per document, LM-loss evaluation only. Not evidence for full-corpus filtering, larger model pretraining, long training, or broad downstream tasks.

## Claim scope

Bounded local validation on 800 public FineWeb sample-10BT documents: dropping the highest 20% of documents by GPT-2 perplexity produced small average downstream LM-loss improvements over an unfiltered equal-token control for tiny GPT-2-style models trained from scratch across three seeds; middle-80% percentile filtering worsened clean WikiText-2 transfer.

## Why it stopped

No-paper useful signal: bounded direct evidence is mixed and too small for publication-grade downstream validation.

## Recommended next action

Stop paper path for this run; if continuing, run a bounded cutoff sweep over top-tail thresholds on a larger token budget before considering scale-out.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cutoff sweep for GPT-2 perplexity top-tail filtering on public web text
- Success threshold: A top-tail cutoff improves both same-corpus and WikiText-2 mean validation loss over unfiltered and matched random-drop controls by at least 0.03 loss with no seed worse than 0.01 loss.
- Stop condition: Stop if no cutoff beats both controls on both evaluations, or if gains remain below 0.01 mean loss after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/downstream-validation-of-gpt-2-perplexity-percentile-filte-54f5a59fab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
