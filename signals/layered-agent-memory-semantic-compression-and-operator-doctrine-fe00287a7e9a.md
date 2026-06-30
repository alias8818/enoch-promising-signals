# Layered Agent Memory: Semantic Compression and Operator Doctrine

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-agent-memory-semantic-compression-and-operator-doctrine-fe00287a7e9a`
Run ID: `layered-agent-memory-semantic-compression-and-operator-doctrine-fe00287a7e9a-20260613T083131190358+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/60c87137e46b

## What looked useful

Layered doctrine pinning produced consistent paired gains at the 350-token-unit budget: +0.096 doctrine recall and +0.024 overall recall versus recency over 200 seeds, but preference recall fell by -0.026 and the initial unquotaed variant showed that doctrine can crowd out task memory.

## Boundaries and scale limits

No real LLM summarization, embedding retrieval, natural-language task traces, multi-session persistence, downstream task-success metric, or doctrine-violation measurement was tested. Absolute recall remained low and preference recall regressed under the tested quota.

## Claim scope

On deterministic synthetic structured traces with front-loaded doctrine facts, a quota-based layered memory policy improves doctrine recall and modestly improves overall recall under tight retained-token budgets compared with recency, random reservoir, and flat latest-per-key retention.

## Why it stopped

No-paper useful signal: the result is a synthetic/proxy mechanism test, not direct validation of layered memory in deployed agents.

## Recommended next action

Run a bounded deepen follow-up in a real agent-harness trace replay with LLM summaries, no-compression oracle, recency/latest-per-key baselines, and downstream doctrine-violation plus task-success metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Layered Memory Compression on Real Agent Traces
- Success threshold: At matched token budget, layered memory achieves at least 20% relative reduction in doctrine violations versus the strongest baseline while keeping task success within 2 percentage points of that baseline across at least 100 replayed tasks.
- Stop condition: Stop if layered memory fails to reduce doctrine violations versus the strongest baseline or reduces task success by more than 2 percentage points in two independent trace slices.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-semantic-compression-and-operator-doctrine-fe00287a7e9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
