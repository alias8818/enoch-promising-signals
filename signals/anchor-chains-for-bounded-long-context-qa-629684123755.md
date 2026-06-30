# Anchor Chains for Bounded Long-Context QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-chains-for-bounded-long-context-qa-629684123755`
Run ID: `anchor-chains-for-bounded-long-context-qa-629684123755-20260619T054609232077+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d7f0382a986

## What looked useful

Anchor traversal achieved 100% accuracy in the main 240-case sweep and three independent replications. One-shot top-20 retrieval failed all 1000- and 3000-distractor configurations, while anchor traversal read a mean 8.7% of chunks overall and 0.3% to 1.69% of chunks in 3000-distractor settings.

## Boundaries and scale limits

Synthetic exact-anchor data only; no LLM reader, no natural-language corpus, no learned anchor generation, no ambiguous duplicate links, and no adversarial paraphrase robustness. Main run covered 240 cases plus three 240-case seed replications, with up to 3000 distractor chunks and chain length 16.

## Claim scope

In deterministic synthetic long-context QA instances with exact symbolic anchor links, iterative anchor-chain traversal recovered multi-hop answer codes while reading bounded local chunks, and it outperformed one-shot BM25 retrieval under high distractor counts.

## Why it stopped

Closed as no-paper useful signal because the evidence is deterministic synthetic/proxy evidence, not direct validation of LLM long-context QA behavior.

## Recommended next action

Run a bounded LLM-in-the-loop follow-up on naturalized anchor-chain documents with ambiguous and paraphrased links, comparing explicit anchor traversal against iterative retrieval without an anchor schema.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop naturalized anchor-chain QA under fixed context budgets
- Success threshold: At least 15 percentage-point absolute accuracy gain over non-anchor iterative retrieval on 500+ naturalized cases, with no more than 5% wrong-hop unrecoverable failures under the same chunk budget.
- Stop condition: Stop if anchor traversal gains less than 5 percentage points over non-anchor iterative retrieval or if wrong-hop failures exceed 20% in paraphrased/ambiguous-link settings.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-chains-for-bounded-long-context-qa-629684123755`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
