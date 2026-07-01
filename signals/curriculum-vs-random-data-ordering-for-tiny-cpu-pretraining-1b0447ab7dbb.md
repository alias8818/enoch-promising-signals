# Curriculum vs random data ordering for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-vs-random-data-ordering-for-tiny-cpu-pretraining-1b0447ab7dbb`
Run ID: `curriculum-vs-random-data-ordering-for-tiny-cpu-pretraining-1b0447ab7dbb-20260619T214842371383+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Curriculum ordering gave a reproducible early-training benefit in the controlled proxy: 16-epoch overall validation NLL was 3.7809 for curriculum versus 3.9746 for random, with curriculum winning 5/5 paired seeds. At 32 epochs the overall gap shrank to -0.0441 and difficulty effects were mixed, but curriculum remained better on hard examples by -0.3671 NLL.

## Boundaries and scale limits

Synthetic corpus, one tiny non-Transformer neural language model, 5 seeds, CPU-only short runs, no natural text, no tokenizer effects, no GPT-2-small-class baseline, and no large-corpus or long-horizon validation.

## Claim scope

In a bounded NumPy tiny next-token CPU proxy with synthetic easy/medium/hard examples and fixed train/validation examples per seed, curriculum ordering improved 16-epoch validation loss versus random ordering across 5/5 paired seeds and retained a hard-example advantage at 32 epochs.

## Why it stopped

The result is a controlled synthetic CPU proxy, not full validation of curriculum ordering for real tiny Transformer pretraining; 32-epoch behavior is mixed despite the reproducible early and hard-example advantage.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next concrete action is a bounded deepen run using a small Transformer on a real text subset with matched sequence-item budget, anti-curriculum control, and multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer real-text curriculum versus random ordering
- Success threshold: Curriculum beats random on mean validation loss/perplexity in at least 3/3 paired seeds at an early checkpoint and remains no worse than random at the final matched-compute checkpoint, with anti-curriculum not matching the curriculum advantage.
- Stop condition: Stop as unsupported if curriculum fails to beat random in at least 2/3 paired seeds at the early checkpoint or if the final checkpoint reverses the mean advantage by more than 0.5 percent perplexity.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-vs-random-data-ordering-for-tiny-cpu-pretraining-1b0447ab7dbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
