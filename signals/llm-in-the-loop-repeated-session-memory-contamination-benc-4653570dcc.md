# LLM-in-the-loop repeated-session memory contamination benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-in-the-loop-repeated-session-memory-contamination-benc-4653570dcc`
Run ID: `llm-in-the-loop-repeated-session-memory-contamination-benc-4653570dcc-20260613T041402693653+0000`

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

- Parent run decision: Layered Agent Memory vs Flat Retrieval on Repeated Multi-Task Sessions: enoch://control-plane/projects/layered-agent-memory-vs-flat-retrieval-on-repeated-multi-task-sessions-bedb16324457/runs/layered-agent-memory-vs-flat-retrieval-on-repeated-multi-task-sessions-bedb16324457-20260613T025230229833+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Qwen2.5-1.5B rose from 4.2% stateless poison choices to 41.7% with shared poisoned memory, but unrelated memory also produced 16.7% poison choices, so the strict 30 percentage point shared-vs-isolated threshold was missed. Qwen2.5-0.5B was too noisy, with 25.0% stateless poison choices.

## Boundaries and scale limits

24 synthetic items, one seed, two local Qwen2.5 instruct model sizes, log-likelihood multiple-choice scoring only; no production memory retrieval, real user histories, free-form parsing, or broad multi-model validation.

## Claim scope

Controlled local benchmark runs on cached Qwen2.5-0.5B-Instruct and Qwen2.5-1.5B-Instruct show that shared poisoned durable-memory text can increase poisoned answer choices versus stateless prompts, but the configured benchmark does not cleanly isolate target-specific contamination from generic unrelated-memory degradation.

## Why it stopped

Tier 1 direct tests produced useful mechanism evidence but did not meet the preregistered success threshold, so this is a no-paper result rather than a positive close.

## Recommended next action

Run a balanced multi-seed benchmark with answer-order randomization and length-matched unrelated-memory controls to separate target-specific contamination from generic context-load degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Balanced multi-seed memory contamination control benchmark
- Success threshold: Aggregate stateless accuracy >= 80%, shared poisoned-memory poison-choice rate at least 30 percentage points above stateless and isolated controls, and the shared-vs-isolated delta positive in every seed.
- Stop condition: Stop as negative if isolated-memory poison-choice rate remains within 20 percentage points of shared poisoned-memory rate or stateless accuracy falls below 80% after prompt/order balancing.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-repeated-session-memory-contamination-benc-4653570dcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
