# Local Synthetic-Then-Filter Pipeline vs Pure Human Text at Fixed Tokens

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-synthetic-then-filter-pipeline-vs-pure-human-text-at-fixed-tokens-0ac431e78b0d`
Run ID: `local-synthetic-then-filter-pipeline-vs-pure-human-text-at-fixed-tokens-0ac431e78b0d-20260610T215030824279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/469411b4e18c

## What looked useful

Pure human text had lower held-out validation loss in all three seeds; mean synthetic-minus-human loss was +0.025082 nats, with one near tie and two clearer human wins. The filter selected fluent low-repetition synthetic chunks, but the downstream learner still generalized slightly worse to human text.

## Boundaries and scale limits

Test used 120,000 characters per condition, a 651,034-parameter character Transformer, 700 optimizer updates, three seeds, a local n-gram generator, and heuristic likelihood/repetition filtering. It does not validate or falsify stronger open-weight generators, learned filters, subword token budgets, GPT-2-small-class models, or large-scale LLM pretraining.

## Claim scope

In a bounded WikiText-2 character-LM probe, a local n-gram synthetic-then-filter pipeline did not match or beat equal-budget pure human text for held-out human language-model loss.

## Why it stopped

Proxy/local early falsification of the tested n-gram synthetic-then-filter variant, not a full validation or full rejection of all synthetic-data pipelines.

## Recommended next action

Stop this run as a no-paper useful signal; the bounded next test is a subword GPT-2-small-class comparison using a stronger local/open-weight generator and learned filter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword GPT-2-small Synthetic-Filter Data Quality Probe
- Success threshold: Filtered synthetic is no worse than pure human by more than 0.01 nats validation loss on average, with no seed worse by more than 0.03 nats, and beats unfiltered synthetic.
- Stop condition: Stop if filtered synthetic remains worse than pure human by more than 0.03 nats in two or more seeds, or if quality filtering collapses diversity relative to human text.

## Evidence references

- Artifact root: `<local-path>/projects/local-synthetic-then-filter-pipeline-vs-pure-human-text-at-fixed-tokens-0ac431e78b0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
