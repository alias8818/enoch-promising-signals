# N-gram speculative draft for GPT-2-small inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-gpt-2-small-inference-9ecc23bf69e6`
Run ID: `n-gram-speculative-draft-for-gpt-2-small-inference-9ecc23bf69e6-20260529T074535988040+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ab3b49546753

## What looked useful

The mechanism works when continuations repeat prompt-local token spans: exact n-gram draft verification reduced GPT-2-small target forwards/token from 1.0156 to 0.6807 on constructed natural prose and to 0.2031 on repetition stress prompts, with exact greedy-match checks passing for all assisted runs.

## Boundaries and scale limits

Only 16 prompts per benchmark suite, 64 generated tokens, constructed prompts, unbatched greedy decoding, fp32, simple Python n-gram lookup, and cache-copy rollback. No real traffic trace, no large held-out corpus, no sampling-mode validation, no larger-model validation, and no production serving integration.

## Claim scope

On bounded GPT-2-small greedy decoding tests on GB10/CUDA, prompt-local n-gram speculative drafting exactly matched greedy outputs and reduced target forward passes, improving throughput by 1.34x-1.51x on a constructed natural-prose suite and up to 4.07x on a deliberate repetition suite.

## Why it stopped

Bounded local evidence supports the mechanism but is not broad or naturalistic enough for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with a held-out corpus benchmark, optimized cache rollback/cropping, and confidence intervals before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-scale GPT-2-small n-gram speculative decoding benchmark
- Success threshold: Exact-match rate 100% for greedy decoding and mean throughput at least 1.15x over baseline with confidence interval excluding 1.0 on held-out natural prompts.
- Stop condition: Stop if exactness fails, if optimized assisted decoding is not faster than baseline within confidence intervals, or if acceptance is too rare to reduce target forwards/token on natural prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-gpt-2-small-inference-9ecc23bf69e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
