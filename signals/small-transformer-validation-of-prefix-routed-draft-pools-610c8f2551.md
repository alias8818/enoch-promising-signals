# Small-transformer validation of prefix-routed draft pools

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-validation-of-prefix-routed-draft-pools-610c8f2551`
Run ID: `small-transformer-validation-of-prefix-routed-draft-pools-610c8f2551-20260526T153111190960+0000`

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

- Parent run decision: Prefix-Routed Speculative Draft Pool: enoch://control-plane/projects/prefix-routed-speculative-draft-pool-189110d68cb5/runs/prefix-routed-speculative-draft-pool-189110d68cb5-20260526T080421061136+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Across three seeds, prefix-routed draft acceptance averaged 0.3012 versus 0.2209 for the global draft and 0.2096 for random routing, a mean +36.4% relative gain over global. Target-to-draft KL also fell from 2.271 to 1.395.

## Boundaries and scale limits

Synthetic route-separable Markov language only; routed pool uses four draft experts and therefore more total draft parameters and aggregate draft training compute than the single global draft; no natural-language, GPT-2-small-class, parameter-matched, or serving-latency validation was run.

## Claim scope

In a controlled synthetic four-prefix sequence task with trained small causal transformers, correct prefix routing among draft experts increased expected speculative-decoding acceptance against a trained target transformer versus a single same-size global draft and a random-routing control.

## Why it stopped

Tier 1 controlled direct test completed and produced useful no-paper mechanism evidence; publication readiness is blocked by synthetic data and parameter/compute confounds, not by execution failure.

## Recommended next action

Run a bounded parameter/compute-matched follow-up comparing the routed pool against a larger global draft with the same total draft parameters and against an equal-total-training-token global baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched control for prefix-routed draft pools
- Success threshold: Correct prefix-routed pool expected acceptance must exceed both a total-parameter-matched global draft and an equal-training-compute global draft by at least 10% relative across the mean of three seeds, while random routing remains below the correctly routed pool.
- Stop condition: Stop as unsupported for this mechanism if either matched global control closes the acceptance gap to within 10% relative or if random routing matches correct routing.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-prefix-routed-draft-pools-610c8f2551`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
