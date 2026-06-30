# Long-range dependency density improves tiny model long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-range-dependency-density-improves-tiny-model-long-context-35e773825b0c`
Run ID: `long-range-dependency-density-improves-tiny-model-long-context-35e773825b0c-20260521T203555331708+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/230fe5f044c9

## What looked useful

Long-range dependency density showed a threshold-like effect: density 0.50 reached 0.969 mean copy accuracy at length 128 versus about 0.016 for density 0.05, but length-256 accuracy for the high-density model was only about 0.334, so density helped the mechanism but did not validate broad long-context generalization.

## Boundaries and scale limits

Synthetic task only; three seeds; sequence length 128 training with 256 evaluation; no natural-language corpus, no GPT-2-small-class baseline, no larger-context training, and incomplete extrapolation beyond the trained context length.

## Claim scope

In a synthetic 64-lag copy task with a two-layer 64-wide causal transformer trained for 5,000 steps, high dependency density (0.50) produced near-perfect trained-length copy accuracy while low and medium densities (0.05, 0.20) stayed near chance under the same budget.

## Why it stopped

No-paper useful signal: the local synthetic evidence supports a density threshold for learning the lag relation but is mixed for long-context extrapolation and is not publication-grade evidence for the broad claim.

## Recommended next action

Run a bounded deepen follow-up with marked/unmarked dependencies, multiple lags, and train/eval lengths that separate memorized position behavior from true length extrapolation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Density threshold and extrapolation diagnostics for synthetic long-lag copy
- Success threshold: High-density conditions should exceed low-density conditions by at least 0.25 absolute copy accuracy on longer-than-trained contexts while maintaining near-perfect trained-length accuracy across seeds.
- Stop condition: Stop if all densities remain at chance after a positive-control marked-copy condition learns, or if longer-context accuracy remains below 0.10 absolute above chance despite trained-length accuracy above 0.90.

## Evidence references

- Artifact root: `<local-path>/projects/long-range-dependency-density-improves-tiny-model-long-context-35e773825b0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
