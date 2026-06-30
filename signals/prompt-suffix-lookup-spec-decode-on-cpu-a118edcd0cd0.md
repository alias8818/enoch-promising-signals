# Prompt-Suffix Lookup Spec-Decode on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-lookup-spec-decode-on-cpu-a118edcd0cd0`
Run ID: `prompt-suffix-lookup-spec-decode-on-cpu-a118edcd0cd0-20260603T162843550265+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/247ced2927e2

## What looked useful

Exact repeated blocks produced 9.59x-12.22x average potential target-call reductions across ngram 4-16 with about 0.92-0.94 draft acceptance; 1% mutation still produced 3.71x-6.59x; random no-reuse stayed at 1.00x with zero accepted drafts; structured records ranged from 1.98x at ngram 4 to about 1.00x at ngram 16. CPU lookup overhead was low, with the corrected sweep completing 9 runs in 18.31 s and max RSS 113 MB.

## Boundaries and scale limits

No real LLM verifier, no BPE tokenizer, no production prompt corpus, and no end-to-end latency measurement; runs used generated traces up to about 257k tokens with pure Python lookup.

## Claim scope

Trace-level synthetic evidence shows CPU prompt-suffix lookup is cheap and can reduce simulated target calls when held-out continuations copy long exact or near-exact spans from the prompt.

## Why it stopped

The result is a bounded synthetic trace useful signal, not direct full validation; it supports the mechanism under repeated-prompt conditions but does not justify a paper-positive claim.

## Recommended next action

Implement the same prompt-boundary-safe lookup in a small CPU language-model decoding loop and measure end-to-end tokens/s versus baseline on real repeated-prompt workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU prompt-lookup speculative decoding with a small real LM
- Success threshold: At least 1.3x end-to-end tokens/s improvement on repeated-prompt workloads with no more than 5% slowdown on no-reuse controls.
- Stop condition: Stop if verifier overhead reduces repeated-prompt speedup below 1.1x or no-reuse controls show more than 10% slowdown after a prompt-boundary-safe implementation.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-lookup-spec-decode-on-cpu-a118edcd0cd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
