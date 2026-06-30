# BPE Tiny-GPT Length Curriculum Confirmation on Realistic Text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bpe-tiny-gpt-length-curriculum-confirmation-on-realistic-t-a19c9536f0`
Run ID: `bpe-tiny-gpt-length-curriculum-confirmation-on-realistic-t-a19c9536f0-20260604T202317278763+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Length Curriculum Data Scheduling for Tiny Pretraining: enoch://control-plane/projects/length-curriculum-data-scheduling-for-tiny-pretraining-f35fbc6410a0/runs/length-curriculum-data-scheduling-for-tiny-pretraining-f35fbc6410a0-20260604T110615314101+0000
- Parent run decision: No-Auxiliary Length Curriculum for Realistic Tiny GPT Pretraining: enoch://control-plane/projects/no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153/runs/no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153-20260604T155222513439+0000

## What looked useful

Forward length curriculum improved mean length-128 validation loss from 5.881676 to 5.860949, a -0.020727 paired mean delta versus the full-length baseline, and reduced mean length-128 perplexity from 358.41 to 351.06. Reverse curriculum worsened mean length-128 loss to 5.909430, supporting the target-length curriculum mechanism rather than arbitrary length mixing.

## Boundaries and scale limits

TinyGPT scale only: 3.34M parameters, WikiText-2, target context length 128, 600 optimizer steps, three seeds, no GPT-2-small-class run, no larger corpus, no context length above 128, and no long-horizon persistence test.

## Claim scope

On WikiText-2 raw text tokenized with train-only ByteLevel BPE, a 3.34M parameter decoder-only TinyGPT trained for 600 steps with an equal estimated token budget showed a consistent full-context validation-loss improvement from a 32 -> 64 -> 128 length curriculum over a full-length-only baseline across seeds 11, 22, and 33.

## Why it stopped

Tier 2 local evidence supports the mechanism at TinyGPT/WikiText-2 scale, but the claim is not paper-ready without larger model/data/context validation and persistence checks.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with a larger realistic-corpus and longer-context confirmation, adding a random-length control and a late-token-budget persistence check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length Curriculum Persistence at Larger Context on Realistic BPE Text
- Success threshold: Forward curriculum must beat full-length baseline and random-length control on target-context validation loss by at least 0.01 nats mean paired delta across at least three seeds, while reverse curriculum must not match the forward curriculum; the advantage must persist after the matched full-length continuation phase.
- Stop condition: Stop as unsupported if the forward curriculum fails to beat the full-length baseline by 0.01 nats mean paired target-context validation loss, if the random-length control matches or beats it, or if the advantage disappears during the full-length persistence phase.

## Evidence references

- Artifact root: `<local-path>/projects/bpe-tiny-gpt-length-curriculum-confirmation-on-realistic-t-a19c9536f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
