# Optimizer memory Pareto at GPT-2-small scale

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5`
Run ID: `optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5-20260614T012457260393+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a89d19a40a

## What looked useful

Optimizer state memory is directly measurable and large enough at GPT-2-small scale to change total CUDA peak allocation; Adafactor is the strongest memory point in this bounded test, while Lion/SGD+momentum are lower-memory and faster than AdamW in synthetic step timing. This supports a deeper quality-aware Pareto test but not a paper claim.

## Boundaries and scale limits

No real corpus, no validation perplexity, no learning-rate sweep, no mixed precision, no activation checkpointing, no sharding/distributed optimizer, and only one short synthetic run at batch 1 sequence 128.

## Claim scope

On a single GB10 using fp32 GPT-2-small-class synthetic causal-LM steps, optimizer state choice changes memory materially: Adafactor used 1.29 MB optimizer state and 54.4% of AdamW CUDA peak allocation, while Lion/SGD+momentum used one parameter-sized state tensor and lower CUDA peak than AdamW.

## Why it stopped

Closed as no-paper useful signal: direct memory/time evidence exists, but the result is synthetic/proxy-only for training quality and cannot validate an optimizer-memory Pareto frontier for real GPT-2-small training.

## Recommended next action

Run a bounded real-corpus GPT-2-small micro-pretraining comparison with optimizer-specific learning-rate sweeps and validation perplexity under the same memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-aware GPT-2-small optimizer memory Pareto micro-pretraining
- Success threshold: At least one non-AdamW optimizer achieves validation perplexity within 5% relative of the best AdamW run at equal tokens while reducing CUDA peak allocation by at least 25%.
- Stop condition: Stop if all lower-memory optimizers are more than 10% worse in validation perplexity after learning-rate sweep, or if the run cannot complete a fixed equal-token budget within local GB10 resource limits.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
