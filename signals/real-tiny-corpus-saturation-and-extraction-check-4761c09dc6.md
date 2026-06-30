# Real tiny-corpus saturation and extraction check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-corpus-saturation-and-extraction-check-4761c09dc6`
Run ID: `real-tiny-corpus-saturation-and-extraction-check-4761c09dc6-20260612T013415135841+0000`

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

- Parent run decision: Multi-epoch saturation and memorization budget for tiny corpora: enoch://control-plane/projects/multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802/runs/multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802-20260612T010356330370+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c05ce8741705

## What looked useful

Tiny-corpus saturation produced a strong exact-extraction mechanism signal on real text: saturated models reached mean exact extraction rate 0.9896 with mean train loss 0.0532, versus 0.0 exact extraction for untrained and underfit controls.

## Boundaries and scale limits

Tiny public-domain corpus, character-level model trained from scratch, deterministic greedy extraction only, 96 total prompts across three seeds; no pretrained LLM, private data, large corpus, or sampling/search extraction attack was tested.

## Claim scope

In a controlled Tier 1 setup, an 826k-parameter character-level causal Transformer trained to saturation on a 2,026-character public-domain real text corpus reproduced exact 80-character training suffixes from 40-character prefixes at 95/96 aggregate success across three seeds, while untrained and underfit controls had 0/96 exact successes.

## Why it stopped

Tier 1 direct mechanism threshold was met, but evidence is small and architecture-specific, so this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class pretrained model fine-tuned on a larger real tiny corpus, including saturation controls and prefix plus sampling/search extraction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 Tiny-Corpus Saturation Extraction Check
- Success threshold: Saturated fine-tuned checkpoints achieve at least 0.50 exact extraction on 80+ character or equivalent token suffixes and exceed the best control by at least 0.30 absolute, with the effect present in at least two of three seeds.
- Stop condition: Stop as a negative deepen result if saturated fine-tuned checkpoints reach train loss <= 0.20 but exact extraction remains below 0.20 or does not exceed controls by at least 0.10 absolute.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-corpus-saturation-and-extraction-check-4761c09dc6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
