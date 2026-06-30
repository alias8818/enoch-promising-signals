# Evidence Ledger Verification for Local Small LLM Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-verification-for-local-small-llm-tool-agen-ae43e11ff4`
Run ID: `evidence-ledger-verification-for-local-small-llm-tool-agen-ae43e11ff4-20260608T163605689197+0000`

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

- Parent run decision: Evidence Ledger for Tool-Calling Small Agents: enoch://control-plane/projects/evidence-ledger-for-tool-calling-small-agents-11561613a664/runs/evidence-ledger-for-tool-calling-small-agents-11561613a664-20260608T141545150249+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/92313955d92d

## What looked useful

Ledger verification achieved 100% corrupt detection and 100% clean acceptance in both a 200-case primary run and a 1,250-case repeat. Transcript-only auditing detected only final-claim mismatches and missed transcript tampering, ledger-output tampering, and fabricated tool observations, giving 25% corrupt detection.

## Boundaries and scale limits

Validated on 1,450 total synthetic local traces across two seeds, deterministic single-step tools, and structured JSON claims. Not validated on real instruction-tuned small LLM agents, natural-language claim extraction, multi-step plans, non-deterministic tools, side-effecting tools, or adaptive attackers with pre-anchor ledger write access.

## Claim scope

In controlled local deterministic tool-agent traces, an append-only hashed evidence ledger with deterministic replay detects final-claim, transcript-observation, ledger-output, and fabricated-tool corruptions while accepting clean traces.

## Why it stopped

Controlled Tier 1 threshold was met, but the evidence is mechanism-only and not paper-positive validation of deployed local small LLM tool agents.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded real local small-LLM tool-agent test that measures natural-language claim extraction, clean false positives, and multi-step ledger replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LLM Evidence Ledger Verification on Multi-Step Tool Traces
- Success threshold: Ledger corrupt-detection rate >= 0.95, clean-acceptance rate >= 0.95, and transcript-only baseline misses at least one tamper class that the ledger catches on real model-generated traces.
- Stop condition: Stop if clean false rejections exceed 10% after parser fixes, if local model/tool execution cannot produce at least 100 valid traces within the CPU/GPU budget, or if ledger detection falls below 90% on any core corruption class.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verification-for-local-small-llm-tool-agen-ae43e11ff4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
