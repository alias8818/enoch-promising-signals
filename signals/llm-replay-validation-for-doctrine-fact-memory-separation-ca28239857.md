# LLM replay validation for doctrine/fact memory separation in volunteer coordination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-replay-validation-for-doctrine-fact-memory-separation-ca28239857`
Run ID: `llm-replay-validation-for-doctrine-fact-memory-separation-ca28239857-20260628T193658269127+0000`

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

- Parent run decision: Volunteer Coordinator Agent Memory Architecture: Doctrine vs Facts: enoch://control-plane/projects/volunteer-coordinator-agent-memory-architecture-doctrine-vs-facts-447c5a43d2e5/runs/volunteer-coordinator-agent-memory-architecture-doctrine-vs-facts-447c5a43d2e5-20260628T173602216223+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Layered doctrine/fact memory reached 1.000 exact accuracy versus 0.583 for flat retrieval, 0.417 for transcript search, and 0.083 for no memory. Failures in non-layered strategies were traceable to missing doctrine rules, noisy rule-like transcript contamination, and stale/current fact confusion.

## Boundaries and scale limits

Synthetic tasks only; deterministic scorer; no live LLM, embedding retrieval, human labels, field data, extraction-error modeling, or large-scale replay.

## Claim scope

In a 12-task deterministic synthetic volunteer-coordination replay benchmark, typed layered doctrine/fact memory avoided stale-fact and noisy-doctrine failures that affected transcript search and flat retrieval.

## Why it stopped

No-paper closure: this run produced useful synthetic proxy evidence, but not direct LLM replay or field validation.

## Recommended next action

Run a bounded live-LLM replay on the same task schema with retrieved memories injected per strategy and score policy violations plus exact action/channel decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM replay of doctrine/fact memory separation for volunteer coordination
- Success threshold: Layered memory improves exact accuracy by at least 15 percentage points over flat retrieval and reduces policy violations by at least 30 percent without increasing stale-fact errors.
- Stop condition: Stop if layered memory fails to beat flat retrieval on exact accuracy or policy-violation rate on the first 50-task live-LLM replay.

## Evidence references

- Artifact root: `<local-path>/projects/llm-replay-validation-for-doctrine-fact-memory-separation-ca28239857`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
