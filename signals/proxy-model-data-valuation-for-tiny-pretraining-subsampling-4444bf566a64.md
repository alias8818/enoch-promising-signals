# Proxy-Model Data Valuation for Tiny Pretraining Subsampling

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `proxy-model-data-valuation-for-tiny-pretraining-subsampling-4444bf566a64`
Run ID: `proxy-model-data-valuation-for-tiny-pretraining-subsampling-4444bf566a64-20260621T150713700735+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6ee64797e2

## What looked useful

Proxy bigram valuation improved mean heldout target NLL versus random by 0.109686 at 5%, 0.139713 at 10%, and 0.169239 at 20% subset budgets while selecting 100% relevant documents and 0% target-vocabulary trap documents.

## Boundaries and scale limits

Synthetic documents, small vocabulary, n-gram proxy and target models, small fixed candidate pool, no neural optimizer dynamics, no real tokenizer/corpus, no large-scale pretraining.

## Claim scope

In a synthetic Markov-language tiny-pretraining proxy, additive-smoothed bigram validation-loss-delta document valuation selected better subsets for an additive-smoothed trigram target LM than random, length/order, and unigram-similarity controls across 12 seeds and 5%, 10%, and 20% budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism only in a synthetic n-gram proxy, not in direct neural tiny-pretraining.

## Recommended next action

Run a bounded neural follow-up with a real tokenizer, a 5M-25M parameter transformer, and a small public text corpus to test whether proxy valuation still improves validation loss at fixed sequence-item budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-pretraining proxy valuation on a small public corpus
- Success threshold: Proxy-selected subsets reduce target validation loss by at least 2% relative to random at the same token budget and beat a non-causal similarity baseline on a heldout domain-matched validation split.
- Stop condition: Stop if proxy selection fails to beat random on two independent seeds or if valuation overhead exceeds the target-training cost saved by subsampling.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-model-data-valuation-for-tiny-pretraining-subsampling-4444bf566a64`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
