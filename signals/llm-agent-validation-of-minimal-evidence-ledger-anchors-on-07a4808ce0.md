# LLM agent validation of minimal evidence-ledger anchors on episodic QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0`
Run ID: `llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0-20260526T142001330647+0000`

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

- Parent run decision: Evidence-Ledger Agent with Compressed Episodic Anchors: enoch://control-plane/projects/evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba/runs/evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba-20260526T063251094295+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2df4cd4f2a67

## What looked useful

Across 144 questions per condition, minimal ledger exact match averaged 0.979 versus 0.410 for full history and 0.778 for noisy ledger; citation faithfulness averaged 0.979 versus 0.396 and 0.785 respectively. All 3 runs passed the preregistered Tier 1 mechanism threshold.

## Boundaries and scale limits

Three deterministic 48-item synthetic runs only; extractive QA rather than a full autonomous generative LLM agent; oracle-aligned ledger construction; no human-authored episodic benchmark or independent natural-language citation judge.

## Claim scope

In a small synthetic episodic QA benchmark using an extractive QA model, deterministic minimal evidence-ledger anchors improved exact-match answer accuracy and citation faithfulness over full-history and noisy-ledger context controls.

## Why it stopped

Tier 1 mechanism support was obtained, but it remains no-paper useful evidence because the run used synthetic generated episodes, an extractive QA model, and deterministic oracle-aligned ledger anchors rather than a full online LLM-agent validation.

## Recommended next action

Run a bounded deepen follow-up with a local generative LLM agent that must build the ledger online, answer held-out episodic questions, and emit cited anchors under full-history, minimal-ledger, and noisy-ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online generative LLM-agent validation of minimal evidence-ledger anchors on episodic QA
- Success threshold: Minimal-ledger agent improves answer correctness by at least 15 percentage points over full-history and noisy-ledger controls while maintaining citation faithfulness at or above 90%.
- Stop condition: Stop as no-paper negative if minimal ledger fails to beat either control by 10 percentage points or citation faithfulness drops below 85% on the first 75 held-out questions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
