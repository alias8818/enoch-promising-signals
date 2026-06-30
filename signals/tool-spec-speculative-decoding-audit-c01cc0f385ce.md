# Tool-Spec Speculative Decoding Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tool-spec-speculative-decoding-audit-c01cc0f385ce`
Run ID: `tool-spec-speculative-decoding-audit-c01cc0f385ce-20260619T022657681349+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/18122a9b386e

## What looked useful

Canonical schema drafts accepted nearly all target tokens under strict normalized serialization, but accepted-prefix coverage fell to 0.477 under format drift and 0.306 under high drift, with only 15.1% of high-drift calls accepting at least half the target. Schema-aware speedup therefore appears conditional on strong output normalization or constrained serialization.

## Boundaries and scale limits

CPU-only proxy over 6000 synthetic traces total. The result cannot validate or refute full ToolSpec benchmark speedups, GPU verification behavior, or real BFCL/ToolBench/API-Bank distributions.

## Claim scope

Synthetic JSON lexical-token audit of schema-aware tool-call speculative drafting under controlled serialization drift; no real target model, model tokenizer, or serving system was measured.

## Why it stopped

Early proxy audit, not full validation: the local synthetic test supports a practical fragility mechanism but lacks direct LLM verification and end-to-end serving latency evidence.

## Recommended next action

Stop this run as a no-paper proxy result; a bounded follow-up should replay the same acceptance audit on real tool-call traces with model tokenizer boundaries and target-model verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace ToolSpec Acceptance Audit
- Success threshold: At least 500 real tool calls per dataset split, with raw-vs-canonical accepted-token differences of 20% or more, plus reproducible scripts and logs.
- Stop condition: Stop if real traces are unavailable, if model/tokenizer licensing prevents local replay, or if raw and canonicalized accepted-prefix distributions differ by less than 5% across 500+ calls.

## Evidence references

- Artifact root: `<local-path>/projects/tool-spec-speculative-decoding-audit-c01cc0f385ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
