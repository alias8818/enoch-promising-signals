# Evidence Ledger Agent Reliability on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-on-cpu-0a2382227de1`
Run ID: `evidence-ledger-agent-reliability-on-cpu-0a2382227de1-20260608T071443506500+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

Across 2,000 cases per condition, the source-weighted ledger matched the baseline at 1.000 clean accuracy and improved adversarial-condition accuracy by 0.3005 to 0.3885 absolute with paired bootstrap CIs excluding zero. A no-source-weight ablation failed under unreliable recent false claims, indicating source attribution and weighting are central to the mechanism.

## Boundaries and scale limits

Toy structured observations only; no production LLM agent, real document retrieval, extraction errors, multi-step tool use, learned source reliability, or large benchmark validation.

## Claim scope

In a deterministic synthetic CPU harness, a source-weighted evidence ledger improved fact-retrieval accuracy over a last-mention baseline under stale and unreliable contradictory observations while preserving clean-control accuracy.

## Why it stopped

No-paper useful signal: the current evidence is a synthetic mechanism proxy, not direct production-agent reliability validation.

## Recommended next action

Run a bounded real-agent follow-up using a small CPU-capable LLM/tool-use harness with document-derived evidence extraction and compare against citation voting or self-consistency baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence ledger reliability on document-derived tasks
- Success threshold: At least 10 percentage-point absolute accuracy improvement or unsupported-claim reduction over the strongest baseline on 500 or more document-derived tasks, with no clean-control regression above 2 percentage points.
- Stop condition: Stop if the ledger cannot beat the strongest baseline by 5 percentage points on a 100-task pilot or if extraction errors dominate more than half of ledger failures.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-cpu-0a2382227de1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
