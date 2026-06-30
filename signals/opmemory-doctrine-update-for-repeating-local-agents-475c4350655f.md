# OpMemory: Doctrine Update for Repeating Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `opmemory-doctrine-update-for-repeating-local-agents-475c4350655f`
Run ID: `opmemory-doctrine-update-for-repeating-local-agents-475c4350655f-20260630T052839001761+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6ddb85ba8b

## What looked useful

Blind persistent memory was cheapest but produced stale-action failures under drift and unbounded memory growth. Strict doctrine memory cut stateless discovery cost by 55.4-72.0% across tested drift rates, kept stale-action failure at 0%, and bounded memory growth. TTL/high-risk-only validation reduced but did not eliminate stale failures.

## Boundaries and scale limits

No live LLM, no real repository edits, and no full local-agent task harness were run. The result supports a doctrine mechanism, not a real-agent performance claim or paper-ready validation.

## Claim scope

In a deterministic proxy benchmark for repeating local agents, project-scoped operational memory with evidence, validation-before-use, and compaction reduced repeated discovery cost while avoiding stale-action failures under controlled project-rule drift.

## Why it stopped

Closed as no-paper useful signal because evidence is simulator/proxy evidence rather than direct LLM-agent validation.

## Recommended next action

Run a bounded real-agent deepen test on 3-5 small repositories with seeded command/rule drift, comparing no memory, blind memory, TTL/high-risk-only memory, and validation-before-use memory on task success, wall-clock, command count, and stale-memory incidents.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent validation of validation-before-use operational memory
- Success threshold: Validation-before-use memory reduces median command/search count by at least 25% versus stateless discovery, keeps task success within 1 percentage point of stateless, and cuts stale-memory incidents by at least 80% versus blind memory.
- Stop condition: Stop if validation-before-use memory fails to reduce command/search count by 10% versus stateless or causes more than a 1 percentage point task-success drop on two or more repositories.

## Evidence references

- Artifact root: `<local-path>/projects/opmemory-doctrine-update-for-repeating-local-agents-475c4350655f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
