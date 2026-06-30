# Self-Speculative Decoding via Early-Exit Draft from Intermediate Layers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-draft-from-intermediate-layers-7cfc0c789512`
Run ID: `self-speculative-decoding-via-early-exit-draft-from-intermediate-layers-7cfc0c789512-20260529T103913213295+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5213de7fb002

## What looked useful

Intermediate exits become more aligned near the final layer, but acceptance and cost are insufficient: exit 11 averaged 63.1% agreement with full greedy continuations, 38.2% draft acceptance, 0.42x measured wall-clock speedup, and 0.52x idealized layer-work speedup versus full greedy decoding.

## Boundaries and scale limits

Single small pretrained model, greedy decoding only, 16 fallback prompts, one gamma value, no trained exit heads, no confidence gating, and a conservative Python implementation. This is an early falsification of the untrained mechanism, not a full-scale validation of all self-speculative methods.

## Claim scope

On GPT-2 small with zero-training early exits using the shared LM head, intermediate-layer greedy drafts do not reach break-even for self-speculative decoding on 16 short prompts with 32 generated tokens and gamma=4.

## Why it stopped

Proxy-scale early falsification: untrained intermediate-layer drafts were directly tested on GPT-2 small and did not approach speedup break-even; larger or trained-exit evidence would be required to overturn this result.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test whether trained or calibrated early-exit heads plus confidence gating can raise acceptance enough to exceed 1.0x idealized layer-work speedup on GPT-2 small.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained and Gated Early-Exit Drafts for GPT-2 Small Self-Speculation
- Success threshold: At least one exit/gate setting achieves mean idealized layer-work speedup greater than 1.10x and measured wall-clock speedup greater than 0.90x on GPT-2 small while exactly matching full greedy decoding.
- Stop condition: Stop if no trained or gated condition exceeds 0.85x idealized layer-work speedup after 128 prompts, because it remains below break-even even before implementation overhead.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-from-intermediate-layers-7cfc0c789512`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
