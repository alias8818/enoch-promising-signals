# Operator-Model Memory Probe for CPU Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-model-memory-probe-for-cpu-agent-94d098a70851`
Run ID: `operator-model-memory-probe-for-cpu-agent-94d098a70851-20260614T045811985347+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

Layered doctrine memory reached 18/18 correct selections, while flat retrieval reached 13/18 and failed through stale operator rules or noisy model suggestions. Transcript search selected noisy model suggestions in all 18 cases.

## Boundaries and scale limits

Synthetic sanitized corpus only; no live LLM agent, no real operator history distribution, no large corpus, no semantic embedding retrieval, and no long-horizon production trace replay.

## Claim scope

On an 18-task synthetic replay corpus for CPU-agent operator instructions, a layered current-operator-doctrine memory policy selected the valid current rule more reliably than no memory, transcript search, or flat lexical retrieval.

## Why it stopped

Closed as no-paper useful signal because evidence is a bounded synthetic replay, not a live model or full-scale validation.

## Recommended next action

Run a bounded deepen follow-up with a live small LLM agent and 50-100 human-authored replay tasks comparing layered doctrine memory against flat retrieval under authority and recency conflicts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM operator-memory replay with authority and recency conflicts
- Success threshold: Layered doctrine memory improves exact rule-selection accuracy by at least 15 percentage points over flat retrieval and reduces stale/noisy error rate by at least 50% on the bounded replay set.
- Stop condition: Stop if layered doctrine memory improves accuracy by less than 5 percentage points over flat retrieval or if most errors come from ambiguous task labels rather than memory strategy.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-memory-probe-for-cpu-agent-94d098a70851`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
