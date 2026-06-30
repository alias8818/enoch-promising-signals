# N-gram speculative draft accelerates GPT-2-small CPU autoregression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-accelerates-gpt-2-small-cpu-autoregression-48e9aa36a966`
Run ID: `n-gram-speculative-draft-accelerates-gpt-2-small-cpu-autoregression-48e9aa36a966-20260529T012513614652+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2bfc7b76631e

## What looked useful

N-gram drafting preserved exact greedy output and gave a 1.099x mean speedup versus full-context no-cache greedy, but only reduced target calls by 5.21% and ran at 0.437x the throughput of standard cached greedy. Acceptance was sparse: 10 accepted draft tokens out of 26 proposed across 192 generated tokens.

## Boundaries and scale limits

Does not test cache-aware speculative verification, tuned CPU serving runtimes, larger prompt suites, long-context/repetition-rich workloads, sampling, batching, quantization, or larger models.

## Claim scope

Bounded GPT-2-small CPU benchmark using Hugging Face/PyTorch greedy decoding on 4 fixed prompts x 2 repeats x 24 generated tokens; the implemented n-gram draft verifier is exact but full-context/no-cache.

## Why it stopped

Direct bounded GPT-2-small CPU evidence shows the simple n-gram speculative draft is non-competitive with the practical cached greedy autoregression baseline, even though it slightly improves over an unoptimized no-cache baseline.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded follow-up if implementing cache-aware verification that must beat cached greedy by at least 1.15x on a predeclared prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware n-gram speculative verification for GPT-2-small CPU
- Success threshold: Sustained >=1.15x mean tokens/s and >=1.05x median tokens/s versus cached greedy with zero exactness failures and at least 20% target-call reduction on the repetition-positive bucket.
- Stop condition: Stop if cache-aware implementation still fails to exceed 1.05x median throughput versus cached greedy or if exactness failures occur under deterministic greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-accelerates-gpt-2-small-cpu-autoregression-48e9aa36a966`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
