# Compressed State Agent Loop

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-agent-loop-c4460d322c81`
Run ID: `compressed-state-agent-loop-c4460d322c81-20260522T110004330872+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e0acb91f60c2

## What looked useful

Compressed state can preserve most query-relevant facts at a small token fraction when the state schema is explicit and enough per-slot history is retained; too-shallow state histories fail history-sensitive queries.

## Boundaries and scale limits

Synthetic traces only; no LLM-in-the-loop extraction, no natural-language ambiguity, no real autonomous agent tasks, and no full-scale model or serving validation.

## Claim scope

On deterministic synthetic agent-loop traces with structured state updates, a slot-indexed compressed state retaining eight values per slot achieved 0.9603 mean QA accuracy at 0.08 of full-history tokens and substantially outperformed naive last-window truncation.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but does not validate a real compressed-state agent loop or justify paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded LLM-in-the-loop deepen test where observations are natural language and the model must write and consume the compressed state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop compressed state on natural-language agent traces
- Success threshold: Mean QA accuracy >= 0.85, compressed-state memory <= 0.25 of full-history tokens, and >= 0.25 absolute accuracy improvement over last-window truncation.
- Stop condition: Stop if compressed-state accuracy is below 0.70 or fails to beat last-window truncation by at least 0.10 absolute accuracy after 30 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-agent-loop-c4460d322c81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
