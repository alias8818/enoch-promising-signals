# LLM Trace Validation for Evidence-Ledger Tool Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-trace-validation-for-evidence-ledger-tool-use-8667dd2830`
Run ID: `llm-trace-validation-for-evidence-ledger-tool-use-8667dd2830-20260526T170241227020+0000`

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

- Parent run decision: Tool-Use Evidence Ledger for Small Agents: enoch://control-plane/projects/tool-use-evidence-ledger-for-small-agents-b86bd3f70daa/runs/tool-use-evidence-ledger-for-small-agents-b86bd3f70daa-20260525T213451140058+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e860e91d93dc

## What looked useful

Evidence-ledger validation improved invalid-trace detection from 0/400 for a transcript-only baseline to 350/400 while accepting all 200 valid traces; all 50 misses were semantic negations with the same evidence terms.

## Boundaries and scale limits

Toy fact database, generated traces, deterministic structural validator, simple single-hop JSON tool results, no live LLM traces, no human-labeled entailment dataset, and no messy multi-tool production traces.

## Claim scope

In a controlled synthetic suite of 600 LLM-style tool-use traces, deterministic evidence-ledger validation caught structural provenance and binding failures that a transcript-only baseline accepted, but it did not catch semantic negation that preserved the same bound terms.

## Why it stopped

Tier 1 direct controlled test produced useful mechanism support and a clear semantic blind spot, but the evidence is synthetic and not paper-positive for a broad LLM trace validation claim.

## Recommended next action

Run a bounded deepen test that adds an entailment-aware claim verifier after structural ledger checks and evaluates semantic negation plus valid paraphrase controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entailment-aware validation for evidence-ledger claim bindings
- Success threshold: Detect at least 90% of semantic contradiction corruptions while keeping valid paraphrase false rejects at or below 5% on the controlled suite.
- Stop condition: Stop if entailment validation cannot exceed the structural-only detector on semantic contradictions without introducing more than 10% false rejects on valid paraphrases.

## Evidence references

- Artifact root: `<local-path>/projects/llm-trace-validation-for-evidence-ledger-tool-use-8667dd2830`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
