# Compressed Ledger Memory on Real Agent Resume Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-ledger-memory-on-real-agent-resume-traces-718bb1803f`
Run ID: `compressed-ledger-memory-on-real-agent-resume-traces-718bb1803f-20260526T200541215442+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Agent State Ledger with Compressed Memory: enoch://control-plane/projects/agent-state-ledger-with-compressed-memory-c6c0320f7141/runs/agent-state-ledger-with-compressed-memory-c6c0320f7141-20260525T094349054851+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f262c98f3c9e

## What looked useful

At 25% trace bytes, compressed ledger mean recall was 0.5194 versus recency 0.6309, failing the >=0.65 recall and >=0.15 margin threshold. At 50% bytes, compressed recall rose to 0.7409 versus recency 0.6733, a small positive signal that structured ledgers may help only at looser budgets.

## Boundaries and scale limits

Tested 12 local traces, up to 260 events and 80 oracle facts per case. Scoring used deterministic lexical coverage of commands, artifacts, metrics, and decision facts, not LLM resume quality or human semantic grading.

## Claim scope

A deterministic compressed ledger built from real local Codex/Enoch JSONL resume traces did not meet a 25% byte-budget lexical recall threshold against run_notes-derived resume facts; at 50% budget it beat recency weakly but not by the required margin.

## Why it stopped

Direct small test on real resume traces failed the stated threshold; the 50% budget signal is useful but too weak and proxy-scored for paper readiness.

## Recommended next action

Stop this run as a Tier 1 negative against the 25% deterministic lexical-recall threshold; if deepening, run a bounded LLM-in-the-loop resume benchmark using the same trace cases and equal token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop compressed ledger resume benchmark on real local agent traces
- Success threshold: Compressed ledger must improve resume-state answer accuracy by at least 0.15 absolute over recency at a 25% token budget and must not reduce artifact/decision consistency on more than one case.
- Stop condition: Stop if compressed ledger is not at least 0.05 absolute above recency after the first 6 real traces, or if failures are dominated by missing facts already absent from the compressed memory.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-ledger-memory-on-real-agent-resume-traces-718bb1803f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
