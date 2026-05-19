# Suffix-Array Speculative Drafting from Generation History

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-drafting-from-generation-history-eaa2278559d2`
Run ID: `suffix-array-speculative-drafting-from-generation-history-eaa2278559d2-20260519T092200755110+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42690e0b52a

## What looked useful

Generation history contains reusable spans that suffix-based matching can exploit. The mechanism is clearly better than random prior copying and, when tuned, modestly better than last-token copying on sampled GPT-2 traces, but the practical margin is too small and indirect for a paper-ready claim.

## Boundaries and scale limits

Only GPT-2-small-class local inference was tested. Metrics are trace-replay exact-token acceptance and a verifier-call proxy; they exclude optimized online suffix-array overhead, batching, KV-cache effects, real speculative sampling integration, larger models, and production serving latency.

## Claim scope

Local GPT-2 generated-token trace evaluation shows that suffix-history drafting can recover reusable continuations from generation history. On sampled GPT-2 continuations, the best tuned suffix-history configuration reached 1.340 simulated tokens per target/verifier call versus 1.300 for a last-token history baseline and 1.045 for random-prior copying; greedy GPT-2 showed a much larger repetition-driven effect.

## Why it stopped

Trace-level local evidence supports the mechanism but not a publication-grade or deployment-grade claim; sampled decoding gain over the strongest cheap baseline was modest and measured without real draft-construction overhead.

## Recommended next action

Stop this run as no-paper useful signal; next, implement an efficient online suffix or rolling-index drafter in a real speculative decoding loop and require at least 5% wall-clock throughput improvement over last-token and n-gram history baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online suffix-history drafter in a real speculative decoding loop
- Success threshold: At least 5% stable wall-clock tokens/sec improvement over the strongest cheap history baseline, with no regression in target forward-pass count, memory posture, or output validity.
- Stop condition: Stop as negative if the optimized implementation fails to beat the strongest cheap history baseline by 5% wall-clock throughput or if suffix-index maintenance overhead erases the trace-level acceptance advantage.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-drafting-from-generation-history-eaa2278559d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
