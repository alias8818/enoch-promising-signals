# Medium Realistic Trace-Locked Ledger Evaluation for Tool-Agent Claim Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-realistic-trace-locked-ledger-evaluation-for-tool-a-69fed5462b`
Run ID: `medium-realistic-trace-locked-ledger-evaluation-for-tool-a-69fed5462b-20260621T061136291965+0000`

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

- Parent run decision: Trace-Locked Evidence Ledger for Tool-Using Agents: enoch://control-plane/projects/trace-locked-evidence-ledger-for-tool-using-agents-04fcc74d3021/runs/trace-locked-evidence-ledger-for-tool-using-agents-04fcc74d3021-20260621T053402392492+0000
- Parent run decision: Real Trace-Locked Ledger Evaluation for Tool-Agent Claims: enoch://control-plane/projects/real-trace-locked-ledger-evaluation-for-tool-agent-claims-f49f5cec4f/runs/real-trace-locked-ledger-evaluation-for-tool-agent-claims-f49f5cec4f-20260621T055511310265+0000

## What looked useful

Trace locking, latest-state indexing, and evidence-ID binding each addressed a distinct failure mode: stale-claim false support in retrieval baselines, tamper invisibility without hash locking, and poor citation fidelity without evidence binding.

## Boundaries and scale limits

The evidence uses synthetic but realistic replay fixtures and deterministic verifier algorithms, not live LLM agents, private production tool logs, or human-authored ambiguous claims.

## Claim scope

On deterministic fixed-seed replay traces with 120 cases and 1440 claims, a trace-locked ledger verifier improves claim verification accuracy over transcript-search and flat-retrieval baselines, eliminates false support on unsupported claims, preserves exact evidence binding, and detects row tampering.

## Why it stopped

Tier 2 medium replay passed the predefined thresholds, but the result remains no-paper because live LLM agent behavior and non-synthetic traces were not directly tested.

## Recommended next action

Run a bounded live-agent replay using the same fixed traces and ablation matrix, requiring generated agent claims to cite ledger evidence IDs before any paper-positive decision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent trace-locked ledger replay for claim verification
- Success threshold: Trace-locked ledger false-support rate on unsupported claims at least 20 pp lower than both real baselines, exact citation/correct-reject rate >= 0.95, tamper detection = 1.0, and no more than 5 pp accuracy loss versus the deterministic verifier on the same traces.
- Stop condition: Stop negative if live agents frequently omit or fabricate evidence IDs such that exact citation/correct-reject rate falls below 0.90 or if false-support reduction versus either real baseline is under 10 pp.

## Evidence references

- Artifact root: `<local-path>/projects/medium-realistic-trace-locked-ledger-evaluation-for-tool-a-69fed5462b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
