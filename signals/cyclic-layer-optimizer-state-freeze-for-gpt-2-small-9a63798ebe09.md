# Cyclic layer optimizer state freeze for GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cyclic-layer-optimizer-state-freeze-for-gpt-2-small-9a63798ebe09`
Run ID: `cyclic-layer-optimizer-state-freeze-for-gpt-2-small-9a63798ebe09-20260605T012654254649+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/210199ea0250

## What looked useful

For cyclic layer training, leaving inactive block gradients as None is preferable to assigning zero gradients just to decay AdamW state: it avoids inactive-weight drift and saves optimizer compute without improving short-horizon synthetic loss.

## Boundaries and scale limits

Synthetic data only, 120 optimizer steps, batch size 2, sequence length 128, three seeds, no natural-language corpus, no long-run perplexity convergence, and no hyperparameter sweep.

## Claim scope

In a 3-seed, 120-step synthetic next-token task using GPT-2-small geometry, cyclic layer training with inactive AdamW state frozen preserved inactive weights exactly, ran about 1.88x faster than explicit zero-gradient state decay, and had no meaningful eval-loss disadvantage.

## Why it stopped

Proxy-scale useful signal only; synthetic short-run evidence is insufficient for a paper-positive GPT-2-small training claim.

## Recommended next action

Run a bounded real-corpus deepen test on GPT-2-small geometry for a few thousand steps comparing cyclic freeze, cyclic zero-decay, dense AdamW, and momentum-reset variants under matched sequence-item budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus cyclic optimizer state freeze confirmation for GPT-2-small
- Success threshold: Cyclic freeze has validation perplexity no worse than zero-decay by 1% at matched tokens, retains at least 25% throughput advantage, and shows no instability across seeds.
- Stop condition: Stop if cyclic freeze is more than 1% worse in validation perplexity than zero-decay in two of three seeds or loses the measured optimizer-throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/cyclic-layer-optimizer-state-freeze-for-gpt-2-small-9a63798ebe09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
