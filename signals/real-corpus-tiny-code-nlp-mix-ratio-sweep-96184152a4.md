# Real-Corpus Tiny Code/NLP Mix Ratio Sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-tiny-code-nlp-mix-ratio-sweep-96184152a4`
Run ID: `real-corpus-tiny-code-nlp-mix-ratio-sweep-96184152a4-20260612T074903961409+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Code/NLP Mix Ratio Sweep for Tiny Mixed-Domain Pretraining: enoch://control-plane/projects/code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f/runs/code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f-20260611T214922817279+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c7cadde24a06

## What looked useful

The 50% code mix beat the best endpoint-only control by 11.37% to 13.47% balanced mean validation loss across three seeds; the main five-ratio sweep found 50% code best overall, with 25% and 75% also much better than endpoints.

## Boundaries and scale limits

842k-parameter byte-level Transformer, short 500-step runs, small fixed corpora, one architecture, no downstream task evaluation, and limited ratio/seed coverage beyond the endpoint-vs-50% persistence check.

## Claim scope

On a fixed small real-corpus byte-level causal LM test using Project Gutenberg NLP text and CPython code, a 50% code / 50% NLP training batch mix achieved lower balanced mean held-out loss than endpoint-only training across three seeds.

## Why it stopped

Tier 1 direct validation produced a stable useful signal but not publication-grade evidence.

## Recommended next action

Run a bounded medium confirmation with a subword tokenizer or GPT-2-small-class model, broader real code/NLP corpora, at least three seeds, and the same endpoint controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-corpus code/NLP mix confirmation with subword GPT baseline
- Success threshold: A mixed ratio beats the best endpoint-only control by at least 3% balanced mean validation loss with overlapping-seed stability and without worsening either domain by more than 10% versus its domain-best endpoint.
- Stop condition: Stop if no mixed ratio beats the best endpoint by at least 1% after three seeds, or if the effect only appears in the byte-level setup and disappears in the subword/GPT-style model.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-code-nlp-mix-ratio-sweep-96184152a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
