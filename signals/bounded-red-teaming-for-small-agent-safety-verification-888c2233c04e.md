# Bounded Red-Teaming for Small Agent Safety Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-red-teaming-for-small-agent-safety-verification-888c2233c04e`
Run ID: `bounded-red-teaming-for-small-agent-safety-verification-888c2233c04e-20260607T041915180413+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Bounded exhaustive verification is practical for genuinely small finite-state agents, but naive coverage-guided bounded red-teaming is not validated by this benchmark: guided recall was 0.1616 on unsafe agents versus 0.2475 for random probing, with zero false positives for both on bounded-safe agents.

## Boundaries and scale limits

No real LLM agents, natural-language prompts, external tools, stochastic policies, or semantic safety oracle were tested. The benchmark used one seed, finite deterministic policies, injected exact trigger paths of length 2-5, depth 5, and budget 300 for guided/random probes.

## Claim scope

On 300 synthetic deterministic finite-state agents with alphabet size 10 and bounded depth 5, exhaustive enumeration provided complete unsafe/safe status within the bound at 111111 queries per agent. The tested naive coverage-guided bounded red-team search did not outperform equal-budget random probing overall.

## Why it stopped

This is a proxy/toy finite-state result: exhaustive bounded verification is supported in the tested scope, but the red-team heuristic claim is mixed/negative and not enough for a paper or broad safety-verification claim.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up comparing stronger prefix-state novelty and symbolic/backward search strategies against random on multiple seeds and small executable tool-agent tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Seed Bounded Search Strategies for Small Tool-Agent Verification
- Success threshold: Across at least 3 seeds, the improved bounded search should exceed random recall by at least 10 percentage points on unsafe cases at equal budget, maintain zero false positives on bounded-safe cases, and show the advantage on at least one executable non-synthetic small-agent task.
- Stop condition: Stop if improved bounded search fails to beat random recall by 5 percentage points on two consecutive seeds or produces any unexplained false positive against exhaustive ground truth.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-red-teaming-for-small-agent-safety-verification-888c2233c04e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
