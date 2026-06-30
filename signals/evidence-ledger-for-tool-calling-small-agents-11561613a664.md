# Evidence Ledger for Tool-Calling Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tool-calling-small-agents-11561613a664`
Run ID: `evidence-ledger-for-tool-calling-small-agents-11561613a664-20260608T141545150249+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/92313955d92d

## What looked useful

Across 40000 clean-tool synthetic cases, baseline unsupported-answer rate was 0.145125 while ledger unsupported-answer rate was 0.0 with about 326 bytes of ledger data and 0.0027 ms added verification time per case. With a 5% tool-error boundary condition, ledger accuracy fell to 0.912875 and unsupported rate rose to 0.087125, showing the ledger verifies against recorded evidence but cannot make false evidence true.

## Boundaries and scale limits

No real LLM agents, natural-language tool traces, multi-turn web/code tasks, adversarial prompt behavior, or large-scale serving workloads were tested. The result is a CPU-only deterministic proxy over synthetic lookup, aggregation, comparison, and threshold tasks.

## Claim scope

In a synthetic structured tool-calling benchmark, a lightweight evidence ledger that records exact tool outputs and reconstructs final answers from those records eliminates post-tool scratchpad-induced unsupported answers when tool outputs are correct, and exposes a clear boundary when tool outputs themselves are faulty.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct evidence for real small LLM tool-calling agents or publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, wrap the same ledger protocol around actual local small LLM agents and compare against transcript-only and self-check baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Verification for Local Small LLM Tool Agents
- Success threshold: Ledger variant reduces unsupported-claim rate by at least 30% relative to transcript-only and self-check controls while adding less than 20% median latency on at least 500 real model-agent episodes.
- Stop condition: Stop if ledger overhead exceeds 50% median latency or unsupported-claim reduction is below 10% in a 100-episode pilot.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-calling-small-agents-11561613a664`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
