# Perplexity-Ordered Curriculum for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-ordered-curriculum-for-tiny-gpt-2-pretraining-186c3c72bb19`
Run ID: `perplexity-ordered-curriculum-for-tiny-gpt-2-pretraining-186c3c72bb19-20260628T170943933637+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cb0d99f13efd

## What looked useful

Strict perplexity sorting was an early falsification of the naive curriculum: random ordering reached mean validation perplexity 4.950, while easy-to-hard reached 12.368, hard-to-easy 11.160, and band-shuffle 11.123. The probe correctly ranked easy, medium, and hard document families, but sorted streams created harmful exposure imbalance.

## Boundaries and scale limits

CPU-only local probe; synthetic corpus; character-level tokenization; 2-layer 64-dim causal Transformer; 160 optimizer steps; 3 seeds per schedule; does not validate GPT-2-small, BPE tokenization, natural web corpora, or long-run convergence.

## Claim scope

On a deterministic synthetic character-level corpus, a 2-layer tiny GPT-style causal Transformer trained with strict probe-perplexity document ordering performed substantially worse than random document ordering after matched optimizer steps and token budget.

## Why it stopped

Proxy-scale early falsification of naive strict perplexity ordering, not a full validation of curriculum learning for GPT-2 pretraining.

## Recommended next action

Stop this run as a no-paper useful negative; the next bounded test should use exposure-balanced perplexity curricula on a natural text subset with a GPT-2 or byte-level tokenizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exposure-Balanced Perplexity Curriculum on Natural Text
- Success threshold: Exposure-balanced perplexity curriculum improves mean validation perplexity by at least 3% over random ordering across 3 seeds without any difficulty stratum degrading by more than 2%.
- Stop condition: Stop if the curriculum fails to beat random mean validation perplexity or repeats the stratum-specific degradation seen in the strict sorted probe.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-ordered-curriculum-for-tiny-gpt-2-pretraining-186c3c72bb19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
