# Quality-aware GPT-2-small optimizer memory Pareto micro-pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-aware-gpt-2-small-optimizer-memory-pareto-micro-pr-547b5ceb38`
Run ID: `quality-aware-gpt-2-small-optimizer-memory-pareto-micro-pr-547b5ceb38-20260614T015121059212+0000`

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

- Parent run decision: Optimizer memory Pareto at GPT-2-small scale: enoch://control-plane/projects/optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5/runs/optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5-20260614T012457260393+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a89d19a40a

## What looked useful

Adafactor used 1.227 MiB optimizer state versus AdamW's 949.401 MiB and had mean final validation loss ratio 0.9973 versus AdamW; SGD momentum used 474.700 MiB state but failed quality with mean loss ratio 1.2834.

## Boundaries and scale limits

Only three short micro-pretraining seeds were run; this does not validate long-horizon GPT-2-small pretraining, larger corpora, schedule sensitivity, downstream quality, checkpoint/restart behavior, or robustness beyond Wikitext-2.

## Claim scope

In a controlled GPT-2-small architecture micro-pretraining test on Wikitext-2 for 30 steps and 7,680 tokens per seed, Adafactor achieved a much lower optimizer-state memory footprint than AdamW while matching AdamW validation loss within the predeclared 1% quality threshold across three seeds.

## Why it stopped

Tier 1 direct small test completed and supports the mechanism, but the evidence remains micro-scale and not paper-positive.

## Recommended next action

Run a bounded deepen follow-up for 100k-1M tokens with checkpointed validation curves and matched AdamW/Adafactor schedules before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer GPT-2-small Adafactor-vs-AdamW memory-quality curve
- Success threshold: Adafactor optimizer-state memory remains at least 50% below AdamW and final validation loss is no more than 1% worse than AdamW across the chosen longer-token budget.
- Stop condition: Stop if Adafactor is more than 1% worse than AdamW for two consecutive validation checkpoints after warmup, or if memory savings drop below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/quality-aware-gpt-2-small-optimizer-memory-pareto-micro-pr-547b5ceb38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
