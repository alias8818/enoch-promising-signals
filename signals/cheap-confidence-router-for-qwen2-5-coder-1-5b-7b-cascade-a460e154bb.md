# Cheap Confidence Router for Qwen2.5-Coder 1.5B/7B Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheap-confidence-router-for-qwen2-5-coder-1-5b-7b-cascade-a460e154bb`
Run ID: `cheap-confidence-router-for-qwen2-5-coder-1-5b-7b-cascade-a460e154bb-20260516T214224053004+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/97ffa072f350

## What looked useful

Minimum generated-token logprob from the 1.5B model had AUC 0.741 for 1.5B correctness and recovered 3 of 5 7B-fixable 1.5B failures while routing 37.5% of tasks. Mean logprob was weaker, recovering 2 fixes only at 50% routing. The mechanism is promising but feature-sensitive and not paper-positive.

## Boundaries and scale limits

Small embedded benchmark only; no public held-out benchmark, no multiple seeds, no trained calibration split, no production latency or dollar-cost measurement, and no robustness testing across prompt styles or decoding settings.

## Claim scope

On a 24-task embedded Python coding benchmark using actual Qwen2.5-Coder-1.5B-Instruct and Qwen2.5-Coder-7B-Instruct greedy generations, cheap 1.5B token-confidence features were informative. The best feature, minimum generated-token logprob, improved pass@1 from 11/24 to 14/24 while routing 9/24 prompts to 7B, compared with 16/24 for always using 7B.

## Why it stopped

Tier 1 direct test produced useful but non-paper evidence: the router improves over 1.5B but remains below 7B-only and was validated only on a small embedded task set.

## Recommended next action

Run a held-out public benchmark confirmation with a pre-registered minimum-token-logprob router threshold and compare against always-1.5B, always-7B, random routing, and oracle routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out MBPP/HumanEval confirmation for minimum-token-logprob Qwen2.5-Coder cascade routing
- Success threshold: Route <=40% of prompts to 7B, improve pass@1 by at least 8 percentage points over always-1.5B, recover at least 50% of the always-7B lift, beat random routing at the same route rate, and remain within 8 pass points of always-7B.
- Stop condition: Stop as unsupported if confidence AUC for 1.5B correctness is below 0.65 or if the pre-registered <=40% router recovers less than half of the 7B lift over 1.5B.

## Evidence references

- Artifact root: `<local-path>/projects/cheap-confidence-router-for-qwen2-5-coder-1-5b-7b-cascade-a460e154bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
