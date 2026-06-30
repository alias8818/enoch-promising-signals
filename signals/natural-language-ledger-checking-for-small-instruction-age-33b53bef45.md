# Natural-language ledger checking for small instruction agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `natural-language-ledger-checking-for-small-instruction-age-33b53bef45`
Run ID: `natural-language-ledger-checking-for-small-instruction-age-33b53bef45-20260529T070913474039+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tool-call evidence ledger reduces unverified claims in tiny CPU agents: enoch://control-plane/projects/tool-call-evidence-ledger-reduces-unverified-claims-in-tiny-cpu-agents-eb48e52c60d1/runs/tool-call-evidence-ledger-reduces-unverified-claims-in-tiny-cpu-agents-eb48e52c60d1-20260528T211344026230+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2bfc7b76631e

## What looked useful

Ledger prompting produced 0/24 full compliance versus 0/24 baseline, +0.0179 mean partial-score delta versus a +0.05 threshold, and 1.23x latency. Ignoring the FINAL marker gave 1/24 full compliance for both conditions.

## Boundaries and scale limits

Single 0.5B local instruction model, synthetic but direct multi-constraint tasks, greedy decoding, one prompt design, no external verifier, no multi-turn repair, no larger-model or real-agent workflow validation.

## Claim scope

Prompt-only natural-language ledger-and-check instructions did not materially improve exact multi-constraint compliance for Qwen/Qwen2.5-0.5B-Instruct on 24 controlled regex-scoreable instruction tasks.

## Why it stopped

Tier-1 controlled direct test failed the pre-run success threshold; this is an early bounded falsification of the prompt-only mechanism, not a full validation or full disproof of all ledger-checking variants.

## Recommended next action

Stop paper path for prompt-only ledger checking; run one bounded deepening test of a two-pass ledger verifier/repair loop only if the goal is to test a stronger mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-pass ledger verifier and repair for small instruction agents
- Success threshold: Two-pass verifier/repair improves full compliance by >=0.15 absolute over baseline and prompt-only ledger, improves partial score by >=0.05, and keeps mean latency below 3x baseline.
- Stop condition: Stop if two-pass verifier/repair full-compliance delta is <0.15 or partial-score delta is <0.05 on the controlled 24-task benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-ledger-checking-for-small-instruction-age-33b53bef45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
