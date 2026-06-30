# Logit-cache projection drafting from recent decoding steps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `logit-cache-projection-drafting-from-recent-decoding-steps-9eb07091775f`
Run ID: `logit-cache-projection-drafting-from-recent-decoding-steps-9eb07091775f-20260620T053554497122+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff5a6bb3738

## What looked useful

Window 1/2 logit projections roughly doubled target-model top-1 agreement versus previous-logit reuse (about 10.3-11.0% vs about 4.7%) and improved top-5 inclusion (about 28.8-29.9% vs about 10.8-11.0%) across two random projection seeds.

## Boundaries and scale limits

Single GPT-2-small-class model, one public text split, teacher-forced packed-token evaluation, no integrated speculative decoder, no end-to-end latency or acceptance measurement, no 7B+ or production-serving validation.

## Claim scope

On GPT-2 with 96 packed WikiText-2 test chunks, a small ridge projection from recent random-projected logits predicts the next target-model logit distribution better than reusing previous logits.

## Why it stopped

Bounded mechanism signal is positive, but the serving-speed drafting claim is unvalidated; this is not publication-grade evidence.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should implement an integrated speculative verifier and require a measured acceptance-rate and tokens/sec gain after projection overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated speculative verification for logit-projection drafts
- Success threshold: At least 1.10x end-to-end tokens/sec over ordinary GPT-2 decoding with acceptance rate at least 20% on held-out prompts after including all projection overhead.
- Stop condition: Stop if net throughput is below 1.02x or acceptance is below 10% in two seeds, because the projection signal is then insufficient for practical drafting at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/logit-cache-projection-drafting-from-recent-decoding-steps-9eb07091775f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
