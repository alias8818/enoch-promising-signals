# Small-Agent Evidence Ledger with Rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-agent-evidence-ledger-with-rollback-1ce70bd75f24`
Run ID: `small-agent-evidence-ledger-with-rollback-1ce70bd75f24-20260522T142314527859+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/04fb381aed47

## What looked useful

Lazy rollback achieved 1.000 mean accuracy and 0 stale derived claims in all tested synthetic settings. Naive cached memory retained stale claims: 67.94 mean stale claims in the main run and 525.78 in the scale probe. Lazy rollback cost about 1.43-1.45x naive cache time, about 0.80-0.82x full recompute in the main/scale probes, but approached or exceeded full recompute at high correction density and fan-in.

## Boundaries and scale limits

Validated only in local CPU synthetic simulations: smoke 3 seeds, main 100 seeds at 128 facts/512 derived claims, scale probe 50 seeds at 512 facts/4096 derived claims, and a 9-setting sweep at 40 seeds each. No real LLM agents, natural-language evidence extraction, persistence layer, concurrent writes, or production task workflow was tested.

## Claim scope

On deterministic synthetic small-agent traces where derived Boolean claims depend on corrected source evidence, a dependency-aware lazy rollback ledger eliminated stale derived claims and was usually cheaper than full recompute when corrections touched a minority of dependencies.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by synthetic rollback traces, not direct evidence from real agent workflows.

## Recommended next action

Run a bounded deepen follow-up that integrates the ledger into a real small-agent workflow with natural-language evidence links, injected source corrections, persistence checks, and task-level recovery metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Agent Evidence Ledger Rollback Harness
- Success threshold: Across at least 100 correction-injected tasks, lazy rollback reduces stale unsupported final claims by at least 50% versus append-only memory while preserving answer accuracy within 2 percentage points of full recompute and using less mean correction-to-answer latency than full recompute.
- Stop condition: Stop if rollback cannot be made persistent and deterministic, or if it fails to reduce stale unsupported final claims by at least 25% versus append-only memory in a 30-task pilot.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-evidence-ledger-with-rollback-1ce70bd75f24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
