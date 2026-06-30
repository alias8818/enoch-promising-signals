# Suffix-array prompt speculation for CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-array-prompt-speculation-for-cpu-919c3afb2908`
Run ID: `suffix-array-prompt-speculation-for-cpu-919c3afb2908-20260528T220031042716+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3af9a9903689

## What looked useful

Suffix-array variable-context lookup did not provide meaningful accepted-token coverage over the best 4-gram table, while adding roughly 132x-450x mean query slowdown at 120k tokens and up to 94x build slowdown. The practical CPU prompt-speculation mechanism is not supported versus a simpler n-gram baseline in this bounded test.

## Boundaries and scale limits

No LLM verifier or production decoder was run; implementation is Python and suffix-array lookup uses binary search plus bounded interval scan. Results cover up to 120k tokens and one CPU process, not native optimized serving or multi-model workloads.

## Claim scope

Bounded CPU proxy for exact prompt-lookup speculation over generated repetitive/protocol/unique streams and local installed Python code, at 40k and 120k token scales, comparing a Python suffix-array prompt index against fixed n-gram occurrence tables.

## Why it stopped

Proxy/early falsification: exact prompt-lookup coverage was equal or worse than n-gram on most datasets and the rare tiny coverage gain was overwhelmed by hundreds-fold CPU query overhead; this is not a full production validation.

## Recommended next action

Stop this suffix-array approach as a no-paper useful signal; only revisit if testing a native suffix automaton/FM-index integrated with an actual CPU LLM verifier against a tuned n-gram baseline.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Native suffix automaton prompt lookup versus n-gram in CPU LLM decoding
- Success threshold: At least 10% end-to-end CPU decoding throughput improvement over tuned n-gram prompt lookup on two real repeated-context workloads, with no more than 5% regression on a low-repeat control.
- Stop condition: Stop if native index lookup remains more than 20x slower than n-gram lookup without at least 5 accepted tokens per 1k target improvement, or if verifier-integrated throughput fails to beat n-gram on the first real workload.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-prompt-speculation-for-cpu-919c3afb2908`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
