# Evidence-Ledger Agent on Reproducible Tool Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-on-reproducible-tool-tasks-f4f1cbad0b94`
Run ID: `evidence-ledger-agent-on-reproducible-tool-tasks-f4f1cbad0b94-20260620T222833578031+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8478ec7cb8b7

## What looked useful

Predicate-plus-digest evidence ledgers caught 37/37 injected invalid claims with 0/24 false rejections; a citation-presence baseline accepted all 37 invalid claims.

## Boundaries and scale limits

Synthetic local traces only; no live LLM agent, no natural-language claim extraction, no ambiguous evidence, and no large external benchmark.

## Claim scope

On 24 deterministic synthetic tool tasks with machine-checkable predicates, an evidence-ledger verifier using cited evidence references, canonical observation digests, and explicit predicates rejected all injected unsupported or tampered claims while accepting all valid claims.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy and does not validate real-agent transcript robustness.

## Recommended next action

Run the same ledger contract on held-out real or replayed tool-agent transcripts with natural-language claim extraction and adversarial drift labels before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger verification on replayed real tool-agent transcripts
- Success threshold: Reject at least 80% of labeled invalid claims with no more than 5% false rejection of valid claims and outperform both baselines by at least 30 percentage points in invalid detection rate.
- Stop condition: Stop if natural-language claim extraction cannot produce auditable predicates for at least 80% of candidate claims or if false rejections exceed 10% in a 30-claim pilot.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-on-reproducible-tool-tasks-f4f1cbad0b94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
