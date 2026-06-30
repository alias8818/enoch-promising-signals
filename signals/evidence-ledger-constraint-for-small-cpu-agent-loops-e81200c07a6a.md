# Evidence-ledger constraint for small CPU agent loops

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-small-cpu-agent-loops-e81200c07a6a`
Run ID: `evidence-ledger-constraint-for-small-cpu-agent-loops-e81200c07a6a-20260608T082610296465+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/97e96394eeb2

## What looked useful

The evidence-ledger constraint appears useful for preventing unsupported synthesis in small CPU agent loops, but it should be paired with evidence-quality checks because exact ledger support can still be stale or false.

## Boundaries and scale limits

Synthetic/proxy-only result. It does not test LLM generation, real tool APIs, long-horizon planning, real task distributions, source trust ranking, or citation checking by independent judges. The ledger does not detect corrupt exact evidence; corrupt-supported rate was 0.1130 for ledger versus 0.1096 for baseline.

## Claim scope

In a deterministic synthetic CPU retrieval-agent abstraction with noisy retrieval, distractors, missing evidence, and corrupted snippets, a hard evidence-ledger final-answer constraint reduced unsupported claims from 0.0766 to 0.0000 and improved aggregate accuracy from 0.8199 to 0.8581, while increasing abstention from 0.0000 to 0.0289.

## Why it stopped

Stopped after a reproducible synthetic/proxy useful signal; this is not full validation and is not paper-ready.

## Recommended next action

Run a bounded deepen follow-up around an actual small local LLM or production-style CPU agent harness with independently checked citation support and answer correctness on real tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU-agent citation support test for evidence-ledger constraints
- Success threshold: Unsupported-claim rate is reduced by at least 50% relative to baseline, accuracy over all tasks drops by no more than 5 percentage points, and latency overhead remains below 20%.
- Stop condition: Stop as negative if unsupported-claim reduction is below 25%, accuracy drops by more than 10 percentage points, or most residual failures come from corrupted cited evidence that the ledger cannot distinguish.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-small-cpu-agent-loops-e81200c07a6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
