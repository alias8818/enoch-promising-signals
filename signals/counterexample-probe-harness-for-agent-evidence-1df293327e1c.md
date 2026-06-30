# Counterexample Probe Harness for Agent Evidence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-probe-harness-for-agent-evidence-1df293327e1c`
Run ID: `counterexample-probe-harness-for-agent-evidence-1df293327e1c-20260613T151032545332+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d76f7b50682f

## What looked useful

A replayable Python harness found all 6,000 injected unsound synthetic cases with 0 false positives on 1,000 sound controls, while the naive citation-id baseline found none. This supports counterexample probing as a practical validator scaffold, not as a paper-ready result.

## Boundaries and scale limits

7,000 synthetic local cases only; no live LLM agents, no real tool traces, no human-labeled evidence corpus, and probes are tailored to generated fault families.

## Claim scope

On deterministic synthetic evidence bundles, targeted counterexample probes detect six common agent-evidence failure classes that a citation-id-exists baseline misses.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic/proxy-only and not full validation of real agent evidence behavior.

## Recommended next action

Run the same probe categories on a small human-reviewed corpus of real agent traces before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample probes on real agent evidence traces
- Success threshold: Recall at least 0.50 on human-labeled unsupported evidence claims with precision at least 0.90 and false-positive rate below 0.10 on sound claims.
- Stop condition: Stop if probes cannot be mapped to real traces without manual trace-specific rules, or if precision falls below 0.80 after tuning only generic probe thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-probe-harness-for-agent-evidence-1df293327e1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
