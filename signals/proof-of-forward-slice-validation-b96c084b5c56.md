# Proof-of-Forward Slice Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proof-of-forward-slice-validation-b96c084b5c56`
Run ID: `proof-of-forward-slice-validation-b96c084b5c56-20260530T052251588594+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12c22dd7eb68

## What looked useful

Forward-slice validation must include control dependencies. A data-only proof failed on 400 of 15,000 branched seed validations and on a minimal handcrafted counterexample; adding branch predicate to assigned-variable control edges produced zero violations in the bounded toy suite.

## Boundaries and scale limits

Synthetic scalar language only; no loops, heap, aliasing, exceptions, calls, interprocedural dependencies, real parser/CFG, or unbounded-domain proof. The run used 5,000 random programs per random suite and exhaustive perturbations over domain {0,1,2}.

## Claim scope

Bounded toy-language validation: for straight-line programs, data-only forward slicing preserved the outside-slice invariance property; for branched programs, data-only slicing was falsified, while a control-aware slice preserved the invariant across 5,000 generated branched programs plus one handcrafted counterexample over a finite domain.

## Why it stopped

Proxy/toy validation only: it falsifies naive data-only slicing and supports a control-aware mechanism locally, but it is not full validation for real programs or an unbounded formal proof.

## Recommended next action

Stop this run as no-paper useful signal; next, implement the same invariant check for a real-language CFG subset with loops/calls bounded by an interpreter or solver.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-CFG Forward Slice Invariance Validation
- Success threshold: Zero outside-slice invariance violations for the control-aware slice on the bounded real-language suite, with at least five minimized counterexamples for data-only slicing.
- Stop condition: Stop if the control-aware slice has any confirmed outside-slice violation after dependency extraction bugs are ruled out, or if no real-language bounded execution/solver harness can be made reproducible locally.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-forward-slice-validation-b96c084b5c56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
