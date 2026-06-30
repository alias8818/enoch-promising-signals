# Evidence-ledger tool agent with falsifiable claim counterexamples

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7`
Run ID: `evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7-20260629T152552710860+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/237047725527

## What looked useful

Counterexample-aware ledger accuracy was 0.984 versus 0.725 for support-only; unsupported recall was 1.000 versus 0.333; false-supported rate was 0.000 versus 0.667, with supported recall decreasing from 0.996 to 0.973 due to conservative rejection under colliding distractor contradictions.

## Boundaries and scale limits

Synthetic structured claims only; no natural-language extraction, real-document retrieval, LLM tool calls, human UX, source-trust modeling, or publication-grade external benchmark.

## Claim scope

On a 22-claim structured synthetic benchmark repeated across 20 seeds with distractor evidence, explicit counterexample retrieval in an evidence ledger improved unsupported-claim rejection over a support-only lookup baseline.

## Why it stopped

Proxy-only structured synthetic result supports the mechanism but is not a full validation of an evidence-ledger tool agent.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ablation on a curated natural-language claim/evidence benchmark with source provenance and contradiction trust labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language evidence-ledger counterexample ablation
- Success threshold: Unsupported recall improves by at least 0.20 over support-only and supported recall drops by no more than 0.05 on the fixed benchmark.
- Stop condition: Stop if counterexample-aware retrieval fails to improve unsupported recall by 0.10, or if supported recall drops by more than 0.10 after source-trust filtering.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
