# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-e3709a5c0d88`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-e3709a5c0d88-20260608T155652966654+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bdd7ad33d59

## What looked useful

Mechanism supported in high-acceptance repetitive regimes: Pythia-14M median speedups 1.05x to 1.07x and GPT-2 repetitive median 1.10x with exact output. Broad/default CPU acceleration is not supported: GPT-2 natural prompts had 12.5% mean acceptance, no forward reduction, and 1.0047x median speedup.

## Boundaries and scale limits

Small prompt sets only; max 48 generated tokens; no production runtime, quantization, batching, large instruction model, long-context corpus, sampling, or optimized n-gram/KV-cache implementation tested.

## Claim scope

Small CPU-only exact-greedy benchmarks with Python/PyTorch on cached tiny-gpt2, Pythia-14M, and GPT-2 show n-gram draft speculative decoding can reduce forwards and modestly speed decode when prompt-local/model repetition yields high draft acceptance, but not on GPT-2 natural prompts.

## Why it stopped

Bounded proxy/direct small-model evidence mixed: high-acceptance repetitive cases showed modest speedup, but GPT-2 natural prompts were an early falsification of broad CPU speedup because acceptance was low and decode speed was neutral.

## Recommended next action

Stop as no-paper useful signal; only pursue a follow-up if implementing the drafter in a real CPU inference runtime with an adaptive enable/disable policy and evaluating it on a larger natural-prompt corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive N-Gram Drafting in an Optimized CPU Runtime
- Success threshold: At least 1.05x p50 decode speedup on repetitive/code prompts, no more than 1% p50 slowdown on natural prompts after adaptive disabling, and exact greedy output match for every case.
- Stop condition: Stop if optimized acceptance on natural prompts remains below 25% without a reliable pre-decode predictor, or if KV-cache-safe verification overhead erases forward-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-e3709a5c0d88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
