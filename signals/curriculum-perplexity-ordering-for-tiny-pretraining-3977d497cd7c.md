# Curriculum Perplexity Ordering for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-perplexity-ordering-for-tiny-pretraining-3977d497cd7c`
Run ID: `curriculum-perplexity-ordering-for-tiny-pretraining-3977d497cd7c-20260528T182923362469+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9412444b7082

## What looked useful

Strict easy-to-hard probe-perplexity ordering worsened mean validation perplexity by 60.06% versus random; bucketed easy-to-hard worsened it by 57.24%; hard-to-easy worsened it by 259.11%; an easy-first-then-random control still worsened it by 9.60%. The simple sorted-curriculum mechanism is therefore not promising in this bounded test.

## Boundaries and scale limits

Synthetic data only; tiny non-transformer model; 5 seeds; 3 training epochs; CPU-only local run. This does not validate or refute curriculum ordering for real text corpora, tokenizer-based GPT-style transformers, or larger pretraining scales.

## Claim scope

In a reproducible synthetic tiny next-token pretraining setup using a NumPy bag-context neural language model, ordering training documents by probe-model perplexity did not improve validation perplexity versus random shuffling.

## Why it stopped

Proxy/local evidence was sufficient to show the simple sorted-ordering idea is harmful in the tested tiny setup, but it is not full validation on natural language or transformer pretraining.

## Recommended next action

Stop this run as a proxy early falsification of simple probe-perplexity sorted pretraining; the only worthwhile bounded next test is a real-text tiny-transformer replication before considering any larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny-transformer check for probe-perplexity curriculum ordering
- Success threshold: A curriculum condition must improve mean validation perplexity by at least 3% versus random across seeds without worsening any reported validation slice by more than 5%.
- Stop condition: Stop if all curriculum conditions are worse than random by at least 2% mean validation perplexity after matched token budgets, or if strict sorting again produces clear degradation in all seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-perplexity-ordering-for-tiny-pretraining-3977d497cd7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
