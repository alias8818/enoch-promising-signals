# N-gram speculative draft for GPT-2-small edge decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-gpt-2-small-edge-decoding-0353782fdcc1`
Run ID: `n-gram-speculative-draft-for-gpt-2-small-edge-decoding-0353782fdcc1-20260604T210241015676+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/29b621a996c5

## What looked useful

Static prompt n-grams rarely accepted more than one token per verifier call and did not accelerate a KV-cached baseline. Dynamic generated-context n-grams can exploit repeated generated phrases and produced exact float32 speedup, but fp16/bfloat16 exactness failures make the edge deployment claim unsafe without precision-focused follow-up.

## Boundaries and scale limits

Small prompt set, GPT-2-small only, greedy decoding only, single GB10 GPU, no batching, no quantized serving stack, no public benchmark suite, and reduced-precision dynamic verification failed exact-match checks.

## Claim scope

On 8 local built-in prompts with 96-token GPT-2-small greedy decoding on NVIDIA GB10, static prompt-only n-gram drafting exactly matched output but was effectively neutral/slower, while dynamic generated-context n-gram drafting with float32 exactly matched output and improved mean throughput by 1.271x with 27.4% fewer target forwards.

## Why it stopped

Medium local evidence is mixed: the static version is non-viable, and the dynamic version is promising only in float32 while reduced-precision edge inference fails exact greedy equivalence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should make dynamic n-gram verification precision-safe for fp16/bfloat16 and validate on a public prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Precision-safe dynamic n-gram speculative decoding for GPT-2-small
- Success threshold: All tested reduced-precision prompts exactly match baseline, mean target-forward reduction is at least 15%, and mean warmed throughput speedup is at least 1.15x versus KV-cached greedy decoding.
- Stop condition: Stop if reduced-precision exactness cannot be guaranteed without losing speedup below 1.05x, or if public-prompt acceptance falls below 1.2 accepted tokens per verifier call.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-gpt-2-small-edge-decoding-0353782fdcc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
