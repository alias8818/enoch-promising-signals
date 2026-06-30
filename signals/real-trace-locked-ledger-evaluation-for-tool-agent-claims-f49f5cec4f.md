# Real Trace-Locked Ledger Evaluation for Tool-Agent Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-locked-ledger-evaluation-for-tool-agent-claims-f49f5cec4f`
Run ID: `real-trace-locked-ledger-evaluation-for-tool-agent-claims-f49f5cec4f-20260621T055511310265+0000`

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
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/299036acf659

## What looked useful

Layered ledger verification achieved F1 1.0 and unsupported-claim leak rate 0.0, while transcript_search and flat_retrieval each leaked all 6 unsupported decoy claims with F1 0.6667.

## Boundaries and scale limits

Small deterministic controlled trace set; not production traces; structured fact_key/value claims only; exact equality verification only; no free-form claim extraction, paraphrase entailment, heterogeneous tools, or long multi-turn sessions.

## Claim scope

In a controlled Tier 1 replay of 3 executed local tool traces and 12 structured claims, exact verification against trace-locked ledger facts prevented unsupported decoy transcript claims better than no-memory, raw transcript search, and flat retrieval baselines.

## Why it stopped

No-paper useful signal: the Tier 1 direct controlled test supports the mechanism but is too small and controlled for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with at least 30 realistic multi-turn traces and 120 claims, including free-form claim extraction and paraphrase/noisy transcript variants.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Realistic Trace-Locked Ledger Evaluation for Tool-Agent Claim Verification
- Success threshold: Ledger strategy F1 >= 0.85, unsupported-claim leak rate <= 0.10, and F1 at least 0.15 above the best non-ledger baseline.
- Stop condition: Stop as not worth paper if ledger F1 < 0.75, leak rate > 0.20, or the advantage over the best non-ledger baseline is < 0.05 after 120 claims.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-locked-ledger-evaluation-for-tool-agent-claims-f49f5cec4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
