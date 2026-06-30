# Perplexity-bucketed subset selection for tiny GPT-2-class pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-bucketed-subset-selection-for-tiny-gpt-2-class-pretraining-624b6c9a46ce`
Run ID: `perplexity-bucketed-subset-selection-for-tiny-gpt-2-class-pretraining-624b6c9a46ce-20260611T115324484440+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65828253bdb7

## What looked useful

Bucketed uniform selection was effectively tied with random on test bits/byte: 2.3227 vs 2.3231, mean delta -0.00033 bpb with paired seed differences in both directions. Easy-only selection was worse by +0.0503 bpb. Hard-only selection improved test bpb but worsened validation bpb, so it is diagnostic rather than support for the bucketed hypothesis.

## Boundaries and scale limits

This run did not train a GPT-2-style transformer, did not use BPE tokenization, did not test large corpora, and did not evaluate downstream transfer. It is an early proxy falsification, not a full-scale transformer validation.

## Claim scope

In a bounded WikiText-2 byte-level causal LM proxy with 600 candidate documents, 180k selected bytes, five stochastic seeds, and fixed validation/test evaluation, uniform teacher-perplexity bucket selection did not reliably improve held-out perplexity over random document selection.

## Why it stopped

Proxy/early falsification: the intended bucketed policy did not beat random beyond noise in the local causal-LM proxy, so this is insufficient for a paper or large-scale escalation.

## Recommended next action

Stop this run as a no-paper useful signal; the only warranted next test is a bounded direct tiny-transformer replication in an environment with PyTorch support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer replication of perplexity-bucketed subset selection
- Success threshold: Bucketed_uniform beats random by at least 0.02 bits/token-equivalent mean validation loss with no worse test loss and consistent sign across at least three seeds.
- Stop condition: Stop if bucketed_uniform remains within random variation or underperforms random after the planned matched-budget transformer run.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucketed-subset-selection-for-tiny-gpt-2-class-pretraining-624b6c9a46ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
