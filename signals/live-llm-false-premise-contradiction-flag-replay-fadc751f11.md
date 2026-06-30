# Live LLM false-premise contradiction flag replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-llm-false-premise-contradiction-flag-replay-fadc751f11`
Run ID: `live-llm-false-premise-contradiction-flag-replay-fadc751f11-20260630T043042208777+0000`

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

- Parent run decision: Live-agent false-premise contradiction flag benchmark: enoch://control-plane/projects/live-agent-false-premise-contradiction-flag-benchmark-96cd1fead3/runs/live-agent-false-premise-contradiction-flag-benchmark-96cd1fead3-20260630T035012509938+0000
- Parent run decision: False-Premise Injection Harness: Contradiction-Flag Rate by Agent Class: enoch://control-plane/projects/false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8/runs/false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8-20260630T032951993256+0000

## What looked useful

Contradiction-flag replay improved recall over exact transcript search from 0.3333 to 0.6667 with no false positives, but recall on novel false premises was 0.0. Direct fact comparison reached 1.0 recall in the closed suite, indicating replay alone is insufficient for broad contradiction handling.

## Boundaries and scale limits

Synthetic data only; no live LLM call; no unannotated natural-language extraction; closed-world fact comparison uses task metadata and should be treated as an upper-bound guardrail proxy.

## Claim scope

In a 32-task synthetic annotated replay suite, replayed contradiction flags detect exact and paraphrased repeats of previously seen false premises but miss novel false values for the same stored facts.

## Why it stopped

Bounded synthetic proxy result, not full live LLM validation; replay-only memory failed the novel-false split, so the tested idea is insufficient as a standalone contradiction detector.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should test the same split design with model-generated premise extraction and contradiction flags from raw prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-generated false-premise flag replay with raw-prompt extraction
- Success threshold: At least 0.85 recall on novel false premises and at least 0.95 precision on clean and benign-update prompts, with saved model transcripts and machine-readable metrics.
- Stop condition: Stop if model premise extraction cannot exceed 0.70 F1 on a 20-prompt smoke set or if replay-plus-fact comparison produces more than 5% false positives on clean prompts.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-false-premise-contradiction-flag-replay-fadc751f11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
