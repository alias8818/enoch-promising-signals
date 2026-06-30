# Length Curriculum Persistence at Larger Context on Realistic BPE Text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `length-curriculum-persistence-at-larger-context-on-realist-4fff3fc6fb`
Run ID: `length-curriculum-persistence-at-larger-context-on-realist-4fff3fc6fb-20260605T005618446453+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: BPE Tiny-GPT Length Curriculum Confirmation on Realistic Text: enoch://control-plane/projects/bpe-tiny-gpt-length-curriculum-confirmation-on-realistic-t-a19c9536f0/runs/bpe-tiny-gpt-length-curriculum-confirmation-on-realistic-t-a19c9536f0-20260604T202317278763+0000
- Parent run decision: No-Auxiliary Length Curriculum for Realistic Tiny GPT Pretraining: enoch://control-plane/projects/no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153/runs/no-auxiliary-length-curriculum-for-realistic-tiny-gpt-pret-e7f1a82153-20260604T155222513439+0000

## What looked useful

The apparent curriculum persistence effect is not specific to the short-to-long schedule: short-only training achieved the best 512-token and late-position validation losses on all three seeds. This suggests the observed advantage over the long-only baseline is likely dominated by optimization/update-count effects from shorter sequences rather than a distinct larger-context curriculum mechanism.

## Boundaries and scale limits

This is a bounded small-model validation, not publication-grade full-scale evidence. It does not test larger models, longer contexts beyond 512, larger token budgets, update-matched/FLOP-matched schedules, or corpora designed to require long-range dependencies.

## Claim scope

At 6.9M parameters, 512-token target context, WikiText-103 raw text with GPT-2 BPE, 3 fixed seeds, and 1,572,864 training tokens per run, a short-to-long length curriculum improves 512-token validation loss versus an all-512 baseline, but a 128-token short-only control improves more.

## Why it stopped

No-paper closure: the direct 512-token target metric showed curriculum beating the long baseline, but the short-only control beat curriculum on every seed, so the proposed persistence mechanism is not isolated.

## Recommended next action

Run one bounded update-matched or FLOP-matched ablation that equalizes optimizer steps across baseline_long, curriculum, and short_only before considering any larger-context escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Update-Matched Length Curriculum Control on BPE Text
- Success threshold: Curriculum must beat both baseline_long and short_only on mean 512-token validation loss and pos_384_511 loss across seeds by at least 0.05 nats without relying on unequal optimizer-step count.
- Stop condition: Stop if short_only remains best or curriculum fails to beat both controls on either overall 512-token loss or late-position loss.

## Evidence references

- Artifact root: `<local-path>/projects/length-curriculum-persistence-at-larger-context-on-realist-4fff3fc6fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
