# Edit-tolerant prompt-lookup speculative decoding on 10GB

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `edit-tolerant-prompt-lookup-speculative-decoding-on-10gb-b85b447f23f5`
Run ID: `edit-tolerant-prompt-lookup-speculative-decoding-on-10gb-b85b447f23f5-20260601T050638566302+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Corrected sequential decoding simulation over 20 edited-repeat documents found median tolerant-over-exact gains of +0.116930 accepted tokens per baseline step and +0.389972 target-call speedup proxy, with 0/48 configurations harmful on the proxy. Median tolerant search overhead was 564.862 us/decode iteration, implying break-even only when target verifier calls cost hundreds of microseconds or more.

## Boundaries and scale limits

Evidence is synthetic and oracle-trace based, not a neural-model verifier or end-to-end GPU decoding test. The tested implementation uses brute-force CPU edit-distance search and is not production optimized.

## Claim scope

On a deterministic synthetic edited-repeat oracle benchmark, bounded edit-tolerant prompt lookup increased accepted draft-token coverage and verifier-call speedup proxy relative to exact prompt lookup across 48 swept configurations.

## Why it stopped

Useful bounded mechanism evidence was obtained, but it is synthetic/oracle-trace evidence with brute-force CPU search rather than publication-grade neural verifier or end-to-end GPU latency evidence.

## Recommended next action

Stop this run as no-paper useful signal; next implement indexed edit-tolerant lookup inside a real neural speculative decoding loop and compare exact lookup, tolerant lookup, and no speculation on actual wall-clock generation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-verifier edit-tolerant prompt lookup with indexed search
- Success threshold: At least 10% end-to-end wall-clock speedup over exact prompt lookup on a real neural verifier workload, with identical greedy outputs and no more than 20% zero-accept proposals in the selected operating region.
- Stop condition: Stop if optimized lookup overhead remains above the measured target-call savings or if neural verifier acceptance gains over exact lookup are below 5% accepted tokens per generated token on edited-repeat prompts.

## Evidence references

- Artifact root: `<local-path>/projects/edit-tolerant-prompt-lookup-speculative-decoding-on-10gb-b85b447f23f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
