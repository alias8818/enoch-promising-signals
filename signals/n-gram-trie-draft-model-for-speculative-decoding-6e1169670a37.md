# N-gram Trie Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-trie-draft-model-for-speculative-decoding-6e1169670a37`
Run ID: `n-gram-trie-draft-model-for-speculative-decoding-6e1169670a37-20260610T160658615084+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/462adb24c06c

## What looked useful

The trie accepted 3.10/4 and 4.84/8 tokens on synthetic logs and 3.52/4 and 6.27/8 on repeated code, but only 0.53/4 on Alice and 0.33/4 on Tiny Shakespeare. The idea is domain-dependent rather than a general draft-model replacement.

## Boundaries and scale limits

CPU-only proxy run over small public/synthetic corpora; no target LLM, no speculative decoding acceptance kernel, no sampler interaction, and no end-to-end tokens/sec measurement. Largest table tested was a naive Python order-16 table estimated at 2.5 GB on Tiny Shakespeare.

## Claim scope

A GPT-2-token n-gram suffix trie can draft useful exact-token prefixes on highly repetitive held-out streams such as synthetic logs and templated code, but the same proxy evaluation shows weak acceptance on natural prose.

## Why it stopped

Closed as no-paper useful signal because this was a proxy early falsification of broad natural-text usefulness, not direct/full speculative decoding validation.

## Recommended next action

Run a bounded real-target speculative decoding test with a small local LLM on repetitive prompts and require both accepted tokens per target call and end-to-end tokens/sec improvement over no draft and a simple learned or n-gram baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-target speculative decoding test for n-gram trie drafts on repetitive domains
- Success threshold: At least 1.5 accepted tokens per target call and at least 15% end-to-end tokens/sec improvement over no draft on repetitive-domain prompts, with no correctness regression versus the target sampler.
- Stop condition: Stop if real target acceptance falls below 1.0 accepted token per target call or if trie lookup/memory overhead eliminates throughput gains on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-trie-draft-model-for-speculative-decoding-6e1169670a37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
