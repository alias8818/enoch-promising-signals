# Gradient-based coreset selection for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-based-coreset-selection-for-tiny-cpu-pretraining-1f5f0f04bdd7`
Run ID: `gradient-based-coreset-selection-for-tiny-cpu-pretraining-1f5f0f04bdd7-20260522T133704532353+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c1981d2fd8ee

## What looked useful

Gradient matching to either the full initial gradient or a small clean probe selected 100% in-domain examples and achieved mean validation loss 0.542-0.649 across 5%-20% subsets, compared with random at 1.203-1.239 and full mixed-data training at 1.170. Gradient norm was only partly useful, and greedy OMP full-gradient matching failed by selecting mostly noise.

## Boundaries and scale limits

Evidence is limited to a synthetic Markov-token corpus, a bigram model, 5 random seeds, and short CPU-only runs. It does not validate transformer pretraining, real text corpora, optimized CPU throughput, or large-scale coreset behavior.

## Claim scope

In a controlled synthetic bigram language-model proxy with mixed useful and distractor token streams, cosine-style gradient matching at initialization selected useful examples and substantially reduced held-out in-domain next-token loss versus random subset selection under tiny CPU training budgets.

## Why it stopped

No-paper useful signal: the local proxy supports a mechanism for one selector family but is synthetic and model-simple, so it cannot support a publication-grade or broad pretraining claim.

## Recommended next action

Run a bounded deepen follow-up on a real tiny text corpus with a tiny transformer, comparing random, quality-filter, gradient-cosine matching, and gradient-norm selection under matched CPU token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-transformer test of gradient-cosine coreset selection
- Success threshold: Gradient-cosine matching improves mean held-out validation loss by at least 5% relative to random and matches or beats a simple quality-filter baseline at the same token budget across at least 3 seeds.
- Stop condition: Stop if gradient-cosine matching fails to beat random by 2% mean validation loss or if selector overhead exceeds the saved training compute under the tiny CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-based-coreset-selection-for-tiny-cpu-pretraining-1f5f0f04bdd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
