# Complexity-Aware Local Cascade Router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `complexity-aware-local-cascade-router-f629c4be0ab9`
Run ID: `complexity-aware-local-cascade-router-f629c4be0ab9-20260629T054151954854+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/95600b59db12

## What looked useful

Complexity routing achieved 0.9599 mean accuracy at 5.6845 mean cost, reducing assigned cost 28.94% versus all-strong and improving accuracy 43.06 percentage points versus all-small. A confidence router also met the target at lower mean cost, so novelty over simple confidence routing is not established.

## Boundaries and scale limits

No real LLMs, real prompts, measured serving latency, or model confidence/logprob calibration were tested. The main run was 24 seeds of 12000 synthetic examples per seed and completed in 14.58 seconds on one CPU.

## Claim scope

On a deterministic synthetic proxy with arithmetic, sorting, and majority-vote tasks, a thresholded complexity router can meet a 95% accuracy target while reducing assigned cost versus an all-strong cascade.

## Why it stopped

Proxy-only evidence supports the mechanism but not a paper claim, and the confidence baseline is cheaper at similar accuracy.

## Recommended next action

Stop this run as a proxy useful-signal result; next run should test two real local models on a small benchmark and require complexity routing to dominate confidence routing at fixed accuracy retention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-model benchmark for complexity versus confidence cascade routing
- Success threshold: Complexity router keeps at least 95% of all-strong accuracy, reduces measured cost or latency by at least 20%, and has lower cost at equal-or-better accuracy than the confidence router.
- Stop condition: Stop if complexity routing fails to meet 95% all-strong accuracy retention or does not dominate confidence routing on cost at matched accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/complexity-aware-local-cascade-router-f629c4be0ab9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
