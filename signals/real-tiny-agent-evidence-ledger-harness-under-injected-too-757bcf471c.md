# Real Tiny-Agent Evidence Ledger Harness Under Injected Tool Noise

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-agent-evidence-ledger-harness-under-injected-too-757bcf471c`
Run ID: `real-tiny-agent-evidence-ledger-harness-under-injected-too-757bcf471c-20260604T182205831953+0000`

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

- Parent run decision: Evidence Ledger for Tiny CPU Agent Reliability: enoch://control-plane/projects/evidence-ledger-for-tiny-cpu-agent-reliability-e63a222e3265/runs/evidence-ledger-for-tiny-cpu-agent-reliability-e63a222e3265-20260604T113721280367+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

The bounded harness met the stated Tier 1 threshold: at noise rates >= 0.40, ledger accuracy was 1.0, ledger advantage over the no-ledger parser ranged from 0.4486 to 0.6620, and injected evidence admissions were zero. The no-ledger parser degraded from 0.5514 accuracy at 0.40 noise to 0.3380 at 0.80 noise.

## Boundaries and scale limits

The run does not test real LLM agents, natural-language prompt injection, learned tool-use behavior, multi-step planning, realistic web/API tools, or adversaries that can forge valid verifier values.

## Claim scope

In a deterministic tiny-agent simulation with synthetic tool observations, a ledger admission rule requiring matching task id, requested field, call id, and verifier preserved exact-answer accuracy and blocked injected evidence across 25,000 controlled trials at noise rates from 0.0 to 0.8.

## Why it stopped

No-paper useful signal: the mechanism is supported in a controlled deterministic harness, but publication readiness requires real-agent and natural-language injection evidence.

## Recommended next action

Run a deepen follow-up with a small real LLM/tool loop where the model must select, cite, and answer from ledger-admitted evidence under natural-language injected observations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small LLM Evidence Ledger Under Natural-Language Tool Injection
- Success threshold: At noise_rate >= 0.40, ledger-enforced LLM accuracy improves by at least 15 percentage points over no-ledger control and injected-evidence citation rate is below 5 percent without increasing abstentions by more than 10 percentage points.
- Stop condition: Stop if the ledger-enforced LLM does not improve accuracy by at least 10 percentage points or still cites injected evidence at 10 percent or higher on the first 200 matched traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-agent-evidence-ledger-harness-under-injected-too-757bcf471c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
