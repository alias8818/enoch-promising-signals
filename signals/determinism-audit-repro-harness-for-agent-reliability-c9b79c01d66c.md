# Determinism-Audit Repro Harness for Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `determinism-audit-repro-harness-for-agent-reliability-c9b79c01d66c`
Run ID: `determinism-audit-repro-harness-for-agent-reliability-c9b79c01d66c-20260620T171327304002+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e42eb863dd25

## What looked useful

The harness produced 360 replay records. Stable controls had deterministic_group_rate 1.000, while the intentionally hash-order-sensitive policy had deterministic_group_rate 0.000 with 12/12 unstable task/seed groups.

## Boundaries and scale limits

Evidence is limited to four synthetic tasks, six local policy/memory strategies, three RNG seeds, five Python hash seeds, and one Python/platform environment. It does not validate real LLM providers, distributed agents, live tool APIs, or production trace replay.

## Claim scope

A local synthetic replay harness can detect seed/hash-order-sensitive nondeterminism in an agent-like memory/action control loop while stable controls remain reproducible.

## Why it stopped

Closed as no-paper useful signal because the run directly validated the harness on synthetic controls but did not audit a real agent stack.

## Recommended next action

Use this harness shape on a small corpus of real saved agent traces with pinned model/provider/tool configurations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay real agent traces through determinism-audit harness
- Success threshold: Either deterministic_group_rate >= 0.99 for the pinned real-trace baseline with no unexplained divergences, or at least one divergence localized to a concrete mechanism with a minimal reproducer.
- Stop condition: Stop if trace sanitization or provider/tool fixture pinning cannot be achieved locally, or if 20 trace replays complete with no divergences and no mechanism beyond the synthetic proxy.

## Evidence references

- Artifact root: `<local-path>/projects/determinism-audit-repro-harness-for-agent-reliability-c9b79c01d66c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
