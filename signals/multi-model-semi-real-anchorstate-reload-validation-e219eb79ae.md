# Multi-model semi-real AnchorState reload validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `multi-model-semi-real-anchorstate-reload-validation-e219eb79ae`
Run ID: `multi-model-semi-real-anchorstate-reload-validation-e219eb79ae-20260520T140134124892+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Model-in-the-loop AnchorState memory persistence test: enoch://control-plane/projects/model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1/runs/model-in-the-loop-anchorstate-memory-persistence-test-6d651568a1-20260520T133652820234+0000
- Parent run decision: Medium AnchorState persistence under naturalistic distractors and separate-process reload: enoch://control-plane/projects/medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7/runs/medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7-20260520T134703470696+0000

## What looked useful

Extraction into durable JSON was exact for all four final models and no-memory/missing/corrupt controls stayed at 0.0, but full-store recall failed the multi-model threshold for Qwen2.5-1.5B, SmolLM2-1.7B, and LiquidAI-1.2B. Exact-entry retrieval appears robust; prompt-only selection from a reloaded shard is the limiting mechanism.

## Boundaries and scale limits

Semi-real generated transcripts only; JSON file store rather than production database; deterministic label retrieval; 15-entry shards; four local cached models; no real private user logs or long-horizon multi-session service.

## Claim scope

Bounded local validation on 180 semi-real AnchorState episodes across four cached instruction models shows correct JSON persistence and high retrieved-slot recall after separate-process reload, but full-store 15-entry shard recall is reliable only for Qwen2.5-3B in this setup.

## Why it stopped

Predeclared Tier 3 multi-model full-store threshold failed: only Qwen2.5-3B reached >=0.80 full-store recall, while the other final models ranged from 0.556 to 0.622 despite exact persisted state.

## Recommended next action

Stop paper escalation; if continuing this line, run a bounded shard-size/top-k retrieval ablation on the same four models to test whether exact-entry retrieval preserves recall while avoiding full-shard selection failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shard-size and top-k retrieval ablation for multi-model AnchorState reload
- Success threshold: For every final model, top-k retrieval with k <= 5 achieves >=0.90 exact recall, >=30 percentage-point gain over no-memory, and missing/corrupt controls remain below 0.20.
- Stop condition: Stop if any two non-Qwen models remain below 0.80 exact recall even with exact-entry or top-3 retrieved AnchorState, because the issue is then not just shard size.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-semi-real-anchorstate-reload-validation-e219eb79ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
