# Falsifiable Agent Traces with Counterexample Preservation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-agent-traces-with-counterexample-preservation-21903bf43e8b`
Run ID: `falsifiable-agent-traces-with-counterexample-preservation-21903bf43e8b-20260610T012651912954+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bc71408406bd

## What looked useful

Counterexample-preserving compaction falsified 100% of false claims with relevant counterexamples at budgets 320, 480, 800, and 1600 bytes, with 0% false positives on true claims and 0% falsification when counterexamples were missing or irrelevant. Full-prefix needed much larger budgets and lossy-latest never retained falsifying evidence in this setup.

## Boundaries and scale limits

Evidence is limited to deterministic synthetic linear-function traces, deterministic compactors, and offline verification against known ground truth. It does not validate real LLM agents, natural-language-only traces, adversarial/noisy counterexamples, or production summarizers.

## Claim scope

On a synthetic executable arithmetic-trace benchmark, preserving claim-linked counterexamples in compacted traces keeps false final claims locally falsifiable at 320 bytes and above when the original trace contains a relevant valid counterexample.

## Why it stopped

Synthetic mechanism evidence is positive but not direct or broad enough for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same verifier contract on real agent/tool traces with machine-checkable assertions and a real summarization baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample-preserving compaction on real machine-checkable agent traces
- Success threshold: At matched budgets, counterexample-preserving compaction improves false-claim falsification by at least 25 percentage points over the strongest baseline while keeping true-claim false-positive falsification under 1%.
- Stop condition: Stop if real traces rarely contain machine-checkable claim-linked counterexamples, if preserved counterexamples produce more than 1% false-positive falsifications, or if the strongest baseline is within 10 percentage points at practical budgets.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-agent-traces-with-counterexample-preservation-21903bf43e8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
