# Channel-Selective INT3 Training for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `channel-selective-int3-training-for-gpt-2-542506b494cb`
Run ID: `channel-selective-int3-training-for-gpt-2-542506b494cb-20260602T180144674654+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ffbf8f38a301

## What looked useful

Selected channel protection showed a small average validation-loss advantage over random protection (-0.00746) and a noisy average advantage over all-INT3 (-0.00529), but the effect was below cross-seed variability and not paper-ready.

## Boundaries and scale limits

Small char-level GPT-style model on Tiny Shakespeare; fake quantization only; no GPT-2 tokenizer, no GPT-2-small-scale corpus, no real INT3 kernel, no throughput or memory-bandwidth validation.

## Claim scope

In a three-seed compact GPT-style character-level continuation-training probe with fake INT3 row quantization, gradient-selected 25% dense row protection slightly outperformed random row protection and was mixed versus all-INT3, while dense continuation remained better on average.

## Why it stopped

No-paper useful signal: this was a direct small-model/fake-quant probe and not a full GPT-2 validation; the selected-channel margin was small and mixed across controls.

## Recommended next action

Run a bounded deepen follow-up on a tokenized GPT-2-small-class model with at least three seeds and require selected channel protection to beat both random protection and all-INT3 by a predeclared margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenized GPT-2-small-class channel-selective INT3 continuation test
- Success threshold: Selected protection beats both all-INT3 and random protection by at least 0.02 validation loss on average across seeds, with no more than a 0.03 validation-loss gap to dense continuation at the same checkpoint budget.
- Stop condition: Stop if selected protection fails to beat random protection in at least two of three seeds or if the dense gap exceeds 0.05 validation loss after matched continuation training.

## Evidence references

- Artifact root: `<local-path>/projects/channel-selective-int3-training-for-gpt-2-542506b494cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
