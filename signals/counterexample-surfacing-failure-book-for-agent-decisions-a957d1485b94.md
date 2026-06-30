# Counterexample-Surfacing Failure Book for Agent Decisions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-surfacing-failure-book-for-agent-decisions-a957d1485b94`
Run ID: `counterexample-surfacing-failure-book-for-agent-decisions-a957d1485b94-20260628T154506677745+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

Structured counterexample memory can improve decision checks when failure modes are represented as explicit tags; lexical retrieval alone was helpful but noisy, especially on benign controls.

## Boundaries and scale limits

Synthetic authored tasks; no live LLM agent, no held-out production traces, no automatic risk-tag inference, and no dense retrieval or reranking baseline.

## Claim scope

In a 24-task authored replay harness with explicit risk tags, a structured failure book surfaced all required counterexamples and avoided benign false positives, outperforming no-memory and lightweight lexical retrieval baselines.

## Why it stopped

Bounded synthetic replay evidence supports the mechanism but is not direct/full validation of agent decision quality.

## Recommended next action

Stop this run as no-paper useful signal; next run should test held-out real agent traces with blind risk-tag inference and stronger retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out trace validation of counterexample failure-book surfacing
- Success threshold: Failure-book strategy improves required-counterexample recall by at least 15 percentage points over the best retrieval baseline while keeping benign false-positive rate at or below 10%.
- Stop condition: Stop as negative if inferred tags fail to beat the best retrieval baseline on recall or if benign false positives exceed 20%.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-surfacing-failure-book-for-agent-decisions-a957d1485b94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
