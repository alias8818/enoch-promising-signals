# Local N-gram Speculative Decoding with Exact No-Spec Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-n-gram-speculative-decoding-with-exact-no-spec-baseline-3490cbee010b`
Run ID: `local-n-gram-speculative-decoding-with-exact-no-spec-baseline-3490cbee010b-20260527T103611163907+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9e30e000efb9

## What looked useful

Local n-gram draft tokens can be verified against the target model to preserve exact greedy output, and repeated contexts can produce high draft acceptance and fewer target calls in a bounded real-model GPU benchmark.

## Boundaries and scale limits

Tiny model, synthetic repetition-heavy prompts, greedy decoding only, uncached full-context verification, and 320 generated tokens per run; not validated on natural corpora, larger models, sampling, production KV-cache paths, or serving batch conditions.

## Claim scope

On five synthetic repeated-text prompts with sshleifer/tiny-gpt2 greedy decoding, local n-gram speculative decoding exactly matched the no-spec baseline while reducing target-model calls by 42.2-46.9% across a small n/gamma grid and by 45.3% in the main n=4,gamma=6 run.

## Why it stopped

Useful bounded signal only; current evidence is synthetic/tiny-model and does not support a paper or broad deployment claim.

## Recommended next action

Run a bounded deepen test on GPT-2-small with natural-corpus prompts and a KV-cache verification implementation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache local n-gram speculative decoding on natural prompts
- Success threshold: All outputs exact, at least 20% median target-call reduction, and at least 10% median end-to-end latency improvement on a natural-prompt subset with repeated local context.
- Stop condition: Stop if exactness fails, median latency is not improved after KV-cache implementation, or natural prompts show less than 10% target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/local-n-gram-speculative-decoding-with-exact-no-spec-baseline-3490cbee010b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
