# Suffix-Tree Speculative Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `suffix-tree-speculative-drafting-f5d360f6bd83`
Run ID: `suffix-tree-speculative-drafting-f5d360f6bd83-20260523T225414886999+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

The suffix mechanism sometimes finds repeated passages and beats a sparse 4-gram baseline, but median accepted length is zero, mean matched suffix length is only 2.15 tokens, held-out paired delta versus bigram is +0.006 accepted tokens with 95% CI crossing zero, and the GPT-2 greedy check is numerically worse than bigram.

## Boundaries and scale limits

This is a bounded natural-text probe, not a full serving-system benchmark. It does not test large corpora, prompt-local repetition-heavy workloads, retrieval/fuzzy suffix matching, stochastic target-model acceptance, or end-to-end tokens/second in an optimized decoder.

## Claim scope

On Tiny Shakespeare tokenized with GPT-2 BPE, a longest-exact-suffix copy drafter over 180k reference tokens does not materially outperform a cheap bigram-majority drafter for 8-token speculative drafts, measured against 5k held-out continuations and a 128-context GPT-2 greedy target check.

## Why it stopped

Bounded direct/proxy evidence does not support the hypothesis: exact suffix-copy drafting mostly behaves like a short n-gram table and fails to beat the cheap bigram baseline on the main tested metrics.

## Recommended next action

Stop this exact-suffix drafting line as a paper candidate unless a future bounded study targets repetition-heavy prompt-local workloads and demonstrates end-to-end serving speedup over a bigram or small-model drafter.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-drafting-f5d360f6bd83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
