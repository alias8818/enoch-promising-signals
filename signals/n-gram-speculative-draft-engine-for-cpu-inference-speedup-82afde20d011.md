# N-gram speculative draft engine for CPU inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-engine-for-cpu-inference-speedup-82afde20d011`
Run ID: `n-gram-speculative-draft-engine-for-cpu-inference-speedup-82afde20d011-20260528T234211062081+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

On Tiny Shakespeare trace replay, n-gram drafting reduced target verifier calls by at most 11.44% and accepted only 0.129 draft tokens per call; single-thread CPU verifier proxy costs made every tested setting slower than baseline. An exact-repeat positive control reached 94.05% call reduction, showing the mechanism works when context repetition is strong.

## Boundaries and scale limits

No production LLM runtime, no real logits, regex tokenization rather than BPE, one natural-language corpus, and verifier timing measured with a transformer-shaped NumPy kernel rather than an optimized CPU inference backend.

## Claim scope

Bounded proxy evaluation of prompt-lookup n-gram speculative drafting on a 178k-token natural-language trace, plus a NumPy CPU verifier-cost proxy and an exact-repeat positive control.

## Why it stopped

Early proxy falsification rather than full validation: natural-text acceptance was too sparse to overcome measured CPU verifier costs, although exact repeated context remained strongly positive.

## Recommended next action

Stop this general natural-text proxy as no-paper evidence; run a bounded real-backend follow-up on code or retrieval-heavy prompts where repeated context may make n-gram drafting viable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU backend n-gram speculation on code and retrieval-heavy prompts
- Success threshold: At least 1.15x end-to-end tokens/sec over greedy baseline on one repetition-prone dataset with accepted draft tokens per call >= 0.75 and no quality/output-regression evidence.
- Stop condition: Stop if accepted draft tokens per call stay below 0.5 or end-to-end speedup stays below 1.05x after tuning n in 2..8 and draft window K in 1..16.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-engine-for-cpu-inference-speedup-82afde20d011`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
