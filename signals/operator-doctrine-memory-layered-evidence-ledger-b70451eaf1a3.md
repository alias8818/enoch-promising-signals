# Operator-Doctrine Memory: Layered Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-layered-evidence-ledger-b70451eaf1a3`
Run ID: `operator-doctrine-memory-layered-evidence-ledger-b70451eaf1a3-20260613T143132679904+0000`

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

Across 32,000 main-run queries per resolver, the layered ledger achieved 1.000 action and provenance accuracy by construction of the declared authority/evidence rule, while the best flat action baseline reached 0.394 and the best flat provenance baseline reached 0.179. Robustness sweeps showed +0.562 to +0.634 action-accuracy deltas and +0.786 to +0.848 provenance deltas.

## Boundaries and scale limits

Synthetic events only; no natural-language retrieval, real operator traces, multi-agent memory, production latency, or human-authored doctrine corpus was tested.

## Claim scope

In a synthetic symbolic doctrine-conflict benchmark, an explicit layered evidence ledger resolved authority/evidence conflicts and preserved provenance better than recency, majority, and evidence-only flat-memory baselines.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct/full validation of operator-doctrine memory in realistic traces.

## Recommended next action

Stop as no-paper useful signal; run a bounded natural-language follow-up with independently authored doctrine scenarios, retrieval/extraction noise, and the same flat-memory baselines before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Doctrine Ledger Conflict Benchmark
- Success threshold: Layered ledger improves action accuracy by at least 15 percentage points and provenance accuracy by at least 25 percentage points over the best flat baseline, with p95 query latency under 50 ms on the bounded corpus.
- Stop condition: Stop if the layered ledger fails to beat the best flat baseline by 5 percentage points on either action or provenance accuracy after parser/retriever sanity checks.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-layered-evidence-ledger-b70451eaf1a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
