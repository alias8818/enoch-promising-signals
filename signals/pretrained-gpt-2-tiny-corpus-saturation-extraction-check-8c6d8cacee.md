# Pretrained GPT-2 Tiny-Corpus Saturation Extraction Check

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-gpt-2-tiny-corpus-saturation-extraction-check-8c6d8cacee`
Run ID: `pretrained-gpt-2-tiny-corpus-saturation-extraction-check-8c6d8cacee-20260612T072740067741+0000`

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

- Parent run decision: Multi-epoch saturation and memorization budget for tiny corpora: enoch://control-plane/projects/multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802/runs/multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802-20260612T010356330370+0000
- Parent run decision: Real tiny-corpus saturation and extraction check: enoch://control-plane/projects/real-tiny-corpus-saturation-and-extraction-check-4761c09dc6/runs/real-tiny-corpus-saturation-and-extraction-check-4761c09dc6-20260612T013415135841+0000

## What looked useful

Saturation produced near-ceiling exact extraction of training secrets for pretrained GPT-2 (mean 0.979) with zero holdout extraction, but a matched random-initialized GPT-2 control also reached near-ceiling extraction (mean 0.951), so the pretrained-specific claim is not supported.

## Boundaries and scale limits

Synthetic tiny corpus only; exact prompts only; gpt2 checkpoint only; no natural private text, paraphrases, black-box extraction, larger GPT-2 variants, or long-training robustness.

## Claim scope

GPT-2-small-class causal language models fine-tuned on 48 synthetic prompt-keyed secret records with 24 holdout records, fixed seeds 11/23/37, repeats=1 versus repeats=16, exact greedy extraction from exact prompts.

## Why it stopped

Tier-2 direct metrics, fixed seeds, ablation, and real baseline show saturation-driven memorization, but the random-initialized baseline nearly matches pretrained GPT-2, so the pretrained-specific extraction hypothesis is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen test should use harder non-exact prompts and multiple corpus sizes to determine whether pretraining ever adds extraction advantage over a same-architecture random baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-Prompt GPT-2 Saturation Extraction Baseline Separation
- Success threshold: Pretrained GPT-2 must exceed random-initialized GPT-2 by at least 20 percentage points in train secret extraction on harder prompts while holdout and decoy extraction remain near zero across at least two corpus sizes.
- Stop condition: Stop if pretrained and random controls remain within 10 percentage points on harder prompt extraction or if holdout/decoy extraction indicates metric contamination.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-tiny-corpus-saturation-extraction-check-8c6d8cacee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
