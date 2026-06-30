# N-Gram Cache Augmented Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cache-augmented-speculative-decoding-de9cb7039e7a`
Run ID: `n-gram-cache-augmented-speculative-decoding-de9cb7039e7a-20260526T002721579103+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Adaptive prompt lookup over n=1..5 reached 1.46875 emitted tokens per target-call proxy, a 31.9% target-call reduction proxy, but chose unigram context for most hits. Restricting to n>=2, the best setting reached only 1.15625 tokens per target call, a 13.5% reduction proxy; higher n values had sparse hits and low full-block acceptance.

## Boundaries and scale limits

Tested one 81.9M-parameter target model, Wikitext-2, 256 held-out prefixes, up to 512-token prefixes, and up to 8-token draft blocks. Did not measure optimized end-to-end wall-clock speculative decoding, stochastic acceptance, larger models, code/chat domains, or long-context serving.

## Claim scope

On a bounded Wikitext-2/distilgpt2 greedy-verification proxy, n-gram cache drafting can modestly reduce target verification calls, but the strongest result depends mostly on unigram/adaptive prompt lookup rather than robust higher-order n-gram continuations.

## Why it stopped

Medium proxy evidence is mixed: the mechanism exists, but higher-order n-gram cache acceptance is too sparse and the best gain mostly comes from unigram fallback, so this is not a paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should implement an end-to-end timed speculative decoder on repetition-heavy code or document workloads and require at least 10-15% wall-clock speedup after all cache and verifier overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Timed Cache-Drafter Speculative Decoding on Repetition-Heavy Workloads
- Success threshold: At least 10-15% end-to-end tokens/sec improvement over greedy decoding with n>=2 cache matches responsible for a material share of accepted draft tokens.
- Stop condition: Stop as negative if optimized end-to-end speedup is below 5% or if accepted-token gains still come primarily from unigram fallback rather than n>=2 cache matches.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-augmented-speculative-decoding-de9cb7039e7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
