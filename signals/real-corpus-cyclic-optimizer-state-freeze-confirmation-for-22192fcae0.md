# Real-corpus cyclic optimizer state freeze confirmation for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-cyclic-optimizer-state-freeze-confirmation-for-22192fcae0`
Run ID: `real-corpus-cyclic-optimizer-state-freeze-confirmation-for-22192fcae0-20260605T053014275731+0000`

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

- Parent run decision: Cyclic layer optimizer state freeze for GPT-2-small: enoch://control-plane/projects/cyclic-layer-optimizer-state-freeze-for-gpt-2-small-9a63798ebe09/runs/cyclic-layer-optimizer-state-freeze-for-gpt-2-small-9a63798ebe09-20260605T012654254649+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/210199ea0250

## What looked useful

Mechanism confirmed with exact zero max-absolute moment drift after restore and nonzero weight updates, but final validation loss was 0.4638 nats worse than AdamW, far outside the 0.05-nat margin.

## Boundaries and scale limits

Small direct Tier 1 run only: 80 updates, two seeds, WikiText-2, short context, scratch initialization. Does not test long-run convergence, pretrained continuation, larger corpora, or alternative freeze schedules.

## Claim scope

On a two-seed, 80-step GPT-2-small-from-scratch WikiText-2 run with sequence length 64, batch size 2, learning rate 2e-4, and cycle length 8, cyclic AdamW moment freezing exactly preserved optimizer moments during freeze windows and still allowed weight updates, but failed the 0.05-nat validation-loss noninferiority threshold versus same-seed AdamW.

## Why it stopped

Direct small real-corpus GPT-2-small test confirmed the optimizer-state freeze mechanism but failed the predefined validation-loss threshold by a large margin, so this is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Stop this run as no-paper useful evidence; the tested cycle length 8 state-freeze schedule is directly falsified on the Tier 1 GPT-2-small/WikiText-2 threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small cyclic optimizer-state freeze schedule sweep on WikiText-2
- Success threshold: At least one cyclic-freeze schedule has mean final validation loss no more than 0.05 nats worse than AdamW across at least 3 seeds while exact moment drift remains 0.0 and weight updates remain nonzero.
- Stop condition: Stop if all tested schedules remain more than 0.10 nats worse than AdamW or if exact moment-freeze diagnostics fail.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-cyclic-optimizer-state-freeze-confirmation-for-22192fcae0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
