# Instruction Mix Ratio for Tiny Base Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `instruction-mix-ratio-for-tiny-base-pretraining-d1285a9e88bf`
Run ID: `instruction-mix-ratio-for-tiny-base-pretraining-d1285a9e88bf-20260530T075323366093+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/38af9342d8d1

## What looked useful

Instruction exposure has a clear likelihood tradeoff curve at toy scale: 0% instruction failed instruction-format likelihood, 10-25% captured most instruction-NLL gain with small base-NLL cost, and 50% degraded base NLL. Exact instruction answering stayed weak and held-out numeric generalization was 0% at every ratio.

## Boundaries and scale limits

Toy synthetic data, character-level one-hidden-layer causal model, 1200 optimization steps, three seeds per ratio, no transformer, no real corpus, no large-scale pretraining, no natural instruction benchmark.

## Claim scope

In a synthetic fixed-budget tiny NumPy character-level causal LM, 10-25% instruction-formatted examples sharply reduced held-out instruction-format character NLL with only modest base-language NLL degradation, but did not produce held-out-number exact answer generalization.

## Why it stopped

The local experiment completed and produced a reproducible toy tradeoff, but evidence is proxy-only for real pretraining and exact held-out instruction generalization was zero.

## Recommended next action

Run a bounded tiny-transformer confirmation on the same ratio grid before considering any paper claim; treat this run as a toy useful signal, not validation of real base pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Confirmation of Instruction Mix Ratio Tradeoff
- Success threshold: A 10-25% instruction ratio improves instruction held-out NLL by at least 40% versus 0% while increasing base NLL by less than 5%, and achieves nonzero held-out-number exact accuracy across at least two of three seeds.
- Stop condition: Stop if the transformer also has 0% held-out-number exact accuracy at all ratios or if the best instruction-NLL ratio requires more than 10% base-NLL degradation.

## Evidence references

- Artifact root: `<local-path>/projects/instruction-mix-ratio-for-tiny-base-pretraining-d1285a9e88bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
