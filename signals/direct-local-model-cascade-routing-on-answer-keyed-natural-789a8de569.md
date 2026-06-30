# Direct local-model cascade routing on answer-keyed natural-language tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-local-model-cascade-routing-on-answer-keyed-natural-789a8de569`
Run ID: `direct-local-model-cascade-routing-on-answer-keyed-natural-789a8de569-20260619T055658350358+0000`

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

- Parent run decision: CPU cascade router: difficulty-based dispatch across tiny/medium local models: enoch://control-plane/projects/cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526/runs/cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526-20260619T053942292708+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a9965c62ab63

## What looked useful

The answer-keyed cascade reached 0.9929 accuracy at 2.014 mean cost units, versus 0.9393 accuracy at 6.000 mean cost units for always-expensive generalist and 0.9393 accuracy at 5.275 mean cost units for a random-specialist cascade. Cheap-only reached 0.8571, showing fallback was necessary.

## Boundaries and scale limits

Small Tier 1 generated task suite; deterministic local answerer proxies rather than actual pretrained neural local models; modeled cost units rather than measured latency, tokens, energy, or GPU utilization; no broad held-out benchmark.

## Claim scope

In a 280-task controlled, template-generated, answer-keyed natural-language suite, a deterministic local cascade router preserved or improved accuracy while reducing modeled cost versus an always-expensive fallback control.

## Why it stopped

Tier 1 controlled direct test met its threshold, but evidence is not paper-ready because local model behavior and cost were modeled with deterministic proxies.

## Recommended next action

Run a bounded direct follow-up using actual local LLMs or small classifiers plus a larger local fallback on a held-out answer-keyed QA benchmark, with measured latency/token/memory cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual local-LLM cascade routing on held-out answer-keyed QA
- Success threshold: Cascade accuracy >= always-large accuracy - 0.02 and measured mean latency or token cost <= 70% of always-large, with accuracy above cheap-only and random-router controls.
- Stop condition: Stop as unsupported if the actual-model cascade misses the accuracy threshold by more than 2 percentage points or cost savings are below 30% after threshold calibration on a validation split.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-model-cascade-routing-on-answer-keyed-natural-789a8de569`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
