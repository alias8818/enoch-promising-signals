# Model-in-the-loop AnchorState memory persistence test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1`
Run ID: `model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1-20260520T133652820234+0000`

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

- Parent run decision: AnchorState: Agent-Controlled Memory Segmentation via Exact Tokens: enoch://control-plane/projects/anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a/runs/anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a-20260520T132708153822+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5f6da419786

## What looked useful

AnchorState persistence worked as a mechanism when paired with a capable 3B instruction model, but the 0.5B model showed that answer/retrieval behavior can dominate persistence despite correctly stored state.

## Boundaries and scale limits

Small synthetic workload only; file reload simulated the session boundary inside one script; deterministic key retrieval; two Qwen instruct models tested; no natural conversation, noisy retrieval, multi-session service restart, or broad model-family validation.

## Claim scope

In a 20-trial synthetic key/value memory task, Qwen/Qwen2.5-3B-Instruct successfully extracted facts into a JSON AnchorState, persisted them across a simulated hard session boundary, and recalled them with 95% full-store accuracy and 100% retrieved-slot accuracy versus 0% no-memory accuracy.

## Why it stopped

Tier 1 direct test completed with useful mechanism support, but evidence remains small, synthetic, and not publication-grade.

## Recommended next action

Run a bounded medium confirmation with at least 100 synthetic and naturalistic memory facts, separate writer/reader processes, multiple seeds, and retrieval-noise ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium AnchorState persistence under naturalistic distractors and separate-process reload
- Success threshold: >=90% exact retrieved-slot recall after separate-process reload, >=80% full-store or noisy-retrieval recall, and >=50 percentage-point gain over no-memory controls with extraction accuracy >=90%.
- Stop condition: Stop as unsupported if retrieved-slot recall is below 80% or the gain over no-memory is below 30 percentage points in two seeds for the strongest tested local model.

## Evidence references

- Artifact root: `<local-path>/projects/model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
