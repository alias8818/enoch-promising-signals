# Domain-Balanced Data Mixing Ratios for Tiny GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `68`
Project ID: `domain-balanced-data-mixing-ratios-for-tiny-gpt-2-small-pretraining-05456174fe69`
Run ID: `domain-balanced-data-mixing-ratios-for-tiny-gpt-2-small-pretraining-05456174fe69-20260619T032752000763+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f26d7f39e047

## What looked useful

Strict balancing was best for worst-domain and minority-domain bits/character, while square-root rebalancing was best for natural-weighted bits/character. The result suggests mixture choice should be objective-specific rather than assuming equal domain balance is universally best.

## Boundaries and scale limits

Synthetic corpora, character n-gram model, 60k training characters, 12k validation characters per domain, 9 seeds, CPU-only; no Transformer, no GPT-2-small model, no real tokenizer, and no real web/code/math corpus.

## Claim scope

In a synthetic three-domain fixed-budget character n-gram proxy, equal domain balancing improves balanced-domain, minority-domain, and worst-domain validation loss, but does not optimize natural-weighted validation loss.

## Why it stopped

Closed as no-paper useful signal because this was a proxy early test, not direct GPT-2-small pretraining validation.

## Recommended next action

Run a bounded deepen follow-up with a tiny Transformer and real text domains, comparing natural, equal-balanced, square-root, and minority-boosted mixtures at matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Real-Corpus Check for Domain Mixing Objectives
- Success threshold: Equal balance beats natural by at least 10% on worst-domain validation loss without more than 10% degradation in natural-weighted loss, or square-root rebalancing Pareto-dominates equal balance on natural-weighted and worst-domain losses.
- Stop condition: Stop if no tested rebalanced mixture improves worst-domain validation loss by at least 5% over natural mixing, or if dependencies/compute prevent a tiny Transformer run within the bounded worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/domain-balanced-data-mixing-ratios-for-tiny-gpt-2-small-pretraining-05456174fe69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
