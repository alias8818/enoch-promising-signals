# CPU-Optimized TinyStories Curriculum Learning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-optimized-tinystories-curriculum-learning-8f8bc03feed6`
Run ID: `cpu-optimized-tinystories-curriculum-learning-8f8bc03feed6-20260523T073657088902+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c3a1e9f2dce

## What looked useful

Random ordering reached final validation NLL 0.5679, while easy-to-hard reached 1.9109 and length-bucket shuffle reached 1.9169. Easy-to-hard was faster (15049.8 vs 13126.5 updates/sec) but never reached level-2 examples by 120k updates, so throughput gains did not translate into sample-efficient learning.

## Boundaries and scale limits

This did not use the real TinyStories dataset, a Transformer/GPT model, BPE tokenization, or multi-epoch coverage-aware scheduling. It is an early proxy falsification of naive sorted curriculum under a 120k-update CPU budget, not a full curriculum-learning validation.

## Claim scope

In a deterministic synthetic TinyStories-style character-level proxy, naive easy-to-hard or length-bucket sorted curriculum improves CPU update throughput but substantially worsens fixed-budget mixed-validation NLL versus shuffled training because hard examples are delayed beyond the early budget.

## Why it stopped

Proxy early falsification: naive easy-to-hard CPU curriculum failed the predefined useful-signal threshold by producing much worse final validation NLL than random despite higher throughput.

## Recommended next action

Stop this no-paper run; the next bounded test should replace naive sorting with a coverage-aware staged curriculum on a small real TinyStories slice and require all difficulty levels to appear before each checkpoint.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-aware TinyStories curriculum on a real small slice
- Success threshold: Coverage-aware staged curriculum must reduce validation NLL per CPU-hour by at least 5% versus shuffled training at the same update count without delaying any difficulty level past the first checkpoint.
- Stop condition: Stop if staged curriculum either regresses final validation NLL by more than 2% versus random or fails to show a throughput-adjusted improvement by the midpoint checkpoint across at least 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-optimized-tinystories-curriculum-learning-8f8bc03feed6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
