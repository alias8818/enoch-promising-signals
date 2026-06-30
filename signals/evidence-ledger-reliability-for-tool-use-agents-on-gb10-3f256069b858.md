# Evidence-Ledger Reliability for Tool-Use Agents on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reliability-for-tool-use-agents-on-gb10-3f256069b858`
Run ID: `evidence-ledger-reliability-for-tool-use-agents-on-gb10-3f256069b858-20260628T152456190799+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d78c17e285c4

## What looked useful

Across four 20,000-task scenarios, ledger accuracy exceeded baseline accuracy by +0.1571 to +0.3988, with main-scenario accuracy 0.9675 vs 0.6132 and conflict recall 1.0. The mechanism appears useful enough to justify a real-agent follow-up, but not enough for a paper.

## Boundaries and scale limits

Synthetic integer facts only; no real LLM agent, natural-language tool output, production API traces, learned trust model, or latency/cost integration. The baseline is intentionally simple and should not be treated as the strongest possible non-ledger agent.

## Claim scope

In a dependency-free synthetic multi-tool fact-retrieval benchmark with known ground truth, noisy supported observations, missing evidence IDs, and adversarial contradictions, a provenance-preserving evidence ledger improved final-answer accuracy and surfaced conflicts compared with a latest-observation baseline.

## Why it stopped

Closed as no-paper useful signal: the current evidence is synthetic mechanism evidence, not publication-grade validation of real tool-use agents.

## Recommended next action

Run a bounded real-agent follow-up using recorded or live tool traces and a stronger baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger reliability on real tool-use traces
- Success threshold: At least 10 percentage-point unsupported-claim reduction or 5 percentage-point accuracy gain over the strongest baseline, with less than 25% latency overhead and auditable evidence links for at least 95% of supported final claims.
- Stop condition: Stop if ledger overhead exceeds 50% without accuracy or unsupported-claim improvement, or if conflict detection has poor precision on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reliability-for-tool-use-agents-on-gb10-3f256069b858`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
