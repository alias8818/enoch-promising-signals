# Small-LM perplexity filter vs heuristic keyword filter for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee`
Run ID: `small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee-20260621T235856481026+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef97128d263b

## What looked useful

Perplexity filtering selected 100% target documents and 0% keyword-spam documents, while keyword filtering selected 22.1% target and 77.9% keyword-spam on average. Downstream validation loss was 0.4482 for perplexity, 0.5692 for keyword, and 0.5104 for random.

## Boundaries and scale limits

Synthetic corpus only; tiny character-level Transformer models; 3 seeds; no real web corpus, tokenizer-scale, GPT-2-small-class, downstream benchmark, or long pretraining validation.

## Claim scope

In a controlled synthetic tiny-pretraining proxy with target, keyword-spam, and off-domain documents, a seed-trained small character LM perplexity filter selected cleaner data and produced lower held-out target loss than a keyword-count filter across 3 seeds.

## Why it stopped

This run produced a useful synthetic proxy signal, but it is not direct/full-scale validation and should remain no-paper evidence.

## Recommended next action

Run a bounded real-corpus follow-up using a GPT-2-small-class tokenizer/model, fixed sequence-item budgets, repeated seeds, and a held-out target-domain validation set before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus bounded comparison of small-LM perplexity filtering against keyword filtering
- Success threshold: Perplexity filtering beats keyword filtering on mean held-out target loss in at least 3 seeds while selecting a materially cleaner corpus under the same token budget.
- Stop condition: Stop if perplexity does not beat keyword on mean held-out target loss, if gains vanish after controlling for selected token count/document length, or if selection audits show no cleaner target-domain composition.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
