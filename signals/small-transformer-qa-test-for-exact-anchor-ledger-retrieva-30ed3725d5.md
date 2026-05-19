# Small Transformer QA Test for Exact Anchor Ledger Retrieval

Status: `useful_signal`
Project ID: `small-transformer-qa-test-for-exact-anchor-ledger-retrieva-30ed3725d5`
Run ID: `small-transformer-qa-test-for-exact-anchor-ledger-retrieva-30ed3725d5-20260517T034744096997+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b9524683d7e6

## What looked useful

The standard small transformer did not demonstrate exact key-conditioned retrieval. On 8-entry ledgers it reached about 12.9% clean exact match, but corrupted-ledger controls and a mean-pool baseline were also about 12.5%, matching the random in-ledger-value hit rate rather than true lookup. On 32-entry ledgers it stayed at global chance through 600 steps.

## Boundaries and scale limits

Tested ledgers up to 32 entries directly; the 32-entry run was stopped at 600 steps after sustained chance performance. The completed diagnostic setting used 8-entry ledgers and 32 values. This does not cover pretrained LLMs, larger models, long natural-language contexts, pointer/copy heads, or extensive hyperparameter search.

## Claim scope

Controlled synthetic anchor-ledger QA with small randomly initialized Transformer encoder models trained from scratch on fresh random ledgers.

## Why it stopped

Early direct falsification for the tested standard small-transformer setup: exact retrieval did not exceed control behavior, so this is useful no-paper evidence rather than publication-grade support.

## Recommended next action

Run a bounded follow-up with an explicit pointer/copy retrieval head and the same clean/corrupt controls before spending larger-scale training budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pointer-head small transformer test for exact anchor-ledger retrieval
- Success threshold: >= 90% clean exact match on ledger_size >= 32 and >= 50 percentage point clean-vs-corrupt gap, with baselines failing to meet the threshold.
- Stop condition: Stop if the pointer/copy model remains below 50% clean exact match after a calibrated run comparable to this Tier 1 budget or if clean accuracy tracks corrupt controls.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-qa-test-for-exact-anchor-ledger-retrieva-30ed3725d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
