# Medium AnchorState persistence under naturalistic distractors and separate-process reload

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7`
Run ID: `medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7-20260520T134703470696+0000`

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

- Parent run decision: Model-in-the-loop AnchorState memory persistence test: enoch://control-plane/projects/model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1/runs/model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1-20260520T133652820234+0000
- Parent run decision: AnchorState: Agent-Controlled Memory Segmentation via Exact Tokens: enoch://control-plane/projects/anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a/runs/anchorstate-agent-controlled-memory-segmentation-via-exact-tokens-c35c2638701a-20260520T132708153822+0000

## What looked useful

Medium confirmation supports the persistence mechanism: extraction and JSON reload were exact, separate-process reader recall was high, and controls did not recover target codes.

## Boundaries and scale limits

Single local model family and size; template-generated naturalistic chats rather than real transcripts; deterministic known-label retrieval; JSON file store rather than production service/database; no multi-model, noisy-retrieval, or long-running multi-session validation.

## Claim scope

For Qwen/Qwen2.5-3B-Instruct on 120 fixed-seed template-naturalistic memory episodes, model-extracted AnchorState JSON persisted across separate writer and reader Python processes and enabled 0.958 exact full-store recall under distractors versus 0.000 no-memory, missing-state, and corrupt-state controls.

## Why it stopped

Tier 2 local mechanism threshold was met, but evidence remains too narrow for paper readiness.

## Recommended next action

Run a bounded deepen test with at least two additional instruction model families and semi-real conversation traces, preserving the same no-memory/missing/corrupt controls and separate-process reload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model semi-real AnchorState reload validation
- Success threshold: For each primary model, model-extracted full-store recall >=0.80, gain over no-memory >=30 percentage points, extraction exact-code rate >=0.80, and no-memory/missing/corrupt controls <0.10.
- Stop condition: Stop if any added primary model falls below 0.60 full-store recall with exact persisted state, or if controls exceed 0.10 exact recall, because that would show the effect is model/prompt fragile or benchmark-leaky.

## Evidence references

- Artifact root: `<local-path>/projects/medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
