# Tiny Draft Model for Tool-Call Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-draft-model-for-tool-call-speculative-decoding-ac4373435a92`
Run ID: `tiny-draft-model-for-tool-call-speculative-decoding-ac4373435a92-20260526T042101316820+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/32cdf8380d92

## What looked useful

Tool-trained byte n-gram draft achieved 92.7% target-call reduction and 10.39x idealized speedup at 1% draft byte cost on seen-schema tool calls, versus 17.4% reduction for unigram and 11.1% for a natural-text n-gram control. Benefits persisted but weakened under shifted values and held-out schemas.

## Boundaries and scale limits

No live LLM target, no neural draft model, no production tokenizer, no KV-cache or batching effects, and no measured end-to-end serving latency; results cover 600 synthetic test samples per condition.

## Claim scope

Synthetic oracle-verifier byte-level tool-call traces show that a tiny tool-trained n-gram draft can reduce expensive verifier calls for repeated tool-call JSON schemas.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only despite supporting the mechanism.

## Recommended next action

Run a bounded real-model trace replay with actual assistant tool-call outputs, production tokenization, and a separately trained tiny neural draft before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace replay for tiny neural tool-call draft decoding
- Success threshold: At least 2x modeled verifier-call speedup at an empirically justified draft/target cost ratio on held-out same-schema traces, with less than 25% degradation on shifted-value traces and better performance than all controls.
- Stop condition: Stop if real-token acceptance yields less than 1.3x modeled speedup or does not beat unigram/generic draft controls on same-schema held-out traces.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-model-for-tool-call-speculative-decoding-ac4373435a92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
