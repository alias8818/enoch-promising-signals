# End-to-end CPU prompt lookup decoding with compact suffix index

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-cpu-prompt-lookup-decoding-with-compact-suffix-e3cb192127`
Run ID: `end-to-end-cpu-prompt-lookup-decoding-with-compact-suffix-e3cb192127-20260611T045010229419+0000`

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

- Parent run decision: Prompt Lookup Decoding on CPU with suffix-trie index: enoch://control-plane/projects/prompt-lookup-decoding-on-cpu-with-suffix-trie-index-0317b32c9cbe/runs/prompt-lookup-decoding-on-cpu-with-suffix-trie-index-0317b32c9cbe-20260611T042351507508+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd153879496d

## What looked useful

Indexed PLD matched greedy/naive outputs, cut proposal search by 64x on repeated prompts and 149x on low-repeat miss-heavy prompts, reduced verifier calls from 384 to 58 on repeated prompts, and beat greedy decode-only latency by 1.25x only when prompt continuations repeated.

## Boundaries and scale limits

Synthetic token streams and deterministic verifier with calibrated CPU work only; no real neural LM, tokenizer, KV cache, natural corpus, or production serving stack was tested. One-off index build can erase the short repeated-prompt win when charged against only 384 generated tokens.

## Claim scope

In a controlled CPU decoder harness with 4096-token prompts and 384 generated tokens, a compact suffix index preserves PLD output equivalence versus naive reverse scan and greatly reduces proposal-search overhead; it improves decode-only latency on repeated prompts but adds overhead on low-repeat prompts.

## Why it stopped

No-paper closure: Tier 1 direct decoder-path evidence supports the mechanism but uses a deterministic verifier rather than a real neural LM, and the low-repeat control shows indexed PLD needs gating before any serving claim.

## Recommended next action

Run a bounded real CPU LM integration that includes tokenizer, KV-cache verification, index-build cost, natural repeated-context prompts, and a hit-rate gate that disables PLD on low-repeat prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LM prompt lookup decoding with suffix-index gating
- Success threshold: At least 1.15x end-to-end tokens/s over greedy on repeated-context prompts after index-build cost, with no more than 5% slowdown on low-repeat controls when the gate is enabled.
- Stop condition: Stop if real-model integration cannot preserve output correctness/acceptance semantics, or if indexed PLD is below 1.05x on repeated prompts or slows low-repeat controls by more than 5% with gating.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-cpu-prompt-lookup-decoding-with-compact-suffix-e3cb192127`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
