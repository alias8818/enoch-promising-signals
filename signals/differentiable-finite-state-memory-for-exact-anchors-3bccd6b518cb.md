# Differentiable Finite-State Memory for Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb`
Run ID: `differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb-20260519T225409227894+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cd36c05e0d83

## What looked useful

The explicit FSM memory is a viable exact-anchor mechanism and a useful inductive-bias probe: it solved all smoke and medium evaluations at 100% accuracy with zero trainable parameters. The stronger claim that exact anchors require this architecture is mixed because a small GRU learned the same task after longer training; the compact Transformer remained weak.

## Boundaries and scale limits

Single synthetic generator, one main seed, fixed anchor pattern, compact baselines only, no natural language corpus, no GPT-2-scale baseline, no learned FSM-transition module, and no broad hyperparameter search. The 2000-step GRU baseline also solved the tested task, limiting novelty claims.

## Claim scope

On a synthetic fixed-token exact-anchor retrieval task with near-miss distractors, an explicit finite-state anchor memory retrieves the payload perfectly without training and remains length-stable over tested lengths 48 to 384. This does not establish a paper-ready language-model architecture claim.

## Why it stopped

Bounded synthetic evidence supports the mechanism but not a publication-grade or broad novelty claim; the 2000-step GRU control solved the task, so this is not a decisive positive result.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded follow-up that integrates a trainable FSM anchor-memory module into a sequence model and compares sample efficiency and length extrapolation against parameter-matched GRU/Transformer baselines across multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trainable FSM Anchor Memory Versus Parameter-Matched Sequence Models
- Success threshold: FSM-augmented model reaches at least 95% extrapolation accuracy with at least 3x fewer training examples than both tuned baselines, and the exact-transition ablation loses at least 20 percentage points under high distractor pressure.
- Stop condition: Stop if tuned baselines match FSM-augmented sample efficiency and extrapolation within 5 percentage points across seeds, or if the exact-transition ablation performs indistinguishably from the full module.

## Evidence references

- Artifact root: `<local-path>/projects/differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
