# CPU LLM cascade router with real small and larger local models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-llm-cascade-router-with-real-small-and-larger-local-mo-4e03f0f7cb`
Run ID: `cpu-llm-cascade-router-with-real-small-and-larger-local-mo-4e03f0f7cb-20260621T085509236310+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Cascade Router: Easy->Small, Hard->Big on CPU: enoch://control-plane/projects/cascade-router-easy-small-hard-big-on-cpu-b219ed55e032/runs/cascade-router-easy-small-hard-big-on-cpu-b219ed55e032-20260621T083932857445+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92728ff62b1b

## What looked useful

The naive confidence-margin cascade failed the direct Tier 1 threshold. Pythia 70M was slower and less accurate than Pythia 14M. Qwen2.5 0.5B was more accurate than SmolLM2 135M, but no tested margin threshold matched Qwen accuracy with lower estimated scoring time.

## Boundaries and scale limits

Only 80 examples for the Pythia 14M/70M pair and 32 examples for the SmolLM2 135M/Qwen2.5 0.5B pair; thresholds were evaluated on the same examples; no batching, quantization, generation, serving concurrency, trained router, or cross-task robustness was tested.

## Claim scope

On HellaSwag multiple-choice CPU scoring with two local model pairs, a simple small-model top-margin threshold cascade did not match larger-model accuracy while reducing estimated scoring time.

## Why it stopped

Direct Tier 1 early falsification of the naive margin-router success threshold; not a full validation of all cascade routing methods.

## Recommended next action

Run one bounded deepen follow-up with a calibrated held-out router for the SmolLM2 135M to Qwen2.5 0.5B pair; stop if it cannot match Qwen accuracy within 1 percentage point while routing fewer than 60 percent of examples to Qwen.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out calibrated router for CPU SmolLM2-to-Qwen cascade
- Success threshold: Evaluation accuracy within 1 percentage point of Qwen2.5 0.5B large-only accuracy with fewer than 60 percent large-model calls and lower measured estimated scoring time than large-only.
- Stop condition: Stop as negative if held-out calibration cannot reach the success threshold or if the evaluation would exceed the local CPU-only budget without producing intermediate metrics.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-llm-cascade-router-with-real-small-and-larger-local-mo-4e03f0f7cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
