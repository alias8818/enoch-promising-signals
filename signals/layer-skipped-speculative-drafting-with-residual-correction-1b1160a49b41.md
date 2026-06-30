# Layer-Skipped Speculative Drafting with Residual Correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layer-skipped-speculative-drafting-with-residual-correction-1b1160a49b41`
Run ID: `layer-skipped-speculative-drafting-with-residual-correction-1b1160a49b41-20260527T133743337710+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

KL-trained residual correction reduced KL(full||draft) by 44.87% mean across three seeds, improved expected acceptance mass by 27.75% relative, improved top-1 agreement by 10.29 percentage points, and retained a 1.68x mean corrected-draft latency speedup versus the full path. Hidden-MSE correction was weaker and hurt top-1 agreement, indicating the objective matters.

## Boundaries and scale limits

Tested only GPT-2-small, WikiText-2, sequence length 128, alternate-layer skipping, final-hidden residual correction, three seeds, and distributional proxy metrics. No full multi-token speculative decoder, KV-cache serving benchmark, larger model, longer context, or cross-domain validation was run.

## Claim scope

On a bounded GPT-2-small WikiText-2 mechanism probe, a 395,776-parameter residual corrector trained with next-token KL makes a six-layer alternate-skipped draft path substantially closer to the frozen full model than plain layer skipping, improving expected speculative acceptance mass while preserving a measured draft-path latency advantage.

## Why it stopped

The run produced reproducible local proxy evidence but not direct end-to-end speculative decoding throughput, so it is not publication-grade validation.

## Recommended next action

Stop this run as a useful no-paper mechanism signal; next bounded action is to implement a complete speculative decoder and measure accepted tokens per second against plain layer skipping and a conventional small draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end speculative decoding benchmark for KL-corrected layer-skipped drafts
- Success threshold: At least 10% accepted-tokens-per-second improvement over plain layer skipping and no loss of exact speculative decoding correctness on the tested prompt set.
- Stop condition: Stop if corrected drafting fails to improve accepted tokens per second by 5% over plain layer skipping or if exactness/correctness checks fail.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skipped-speculative-drafting-with-residual-correction-1b1160a49b41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
