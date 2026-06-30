# Replay Real Repeated Agent Tasks with Actual Layered Memory Extraction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-real-repeated-agent-tasks-with-actual-layered-memor-cbd3b5d944`
Run ID: `replay-real-repeated-agent-tasks-with-actual-layered-memor-cbd3b5d944-20260628T071806482537+0000`

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

- Parent run decision: Layered Memory vs Full-Transcript Search on Repeated Agent Tasks: enoch://control-plane/projects/layered-memory-vs-full-transcript-search-on-repeated-agent-tasks-301ea02c838e/runs/layered-memory-vs-full-transcript-search-on-repeated-agent-tasks-301ea02c838e-20260628T064639174289+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

Compact layered memory preserved 25/25 required facts at 224 words and 11.63x compression, compared with 6/25 for same-budget head truncation and 8/25 for repeated-line memory.

## Boundaries and scale limits

Single project, two prompt files, deterministic constraint evaluator, no LLM replay behavior test, no cross-project robustness, no noisy or adversarial memory extraction.

## Claim scope

In one real repeated Enoch agent-task pair from this project, deterministic layered memory extraction compressed 2606 words of repeated prompts into a 224-word replay memory while preserving all 25 controller-critical constraints used by the evaluator.

## Why it stopped

Tier 1 direct small test produced a useful mechanism signal, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on at least 20 real repeated agent-task pairs with LLM replay validation and stronger summarization baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-Project LLM Replay Validation for Layered Agent-Task Memory
- Success threshold: Layered memory must reach at least 90% constraint coverage, at least 95% valid decision-artifact production in LLM replay, at least 5x word compression, and at least a 20 percentage point artifact-validity advantage over same-budget naive baselines.
- Stop condition: Stop as unsupported if layered memory falls below 80% constraint coverage or fails to beat same-budget naive baselines by at least 10 percentage points on artifact validity.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-repeated-agent-tasks-with-actual-layered-memor-cbd3b5d944`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
