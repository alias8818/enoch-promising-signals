# N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-1211dc271ff2`
Run ID: `n-gram-speculative-decoding-1211dc271ff2-20260605T043211141761+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/28b2f05902ed

## What looked useful

Across 144 GPT-2 sweep rows, every speculative decode exactly matched greedy output. Best repeated-span setting was ngram=2,max_draft=8 with 0.243 ideal calls/token and 4.37x ideal call speedup; controls also benefited at 0.264 calls/token and 3.87x, suggesting model self-repetition is a major contributor. This supports the mechanism but not a paper-ready production speedup claim.

## Boundaries and scale limits

Current direct run used GPT-2 small, 24 synthetic prompts, 48 generated tokens per prompt, and ideal verifier-call counting rather than an optimized batched serving implementation. Prior local code-oracle evidence showed weak exact n-gram speedups on held-out Python code streams.

## Claim scope

Exact suffix n-gram drafting can preserve greedy output and reduce ideal target-verifier calls on GPT-2-small-class local greedy decoding for synthetic repeated-span and self-repetitive operational-note prompts.

## Why it stopped

Mechanism supported only under small synthetic and idealized verifier-call evidence; full validation needs optimized batched serving latency evidence, so this is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement true batched KV verification in a serving-style loop and require wall-clock speedup over greedy plus prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched KV verifier for exact n-gram speculative decoding
- Success threshold: Exact greedy match on all prompts and at least 1.3x aggregate wall-clock speedup over greedy with no more than 5% p10 slowdown on controls.
- Stop condition: Stop if exactness fails, cache repair requires full-context recomputation on most rejections, or aggregate wall-clock speedup is below 1.1x after optimization.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-1211dc271ff2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
