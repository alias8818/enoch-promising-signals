# Real-text tiny transformer test of middle-surprise filtering

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-tiny-transformer-test-of-middle-surprise-filteri-42a4a54316`
Run ID: `real-text-tiny-transformer-test-of-middle-surprise-filteri-42a4a54316-20260520T035456616350+0000`

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

- Parent run decision: Middle-surprise filtering for tiny neural LM pretraining: enoch://control-plane/projects/middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86/runs/middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86-20260520T034927445434+0000
- Parent run decision: Surprise-Scored Data Pruning for Tiny Pretraining: enoch://control-plane/projects/surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145/runs/surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145-20260519T224323422391+0000

## What looked useful

Middle-surprise filtering failed the broad data-efficiency threshold at 800 steps and at best-checkpoint comparison, but showed a consistent late-training robustness signal: at 2400 fixed steps it beat random by 0.1315 nats mean validation loss and won 3/3 paired seeds, while full-data training remained much better.

## Boundaries and scale limits

Single real-text corpus, character-level tokenization, bigram surprise scorer, under-1M-parameter transformer, three seeds for filtered conditions, one seed for full-data baseline; not evidence for GPT-2-small-class or larger pretraining.

## Claim scope

On Tiny Shakespeare character-level language modeling with an 824897-parameter decoder-only transformer and 20% bigram-surprise-selected chunks, middle-surprise filtering did not improve best validation loss versus random equal-token filtering, but it did reduce final fixed-budget overfitting at 2400 steps versus random, low-surprise, and high-surprise filters.

## Why it stopped

Mixed Tier 2 evidence: middle filtering supports only an overtraining-robustness mechanism, not a general validation-loss or data-efficiency improvement, and the full-data baseline is substantially stronger.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test whether the fixed-budget robustness effect persists with token-level modeling on a broader real-text corpus and an early-stopping/best-checkpoint control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level real-text test of middle-surprise overtraining robustness
- Success threshold: Middle beats random by at least 0.03 nats mean validation loss at fixed final budget and is no worse than random by more than 0.005 nats at best checkpoint, with wins in at least 3/5 paired seeds and better mean validation loss than low and high filters.
- Stop condition: Stop as negative if middle does not beat random at fixed final budget or remains worse than random at best checkpoint by more than 0.02 nats on the broader token-level corpus.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-tiny-transformer-test-of-middle-surprise-filteri-42a4a54316`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
