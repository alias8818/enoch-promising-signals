# Self-Speculative Early-Exit Decoding Without Draft Model VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-early-exit-decoding-without-draft-model-vram-3b972423ed2e`
Run ID: `self-speculative-early-exit-decoding-without-draft-model-vram-3b972423ed2e-20260528T155634811752+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/233ff68cbe05

## What looked useful

Intermediate exits had only 18.75% to 31.25% top-1 agreement with the final layer. The best tested speculative configuration was layer 2 with draft length 1, accept rate 23.08%, emitted/iteration 1.2308 versus 1.3333 break-even, and idealized speedup 0.923x. Longer drafts were worse.

## Boundaries and scale limits

One small GPT-2-class model, fixed small prompt set, no trained early-exit heads, no long-context benchmark, no production KV-cache implementation, and speed estimated by idealized transformer-block steps rather than wall-clock serving throughput.

## Claim scope

On distilgpt2 with untrained logit-lens/tied-head intermediate exits, self-speculative greedy decoding without a separate draft model did not achieve idealized break-even speed on 32 fixed prompts and an 8-prompt speculative simulation sweep.

## Why it stopped

Proxy/early falsification: the directly tested untrained early-exit draft path failed to reach idealized break-even, so the result is no-paper useful signal rather than a publication-grade positive or universal negative.

## Recommended next action

Stop this no-training tied-head variant; the bounded result is a proxy/early falsification, not full validation. If continuing, train lightweight auxiliary early-exit heads and require held-out exact acceptance plus measured wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for self-speculative decoding
- Success threshold: At least 1.15x measured tokens/sec over baseline greedy decoding on held-out prompts with exact greedy output equivalence and no separate draft model weights resident in memory.
- Stop condition: Stop if trained exits cannot exceed 70% held-out top-1 agreement at an exit shallow enough to give an idealized speedup above 1.0x, or if measured wall-clock throughput remains <= baseline.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-decoding-without-draft-model-vram-3b972423ed2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
