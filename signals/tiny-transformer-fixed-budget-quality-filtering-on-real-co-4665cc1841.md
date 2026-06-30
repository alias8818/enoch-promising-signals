# Tiny transformer fixed-budget quality filtering on real corpus slices

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-transformer-fixed-budget-quality-filtering-on-real-co-4665cc1841`
Run ID: `tiny-transformer-fixed-budget-quality-filtering-on-real-co-4665cc1841-20260614T074121995891+0000`

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

- Parent run decision: Tiny Pretraining with Bounded Data Selection: Quality Filtering Effects at Scale: enoch://control-plane/projects/tiny-pretraining-with-bounded-data-selection-quality-filtering-effects-at-scale-4552400e8255/runs/tiny-pretraining-with-bounded-data-selection-quality-filtering-effects-at-scale-4552400e8255-20260614T071052073101+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

Top-only fixed-budget quality filtering failed the predeclared +0.02 nats improvement threshold, with quality_top -0.031743 nats worse than random. Bottom-quality slices were +0.482362 nats worse than random, indicating the heuristic detects harmful text but the top-only selection policy is not useful in this bounded setup.

## Boundaries and scale limits

Only WikiText-2 raw, byte-level tokenization, 49152 training bytes per condition, 32768 validation bytes, 3 seeds, 120 steps, 2-layer 64-dim Transformer, and a hand-built printable/alpha/unique/length quality heuristic were tested. Larger corpora, learned filters, bottom-only rejection policies, longer training, and GPT-2-small-class models remain untested.

## Claim scope

On a CPU-bounded Tier 1 tiny byte-level Transformer trained for 120 steps on equal 49152-byte WikiText-2 raw train slices, the tested simple top-only text-quality filter did not improve validation loss versus seeded random selection; the same heuristic did identify strongly harmful bottom-quality slices.

## Why it stopped

Tier 1 direct test completed and failed the success threshold; result is an early bounded falsification of the top-only heuristic, not a full-scale rejection of all quality filtering.

## Recommended next action

Run one bounded deepen follow-up that filters out only the bottom quartile while sampling the remaining WikiText-2 lines randomly, using at least 5 seeds and the same fixed-budget tiny Transformer threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bottom-quartile rejection instead of top-only quality selection for fixed-budget tiny Transformer training
- Success threshold: Bottom-quartile rejection improves mean final validation loss versus random by at least 0.02 nats and beats top-only selection, with no more than one losing seed out of five.
- Stop condition: Stop if bottom-quartile rejection fails to beat random by 0.02 nats mean validation loss or if slice metadata shows the policy does not preserve broader coverage than top-only selection.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-fixed-budget-quality-filtering-on-real-co-4665cc1841`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
