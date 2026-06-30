# N-gram Suffix Trie Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-trie-speculative-decoding-on-cpu-7190651412ee`
Run ID: `n-gram-suffix-trie-speculative-decoding-on-cpu-7190651412ee-20260619T143830483044+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4aa8e15361c3

## What looked useful

Best suffix-trie replay achieved 9.20x idealized target-step speedup on repetitive project scaffold text, 2.58x on synthetic repetitive logs, and 2.57x on low-entropy Markov text; the high-entropy control achieved only 1.00017x with 1 accepted token over 22,440 proposals.

## Boundaries and scale limits

Small local/synthetic corpora only: 5.3k to 20k regex tokens; no real LLM, tokenizer, KV cache, or end-to-end CPU serving latency.

## Claim scope

Bounded trace-replay evidence shows an n-gram suffix-trie drafter can reduce idealized target verification steps on repetitive, low-entropy, or template-like token traces, but not on a high-entropy random-token control.

## Why it stopped

Proxy-only bounded evidence is useful and domain-specific but incomplete for a paper claim; this is an early mechanism result rather than full LLM-serving validation.

## Recommended next action

Run a bounded real-model follow-up on a small CPU-served LM with a real tokenizer, measuring end-to-end latency on repetitive traces versus a no-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer CPU latency test for suffix-trie drafting on repetitive traces
- Success threshold: At least 20% end-to-end tokens-per-second improvement on repetitive traces with no regression greater than 5% on the negative-control corpus.
- Stop condition: Stop if real-tokenizer acceptance on repetitive traces is below 25% any-token acceptance or if drafter overhead erases the target-step reduction in a smoke run.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-trie-speculative-decoding-on-cpu-7190651412ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
