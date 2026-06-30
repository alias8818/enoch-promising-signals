# Real-agent commitment ledger adherence benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-agent-commitment-ledger-adherence-benchmark-f4fcd6ad11`
Run ID: `real-agent-commitment-ledger-adherence-benchmark-f4fcd6ad11-20260527T035303906204+0000`

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

- Parent run decision: Simplified Commitment Ledger for Agent Plan Adherence: enoch://control-plane/projects/simplified-commitment-ledger-for-agent-plan-adherence-bfde17a8bbdf/runs/simplified-commitment-ledger-for-agent-plan-adherence-bfde17a8bbdf-20260524T181857854854+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f353212c01e

## What looked useful

The ledger condition scored 15/15 commitments and the control condition also scored 15/15, yielding 100% mean adherence in both conditions and 0.0 ledger-minus-control improvement. This directly fails the predeclared support threshold requiring at least a 10 percentage point ledger gain.

## Boundaries and scale limits

Single real agent, three toy repositories, single-turn prompts, explicit commitments, and same-prompt conflict pressure only; no multi-turn memory decay, multi-agent comparison, natural project history, or long-horizon work was tested.

## Claim scope

In a Tier 1 controlled direct test using codex-cli 0.134.0 on three short single-turn file-editing tasks, adding a COMMITMENT_LEDGER.md artifact plus final verification reminder did not improve objective commitment adherence over a clear prose-control prompt.

## Why it stopped

The direct Tier 1 test completed and falsified the predeclared improvement threshold for this scoped single-turn benchmark; this is not a full validation of all ledger mechanisms.

## Recommended next action

Stop this run as no-paper useful evidence; if continuing the line, run a harder multi-turn drift benchmark where the prose-control condition is demonstrably below ceiling before testing ledger benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-turn commitment ledger drift benchmark
- Success threshold: Ledger condition beats prose-control by at least 10 percentage points in mean objective adherence while reaching at least 80% absolute adherence on paired multi-turn tasks.
- Stop condition: Stop if a pilot of 3 paired multi-turn tasks still has prose-control at or above 95% adherence, because the benchmark remains ceiling-limited rather than ledger-sensitive.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-commitment-ledger-adherence-benchmark-f4fcd6ad11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
