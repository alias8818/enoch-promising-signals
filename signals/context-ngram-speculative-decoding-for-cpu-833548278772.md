# Context-Ngram Speculative Decoding for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-ngram-speculative-decoding-for-cpu-833548278772`
Run ID: `context-ngram-speculative-decoding-for-cpu-833548278772-20260529T154443348091+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba560ee0641d

## What looked useful

Repeated-block controls reached about 0.77-0.79 ideal target-call reduction, confirming the mechanism for exact repetitions. Natural byte traces reached 0.31-0.40 ideal reduction, but shuffled controls retained most of it; natural word traces were near zero. Break-even verifier overhead on natural byte traces was only about 1.46x-1.66x a single-token call.

## Boundaries and scale limits

No live transformer target, no KV-cache-aware verifier, no wall-clock neural decoding benchmark, one public corpus, deterministic trace matching only. Results should not be generalized to all prompt-lookup speculative decoding systems.

## Claim scope

Trace-level CPU proxy on tiny Shakespeare byte and word streams: context n-gram drafting is useful for exact repeated blocks, but natural-text gains are small after shuffled controls and likely fragile to CPU verifier overhead.

## Why it stopped

Proxy/control evidence does not support a paper-ready CPU speculative decoding claim: natural-trace gains are mostly byte-frequency driven and leave little verifier-overhead margin.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded deepen test should implement real CPU transformer verification and require wall-clock speedup over greedy decoding before reviving the idea.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU prompt-lookup speculative decoding with a real small transformer
- Success threshold: At least 1.15x wall-clock tokens/sec improvement over greedy decoding on natural prompts and at least 1.5x on repetition-heavy prompts, with identical greedy outputs and verifier overhead below the trace-derived break-even range.
- Stop condition: Stop if verifier batch overhead is >=1.7x a single-token call on the target CPU or if natural prompt acceptance remains close to the shuffled-control trace signal.

## Evidence references

- Artifact root: `<local-path>/projects/context-ngram-speculative-decoding-for-cpu-833548278772`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
