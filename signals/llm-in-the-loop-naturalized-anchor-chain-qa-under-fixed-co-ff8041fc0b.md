# LLM-in-the-loop naturalized anchor-chain QA under fixed context budgets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-in-the-loop-naturalized-anchor-chain-qa-under-fixed-co-ff8041fc0b`
Run ID: `llm-in-the-loop-naturalized-anchor-chain-qa-under-fixed-co-ff8041fc0b-20260619T061015016631+0000`

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

- Parent run decision: Anchor Chains for Bounded Long-Context QA: enoch://control-plane/projects/anchor-chains-for-bounded-long-context-qa-629684123755/runs/anchor-chains-for-bounded-long-context-qa-629684123755-20260619T054609232077+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d7f0382a986

## What looked useful

Across the corrected 120-example Tier 1 run, anchor-chain retrieval achieved 100% exact answer and terminal-hit rate versus 0% for one-shot retrieval under the same budget. A budget-below-chain ablation dropped anchor-chain exact accuracy to 0%, showing the mechanism depends on having enough retrieval/context steps to reach terminal evidence.

## Boundaries and scale limits

The test used synthetic chunks, BM25 retrieval, chunk-count budgets, and rule-based anchor/answer extraction. It did not test a real generative LLM in the loop, real documents, paraphrased anchors, noisy evidence, or token-level context packing.

## Claim scope

In a deterministic synthetic multi-hop QA corpus where each gold chunk contains a natural-language next-anchor handoff and the retrieval budget equals the chain length, iterative anchor-chain retrieval recovered terminal answer evidence while one-shot fixed-budget retrieval did not.

## Why it stopped

Tier 1 evidence supports the anchor-chain retrieval mechanism but not the full LLM-in-the-loop naturalized QA claim; this is no-paper useful signal rather than paper-positive validation.

## Recommended next action

Run a bounded direct follow-up where a small local instruct or QA model performs anchor extraction and final answer generation on 100-200 generated cases under the same fixed token budget, with one-shot retrieval as the control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model LLM-in-the-loop anchor-chain QA under fixed token budgets
- Success threshold: At least 80% exact-answer accuracy for the anchor-chain method and at least 30 percentage points improvement over one-shot retrieval on 100-200 cases, with per-hop anchor extraction accuracy at least 90%.
- Stop condition: Stop if anchor extraction falls below 70% on a 30-case smoke test or if anchor-chain exact accuracy is not at least 15 percentage points above one-shot in the first 100 cases.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-naturalized-anchor-chain-qa-under-fixed-co-ff8041fc0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
