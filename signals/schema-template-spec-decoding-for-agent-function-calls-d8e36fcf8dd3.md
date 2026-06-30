# Schema-Template Spec Decoding for Agent Function Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `schema-template-spec-decoding-for-agent-function-calls-d8e36fcf8dd3`
Run ID: `schema-template-spec-decoding-for-agent-function-calls-d8e36fcf8dd3-20260628T094718679577+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e49079f54af2

## What looked useful

Post-hoc repair recovered JSON parseability but still left missing/extra argument keys, wrong argument shapes, and type/enum/range violations; schema-template decoding removed those failure classes and improved exact match in every tested noise condition.

## Boundaries and scale limits

No real LLM logits, natural-language prompt understanding, public function-calling dataset, or production agent traces were evaluated. The 100% schema-validity result is expected from the constrained renderer by design.

## Claim scope

In a local synthetic decoder-layer benchmark with six tool schemas and controlled structural/semantic noise, schema-template rendering eliminated JSON/schema validity failures and improved exact-match rate versus raw free-form JSON and a simple schema-aware repair baseline.

## Why it stopped

Useful bounded synthetic evidence was produced, but it is proxy evidence rather than publication-grade validation for real agent function calls.

## Recommended next action

Run a bounded direct LLM evaluation using sampled completions or logits from a small open instruct model on held-out natural-language tool-use prompts, comparing free-form, repair, and schema-template decoding with the same schema-validity and exact-match metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Schema-Template Decoding Evaluation for Function Calls
- Success threshold: Schema-template decoding improves schema-validity by at least 5 percentage points over repair while exact-match accuracy is no worse than 1 percentage point below repair on at least 500 held-out prompts.
- Stop condition: Stop if schema-template exact match is more than 3 percentage points worse than repair or if the validity gain over repair is below 2 percentage points after 500 prompts.

## Evidence references

- Artifact root: `<local-path>/projects/schema-template-spec-decoding-for-agent-function-calls-d8e36fcf8dd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
