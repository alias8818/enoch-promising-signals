# No-Auxiliary Length Curriculum for Realistic Tiny GPT Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153`
Run ID: `no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153-20260604T155222513439+0000`

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
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0c356b85ef28

## What looked useful

The planned 240-step test improved mean final val_loss_128 by 0.02294 nats, and a 1000-step persistence check improved it by 0.04679 nats; all three seeds improved in both runs. Curriculum initially lagged at target length during short-context phases and recovered after switching to length 128.

## Boundaries and scale limits

This does not validate realistic pretraining broadly: it uses byte tokens, WikiText-2, 1.9M parameters, max context 128, and short local runs. BPE tokenization, larger corpora, GPT-2-small-class scale, longer contexts, downstream metrics, and longer training are untested.

## Claim scope

In a small direct CUDA test using a 1.9M-parameter byte-level causal GPT on WikiText-2 with max context 128 and matched sequence-item budgets, a no-auxiliary 32->64->128 length curriculum improved final held-out context-128 validation loss versus fixed length 128 across three seeds.

## Why it stopped

No-paper useful signal: bounded direct evidence supports the mechanism locally, but it is not publication-grade realistic tiny GPT pretraining evidence.

## Recommended next action

Run a bounded deepen follow-up with BPE tokenization and a GPT-2-small-class or parameter-matched tiny GPT on a larger realistic text corpus, preserving matched sequence-item budget and fixed-length control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Tiny-GPT Length Curriculum Confirmation on Realistic Text
- Success threshold: Curriculum mean final target-context validation loss is at least 0.02 nats better than fixed length, or not worse than 0.01 nats while materially reducing training wall-clock or memory at matched sequence-item budget, with no seed worse by more than 0.02 nats.
- Stop condition: Stop if curriculum is worse than fixed length by more than 0.02 nats mean target-context validation loss after the target-length phase, or if schedule-boundary recovery fails in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
