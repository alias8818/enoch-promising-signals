# N-gram suffix-tree speculative decoding with exact-match guarantee

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-with-exact-match-guarantee-c51611388ee3`
Run ID: `n-gram-suffix-tree-speculative-decoding-with-exact-match-guarantee-c51611388ee3-20260611T131728198704+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a0d9ea87e241

## What looked useful

Suffix-history drafting can exactly preserve greedy decoding while producing useful proposals on repetitive/structured GPT-2 traces. The main run measured 72.6% token acceptance, 12.8% proposal-start coverage, and a 3.36x idealized target-call reduction upper bound, but generated traces show repetition dominates the benefit.

## Boundaries and scale limits

Small GPT-2 model only; hand-written prompt set; greedy decoding only; offline verifier-call accounting only; no production speculative loop, batching, KV-cache policy, stronger model, sampled decoding, or end-to-end latency validation.

## Claim scope

On 10 hand-written prompts with openai-community/gpt2 greedy continuations of 128 tokens, a suffix-history n-gram drafter preserved exact target output under oracle verification and reduced idealized verifier calls from 1280 to 381 at min_suffix=2, with the effect persisting but weakening at min_suffix=8.

## Why it stopped

Closed as no-paper useful signal because this run produced direct exact-match and verifier-call evidence, but only proxy latency evidence on a small, repetitive GPT-2 trace set rather than publication-grade serving validation.

## Recommended next action

Run a bounded deepen follow-up that implements the verifier in a real generation loop for a stronger small model and a larger prompt set, requiring exact output equality plus measured latency improvement over baseline greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-loop suffix-history speculative decoding latency test
- Success threshold: At least 15% median latency reduction and no exact-output mismatches on at least 100 prompts, with no prompt category showing a median slowdown above 10%.
- Stop condition: Stop if exact-output mismatches occur, if median latency improvement is below 5%, or if acceptance/coverage diagnostics show the benefit is confined only to degenerate repeated-output traces.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-with-exact-match-guarantee-c51611388ee3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
