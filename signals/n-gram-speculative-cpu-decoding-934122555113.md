# N-gram speculative CPU decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-cpu-decoding-934122555113`
Run ID: `n-gram-speculative-cpu-decoding-934122555113-20260607T012505183104+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6b86760bd48b

## What looked useful

Order 4-5 n-gram prompt lookup with draft length 8-16 was the strongest region, suggesting local repeated context can provide practical speculative bursts worth testing in a real CPU decoder.

## Boundaries and scale limits

This was a byte-token trace proxy, not a real CPU LLM serving benchmark. It did not measure transformer verifier latency, BPE/SentencePiece tokenization, sampled generation quality, or multi-corpus robustness.

## Claim scope

On a 250k-byte TinyShakespeare trace, exact n-gram speculative drafting reduced target-token verification calls by 21.7% for the best static-train configuration and 31.1% for the best prompt-lookup configuration, with a single-thread Python lookup benchmark completing in 4:38.65 wall time.

## Why it stopped

Proxy trace evidence supports the mechanism but is insufficient for a paper or deployed-speedup claim because no real transformer verifier was benchmarked.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement the drafter inside a CPU LLM runtime and require direct wall-clock speedup over greedy decoding on repeated and non-repeated prompt suites.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM benchmark for n-gram prompt-lookup speculative decoding
- Success threshold: At least 10% median wall-clock tokens/s improvement over greedy decoding on repetition-heavy prompts, no more than 2% slowdown on low-repetition prompts, and exact greedy-output equivalence.
- Stop condition: Stop if integrated verifier overhead erases the trace-level call reduction, if output equivalence fails, or if median speedup is below 5% on repetition-heavy prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-cpu-decoding-934122555113`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
