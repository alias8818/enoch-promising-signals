# Curriculum Ordering Effects in Bounded Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `curriculum-ordering-effects-in-bounded-local-pretraining-b8a7b2d5d75e`
Run ID: `curriculum-ordering-effects-in-bounded-local-pretraining-b8a7b2d5d75e-20260628T035728689531+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de30b90b0dd7

## What looked useful

Ordering effects were real in the local probe, but the mechanism was recency/forgetting rather than an easy-first advantage. Interleaving or replay-style mixing should be a required control for future bounded local pretraining curriculum tests.

## Boundaries and scale limits

Synthetic modulo-token data only; tiny 128-d model; 1000 training steps; 3 seeds; no natural-language corpus, GPT-2-small-class baseline, downstream task, or long-run robustness validation. Random mixture was near but not exactly 50/50 per seed.

## Claim scope

In a bounded synthetic causal-language pretraining probe with a 4-layer tiny Transformer, 3 seeds per schedule, 8.192M training tokens per run, and two learnable modulo sequence distributions, curriculum ordering strongly changed final retention: contiguous half-run blocks learned the last distribution and forgot the first, while alternating and near-50/50 random mixtures retained both.

## Why it stopped

Closed as no-paper useful signal: the evidence is reproducible and direct for the synthetic probe, but it is not direct/full evidence for broad local pretraining curriculum claims.

## Recommended next action

Run a bounded direct follow-up on a small real-token corpus with a GPT-2-small-class or parameter-matched model, comparing block order, minibatch interleaving, and replay while measuring phase retention at matched sequence-item budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token retention test for block versus interleaved local pretraining curricula
- Success threshold: Interleaved or replay-control schedules must improve final mean validation loss by at least 10% over both block schedules while retaining each domain within 5% relative loss of its best phase checkpoint.
- Stop condition: Stop if block and interleaved schedules are within 2% final mean validation loss and show no meaningful per-domain retention gap across at least two seeds, or if the run cannot complete within the bounded local compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-effects-in-bounded-local-pretraining-b8a7b2d5d75e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
