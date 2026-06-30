# Prompt-Lookup Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-speculative-decoding-on-cpu-e900513231b9`
Run ID: `prompt-lookup-speculative-decoding-on-cpu-e900513231b9-20260620T231552670638+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c76634a5b68a

## What looked useful

Indexed prompt lookup reduced simulated verifier calls by 80-87% on highly repetitive protocol/code-template text with about 7 us lookup overhead per generated token, but gave 0% reduction on low-repetition random text and only 5% reduction on the real project prompt, where projected speed fell below baseline under a 0.25 extra-token verifier cost ratio.

## Boundaries and scale limits

No neural model, production tokenizer, KV-cache behavior, batching, or end-to-end wall-clock model latency was measured; evidence is proxy-only and local to small token streams.

## Claim scope

Dependency-free CPU token-stream benchmark of prompt-lookup speculative decoding mechanics with indexed lookup, exact n-gram prompt reuse, and verifier-call cost projections on four small prompt classes.

## Why it stopped

Proxy-only mixed result: mechanism is useful on exact repetitive contexts, but not broad or paper-ready without direct model latency evidence.

## Recommended next action

Run a bounded direct small-model CPU benchmark with a real tokenizer and target model, comparing greedy baseline against PLD on the same four prompt classes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model CPU latency benchmark for gated prompt-lookup speculative decoding
- Success threshold: At least 1.2x measured tokens/sec on high-repetition/template prompts with no more than 5% slowdown on natural or low-repetition controls when gated.
- Stop condition: Stop if real-model PLD is slower than greedy on both high-repetition and template prompts, or if the gate cannot distinguish beneficial from harmful prompt classes in the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-on-cpu-e900513231b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
