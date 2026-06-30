# Distilled n-gram draft speculative decoding for 124M target on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distilled-n-gram-draft-speculative-decoding-for-124m-target-on-gb10-f89e4367142c`
Run ID: `distilled-n-gram-draft-speculative-decoding-for-124m-target-on-gb10-f89e4367142c-20260602T151113757997+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e07d7bd80473

## What looked useful

Order-1 target-distilled n-gram achieved 14.72% acceptance, 1.569x target-forward reduction, and 1.536x wall speedup with exact output equality; prompt-only control achieved only 1.95% acceptance and 1.061x speedup. Order-4 target-distilled fell to 4.35% acceptance and 1.148x speedup, showing sparsity risk.

## Boundaries and scale limits

Evaluated only on 24 held-out synthetic prompts per medium run, 64 generated tokens each, gamma 4, n-gram orders 1/2/4, simple no-cache verification harness, and one 124M-class target. Not validated on natural benchmark corpora, long contexts, stochastic decoding, cache-aware serving, larger models, or neural draft baselines.

## Claim scope

On short synthetic technical prompts with GPT-2-small/gpt2 greedy decoding on GB10, target-distilled low-order n-gram draft tables can reduce exact greedy speculative target forward calls and improve wall-clock throughput versus greedy baseline; naive high-order exact n-grams are sparse and much weaker.

## Why it stopped

No-paper useful signal: bounded local evidence supports low-order target-distilled n-gram drafting but the result is scoped, synthetic, and not a full serving or benchmark validation.

## Recommended next action

Run a cache-aware deepen follow-up on a real held-out prompt benchmark with backoff n-gram distillation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware backoff n-gram speculative decoding on real held-out prompts
- Success threshold: Exact output equality for all prompts, at least 1.25x wall-clock speedup over greedy baseline, and at least 5 percentage points higher acceptance than prompt-only n-gram control on the same prompts.
- Stop condition: Stop as negative if cache-aware wall speedup is below 1.10x or acceptance advantage over prompt-only control is below 2 percentage points after the benchmark ablation.

## Evidence references

- Artifact root: `<local-path>/projects/distilled-n-gram-draft-speculative-decoding-for-124m-target-on-gb10-f89e4367142c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
