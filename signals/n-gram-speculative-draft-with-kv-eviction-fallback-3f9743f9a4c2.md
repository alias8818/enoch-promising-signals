# N-Gram Speculative Draft with KV-Eviction Fallback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-with-kv-eviction-fallback-3f9743f9a4c2`
Run ID: `n-gram-speculative-draft-with-kv-eviction-fallback-3f9743f9a4c2-20260604T134843676615+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d9b13293951

## What looked useful

N-gram drafting is useful when the target model follows local repetition: distilgpt2 accepted 60.0% of drafted tokens and reduced target calls from 96 to 53 across six short prompts. The fallback mechanism preserved exact greedy outputs when synthetic KV budget pressure forced 49 recomputes.

## Boundaries and scale limits

No production incremental KV cache, no paged-attention integration, no broad corpus, no GPT-2-small-class or larger serving benchmark, and no publication-grade latency/throughput measurement.

## Claim scope

On six short repetitive prompts, a Python n-gram speculative verifier matched greedy decoding exactly and reduced target-model forward calls by 44.8% on distilgpt2; a synthetic tight KV budget triggered fallback recomputes without output divergence.

## Why it stopped

Evidence is bounded and partly proxied: exactness, acceptance, call reduction, and fallback triggering were tested, but production KV eviction and real serving throughput were not.

## Recommended next action

Stop this run as a no-paper useful signal; next implement the same verifier against a real incremental KV-cache decoder and benchmark GPT-2-small-class prompts with repetitive/non-repetitive splits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental KV-cache benchmark for n-gram speculative drafting
- Success threshold: At least 15% tokens/sec improvement on repetitive prompts, less than 5% slowdown on non-repetitive prompts, and 100% exact greedy-output match under all tested KV budgets.
- Stop condition: Stop if exactness fails under fallback, or if verifier/fallback overhead removes target-call savings and tokens/sec is not improved on repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-with-kv-eviction-fallback-3f9743f9a4c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
