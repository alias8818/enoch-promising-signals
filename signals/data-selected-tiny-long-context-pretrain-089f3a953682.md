# Data-Selected Tiny Long Context Pretrain

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `data-selected-tiny-long-context-pretrain-089f3a953682`
Run ID: `data-selected-tiny-long-context-pretrain-089f3a953682-20260522T180006164179+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acbb5f2d3255

## What looked useful

The selected subset was strongly enriched for long-dependency examples, but six-seed aggregate accuracy was effectively tied with random: selected 0.5378 vs random 0.5423, mean delta -0.0046, with three selected wins and three random wins. Naive long-context enrichment alone is not a reliable improvement in this bounded setting.

## Boundaries and scale limits

Toy synthetic data, 256-token contexts, six seeds, CPU-only small transformer, short training horizon, no natural-language corpus, no GPT-2-class or larger baseline, and no diversity-constrained data selection control.

## Claim scope

In a synthetic 256-token associative-recall proxy with a 1-layer width-48 causal transformer trained for 90 steps per condition, naive selection for long dependency distance plus distractor count did not reliably improve held-out hard long-recall accuracy over random mixed-distance examples at equal token budget.

## Why it stopped

Proxy bounded confirmation produced a mixed/null result rather than a reliable selected-data advantage; this is an early falsification of naive long-dependency selection, not a full validation or full disproof at natural-language scale.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should control selection diversity and key/value coverage before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained Long-Dependency Data Selection
- Success threshold: Diversity-constrained long selection beats random by at least 5 absolute accuracy points on mean held-out hard long recall, with positive deltas in at least 8 of 10 seeds and no worse mean loss.
- Stop condition: Stop if the diversity-constrained selector fails to beat random by at least 2 absolute accuracy points after 10 seeds or if gains remain dominated by seed variance.

## Evidence references

- Artifact root: `<local-path>/projects/data-selected-tiny-long-context-pretrain-089f3a953682`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
