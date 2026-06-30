# Cheating-Resistant Volunteer Training via Audit Replays on Tiny GPT-2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cheating-resistant-volunteer-training-via-audit-replays-on-tiny-gpt-2-2f1fce258aa3`
Run ID: `cheating-resistant-volunteer-training-via-audit-replays-on-tiny-gpt-2-2f1fce258aa3-20260621T210612480795+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14bbe7f1f354

## What looked useful

Seen replay accuracy alone is unsafe for cheating-resistant volunteer training. In the final run, honest replay training reached 100% seen-family accuracy but only 25% novel-family and 25% paraphrased-novel accuracy. A shortcut-trained control also reached 100% seen clean accuracy, while a badge-conflict probe exposed a 25 point robustness gap versus the honest model.

## Boundaries and scale limits

Not pretrained Tiny GPT-2 or GPT-2-small; synthetic corpus only; 36 training examples, 24 seen-family test examples, 8 novel-family examples, and 8 paraphrased novel examples; one explicit shortcut channel tested.

## Claim scope

Synthetic from-scratch tiny GPT-2-class proxy for volunteer audit replay training. The model memorized seen replay families but failed held-out action-family and paraphrased novel cases.

## Why it stopped

Proxy early falsification: the bounded from-scratch tiny GPT-2-class model did not support the strong cheating-resistant training claim beyond seen-case memorization.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should fine-tune pretrained Tiny GPT-2 or GPT-2-small on a larger synthetic-plus-realistic audit corpus with held-out action-family and shortcut-conflict gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Tiny GPT-2 audit replay shortcut-resistance gate
- Success threshold: At least 75% held-out action-family accuracy, at least 70% paraphrase/OOD accuracy, and less than 10 percentage-point shortcut-conflict degradation versus clean held-out accuracy.
- Stop condition: Stop if pretrained fine-tuning remains at or below 60% held-out action-family accuracy or shortcut-conflict degradation is 20 percentage points or worse after a calibrated medium run.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-volunteer-training-via-audit-replays-on-tiny-gpt-2-2f1fce258aa3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
